from pathlib import Path
import shutil
import os
#return the name of an html file
def html_file_name(name1,folder_name1,folder_name2):
    name = "'["+folder_name1+"]["+folder_name2+"]" + name1.split(folder_name1)[1].replace("/","⁄").replace("\\","⁄")+"'.html"
    return Path(name)

#creates the result folders and returns their name
#if folder_name2 is none, the input is a project name folder
def create_end_return_export_folder(folder_name1,folder_name2=None):
    os.makedirs("Results", exist_ok=True)
    if folder_name2!=None:
        name = "["+folder_name1+"]["+folder_name2+"]"
        export_folder_path =  "Results" / Path(name)
    else:
        export_folder_path =  "Results" / Path(folder_name1)
    html_files_folder_path =  export_folder_path / "html_files"
    if not export_folder_path.exists():
        export_folder_path.mkdir()
    else:
        shutil.rmtree( export_folder_path)
        export_folder_path.mkdir()
    html_files_folder_path.mkdir()
    return export_folder_path,html_files_folder_path


def get_subfolder_pairs(folder_path):
   try:
       sub_folders = sorted([f.path for f in os.scandir(folder_path) if f.is_dir()])
       pairs = []
       for i in range(len(sub_folders) - 1):
           pair = [sub_folders[i], sub_folders[i + 1]]
           pairs.append(pair)
       releases =[]
       for sub_folder in sub_folders:
            releases.append(sub_folder.replace(folder_path,"").replace("\\","").replace("/",""))
       releases =  sorted(releases)
       update_pairs = []
       for f1,f2 in pairs:
           subf1 = [f.path for f in os.scandir(f1) if f.is_dir()]
           subf2 = [f.path for f in os.scandir(f2) if f.is_dir()]
           if len(subf1) ==1 and len(subf2)==1:
               update_pairs.append([subf1[0],subf2[0]])
       if update_pairs==[]:
            update_pairs = pairs
       else:
           print("update pairs",update_pairs)
       return releases, update_pairs
   except FileNotFoundError as e:
       print(f"Error {e}: '{folder_path}' is not a valid folder path")
       return None, None


#prints to console and write to a file
def printLog(text,flag,out):
    if flag: 
        print(text,file=out)
        print(text)