import time
import sys
from File import File
from pathlib import Path
from util.name_and_path_creator_utility import create_end_return_export_folder
from util.name_and_path_creator_utility import get_subfolder_pairs,printLog
from util.file_comparison_utility import get_comparable_files
from util.file_comparison_utility import Get_introduced_deleted_classes
from util.file_comparison_utility import getBlocks,Get_introduced_deleted_classes
from util.html_excel_creator_utility import create_html_per_refactor
from util.CheckForRefactors_and_PrintSummary import CheckForRefactors
from util.CheckForRefactors_and_PrintSummary import create_and_print_summary
import concurrent.futures

def get_refactors(directory1,directory2,html_files_folder_path,bool_print,out):#,project_name=None):
    folder_name1 = directory1.name
    folder_name2 = directory2.name
    version1_name = directory1.name
    version2_name = directory2.name
    printLog("Comparing '%s' and '%s' ..." % (folder_name1,folder_name2),bool_print,out)
    #creates a list with all the comparable files
    comparable_files = get_comparable_files(directory1,directory2)
    printLog("Done. Found %d comparable files." % (len(comparable_files)),bool_print,out)
    #main refactor list
    refactors=[]
    printLog("---------------------------------------------",bool_print,out)
    printLog("Searching for refactors...",bool_print,out)
    introduced_classes,deleted_classes = Get_introduced_deleted_classes(comparable_files) 
    #loop within the comparable files
    for  index,cf in enumerate(comparable_files):
        index = index +1
        count=0
        name_1=folder_name1+str(Path(cf[0].split(folder_name1)[1]))
        name_2 =folder_name2+str(Path(cf[0].split(folder_name1)[1]))
        printLog("%d)Comparing '%s' and '%s'" % (index,name_1,name_2),bool_print,out)
        file1 = File(cf[0])
        file2 = File(cf[1])
        
        #gets all diff block for two files
        #uses  difflib library to get a html file
        #then, using the Beautifulsoup library, parses each line for each block
        Diffblocks =getBlocks(file1,file2)
        #----------------------------------------------------------#
        #loop within each block
        for block in Diffblocks:
            rfs=[]
            #checks each block for the specific refactor
            #each function returns a list of refactors
            rfs = CheckForRefactors(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes,deleted_classes)
            #sets the found refactors to each block
            for r in rfs:
                    block.set_refactors(r)
            #append the found refactors to the main refactor list
            for rf in rfs:
                count+=1
                refactors.append(rf)
        #----------------------------------------------------------#
        #checks if more than 1 Refactors have been found and creates the html output for this comparable file
        if count!=0:
            create_html_per_refactor(file1,file2,name_1,name_2,Diffblocks,html_files_folder_path)#,project_name)
    count_comparable_files = len(comparable_files)
    return refactors,count_comparable_files

def process_subfolder_pair(subfolder_pair):
    directory1 = Path(subfolder_pair[0])
    directory2 = Path(subfolder_pair[1])
    version1_name = directory1.name
    version2_name = directory2.name
    refs, count_comparable_files = get_refactors(directory1, directory2, html_files_folder_path, False, out)
    printLog("Done comparing [" + str(version1_name) + "] and [" + str(version2_name) + "]", True, out)
    return refs, count_comparable_files, version1_name, version2_name

if __name__ == '__main__':
    start_time = time.time()
    directory1 = Path('input_folder/test1')
    directory2 = Path('input_folder/test2')
    
    project_name_folder = None
    version1 = None
    version2 = None

    if len(sys.argv) ==2:
        project_name_folder = sys.argv[1]
        project_name = Path(sys.argv[1]).name
        releases, subfolder_pairs = get_subfolder_pairs(project_name_folder)
    elif len(sys.argv) ==3:
        directory1 = Path(sys.argv[1])
        directory2 = Path(sys.argv[2])
    elif len(sys.argv) ==1:
        print("Using the default input")
    else:
        print( "Usage options : \
                \n\t1. python src/main.py (set project folder or version1 and version2 in code) \
                \n\t2. python src/main.py [project_folder] \
                \n\t3. python src/main.py [version1_folder] [version2_folder]" \
            )    
    if len(sys.argv) ==3 or len(sys.argv) ==1:
        version1_name = directory1.name
        version2_name = directory2.name
        export_folder_path,html_files_folder_path=create_end_return_export_folder(version1_name,version2_name) 
        out = open(export_folder_path / 'Execution.txt', 'w',encoding='utf-8')
        refactors, count_comparable_files = get_refactors(directory1,directory2,html_files_folder_path,True,out) 
        create_and_print_summary(refactors,export_folder_path,True,out,directory1,directory2)
    elif len(sys.argv) ==2 and subfolder_pairs:
            export_folder_path,html_files_folder_path=create_end_return_export_folder(project_name)
            out = open(export_folder_path / 'Execution.txt', 'w',encoding='utf-8')
            printLog("Project name: "+str(project_name),True,out)
            printLog("Number of releases: "+str(len(releases)),True,out)
            printLog("Releases: \n"+str(", ".join(releases)),True,out)
            printLog("Total comparisons: "+str(len(subfolder_pairs)),True,out)           
            refactors = []
            total_comparable_files = 0
            n_threads = len(subfolder_pairs)
            with concurrent.futures.ThreadPoolExecutor(n_threads) as executor:    
                results = list(executor.map(process_subfolder_pair, subfolder_pairs))
            for refs, count_comparable_files, version1_name, version2_name in results:
               refactors.extend(refs)
               total_comparable_files += count_comparable_files
                
            printLog("Total comparable files : "+str(total_comparable_files),True,out)
            create_and_print_summary(refactors,export_folder_path,True,out,None,None,project_name,releases)
    if out:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        printLog(f"Execution time: {int(minutes)} minute(s) and {int(seconds):02d} seconds",True,out)     
        out.close()
