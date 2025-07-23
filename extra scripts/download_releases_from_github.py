import requests
import os
import zipfile
import re
import shutil
import config
import concurrent.futures
#                        '     github TOKEN HERE     '
#                                  | |
#                                  | |
#                                   V
GITHUB_TOKEN = 'Bearer '+ config.GITHUB_TOKEN

MAX_RELEASES_TO_DOWNLOAD = config.MAX_RELEASES_TO_DOWNLOAD


def printLog(text,out):
    print(text,file=out)
    print(text)
    
def uzip_and_move(zip_name):
    extraction_dir = zip_name.split(".zip")[0]
    if not os.path.exists(extraction_dir):
        os.makedirs(extraction_dir)
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extraction_dir)
    extracted_dir = os.path.join(extraction_dir, os.listdir(extraction_dir)[0])
    for item in os.listdir(extracted_dir):
        shutil.move(os.path.join(extracted_dir, item), os.path.join(extraction_dir, item))
    os.rmdir(extracted_dir)


def download_and_unzip_releases(out, link, limit):
    username, repo = get_username_repo_from_link(link)
    url = 'https://api.github.com/repos/'+username+'/'+repo+'/releases'

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': GITHUB_TOKEN,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        directory_name = username+"_"+repo
        # Create a directory
        for item in json_data:
            if len(item.get('zipball_url', '')) > 0:
                os.makedirs(directory_name, exist_ok=True)
                break
            else:
                printLog(f"No releases found for {username}/{repo}. [ {link} ]", out)
                return -2
        count=0
        for item in json_data:
            if count==limit:
                break
            zipball_url = item['zipball_url']

            tag_name = item['tag_name']
            response1 = requests.get(zipball_url, headers=headers)
            with open(f"{directory_name}/{tag_name}.zip", "wb") as file:
                file.write(response1.content)
            if response1.status_code!=200:
                print(f"[{tag_name}] Request failed with status code: {response1.status_code}")
            else:
                uzip_and_move(f"{directory_name}/{tag_name}.zip")
                #with zipfile.ZipFile(f"{directory_name}/{tag_name}.zip", 'r') as zip_ref:
                #    zip_ref.extractall(f"{directory_name}/{tag_name}")
                os.remove(f"{directory_name}/{tag_name}.zip")
                print(f"[{username}]/[{repo}] -> [{tag_name}] done")
                count+=1
        printLog(f"Done downloading {username}/{repo}. Total releases: {count}. [ {link} ]", out)
        return 0
    else:
        printLog(f"Error downloading {username}/{repo}.Response code: {response.status_code}. [ {link} ]", out)
        return -1

import re

def get_username_repo_from_link(link):
    pattern = r'https://github.com/([\w-]+)/([\w-]+)'
    match = re.match(pattern, link)
    if match:
        username = match.group(1)
        repo = match.group(2)
        return username, repo
    else:
        return None, None

def download_link(link):
   
    return_code = download_and_unzip_releases(out, link, MAX_RELEASES_TO_DOWNLOAD)
    return return_code

if __name__ == '__main__':
    out = open('Download_from_github_logs.txt', 'w')
    printLog("Starting...\n", out)
    with open('github_links_list.txt', 'r') as file:
        links = file.readlines()
        links = [link.strip() for link in links]

    with concurrent.futures.ThreadPoolExecutor() as executor: 
        results = executor.map(download_link, links)
        
    count_successful = 0
    count_failed = 0
    for result in results:
        if result == 0:
            count_successful+=1
        else:
            count_failed+=1
            
    printLog(f"\nSuccessful: {count_successful}\nFailed: {count_failed}", out)
    out.close()
