import difflib
from bs4 import BeautifulSoup
from filecmp import dircmp
import os
from pathlib import Path
from DiffBlock import *
from File import File
from thefuzz import fuzz

#Compares two folders and finds comparable files
def get_comparable_files(directory1,directory2):
    comparable_files=[]
    #Source :https://docs.python.org/3/library/filecmp.html
    def get_diff_files(dcmp):
        for name in dcmp.diff_files:
            if name.endswith(".py"):
                #comparable_files.append([str(dcmp.left)+"/"+str(name),str(dcmp.right)+"/"+str(name)])
                comparable_files.append([str(Path(str(dcmp.left)) / str(name) ),str(Path(str(dcmp.right)) / str(name))])
        for sub_dcmp in dcmp.subdirs.values():
            get_diff_files(sub_dcmp)
        return comparable_files
    dcmp = dircmp(directory1, directory2)
    return get_diff_files(dcmp)    



#creates a diff-block objects list for both versions of a file   
def getBlocks(file1,file2):
    #read file1 and file2
    f1 = open(file1.file_path,"r", encoding='utf-8',errors="ignore").readlines()
    f2 = open(file2.file_path,"r", encoding='utf-8',errors="ignore").readlines()
    #difflib library, finds the difference between the two files
    difference = difflib.HtmlDiff()
    #creates an html file with all the diffs it found
    #.make_file() is a method of  the difflib library that returns a string in html format with the differences of the 2 files
    html = difference.make_file(fromlines=f1, tolines=f2,context=True,fromdesc=file1.file_path, todesc=file2.file_path)
    #f = open("results/"+file1.file_path.replace("\\","_")+"_diff.html","w")
    #f.write(html)
    #f.close()
    #BeautifulSoup library to parse the html file
    soup = BeautifulSoup(html, 'html.parser')
    blocks=[]
    #searching in html file for the diff blocks by the tag 'tbody'
    for t in soup.select('tbody '):
        lines=[]
        #search  for the tag 'tr'
        for tr in t.select('tr'):
            line=[]
            #search for the tag 'td'
            for td in tr.select("td"):
                type_ = None
                if '<span class="diff_sub">' in str(td):
                    type_= "Sub"
                if '<span class="diff_add">' in str(td):
                    type_ = "Add"
                line.append([td.text.replace("\xa0",""),type_])
            lines.append(line)
        blocks.append(lines)
    #at this point blocks is a list of strings with all the differences of the two files
    #list of DiffBlock objects
    diffBlocks = []
    for b in blocks:
        #gets two lists with Blockline objects for each block
        #list1 is for all lines+type for the file1
        #list2 is for all lines+type for the file2
        temp = get_atr_from_block(b,file1,file2)
        #creates and append the DiffBlocks
        diffBlocks.append(DiffBlock(temp[0],temp[1]))
    return diffBlocks

#gets two list with Blockline objects for each block
#list1 is for all lines+type for the file1
#list2 is for all lines+type for the file2
def get_atr_from_block(lines,file1,file2):
    f1 =[]
    f2= []
    for l in lines:
        f1l = ''
        f2l = ''
        if l[1][0] != '':
            f1l = file1.Lines[int(l[1][0])-1]
        if l[4][0] != '':
            f2l =file2.Lines[int(l[4][0])-1]
        f1.append(BlockLine(l[2][1],f1l))
        f2.append(BlockLine(l[5][1],f2l))
    return [f1,f2]

def Get_introduced_deleted_classes(comparable_files):
    introduced_classes =[]
    deleted_classes = []
    version1_classes=[]
    version2_classes=[]
    for  index,cf in enumerate(comparable_files):
        file1 = File(cf[0])
        file2 = File(cf[1])
        for f1 in file1.Lines:
            if f1.line_type.name == "Class":
                version1_classes.append([f1.line_type.name_of_the_class,file1.file_path] )
        for f2 in file2.Lines:
            if f2.line_type.name == "Class":
                version2_classes.append([f2.line_type.name_of_the_class,file2.file_path] )
  
    for version2_class_name,version2_class_path in version2_classes:
        flag = False
        for version1_class_name,version1_class_path in version1_classes:
            if fuzz.ratio(version1_class_path,version2_class_path)>95:
                if version1_class_name != version2_class_name:
                    flag=True
                else :
                    flag = False
                    break
        if flag:
            introduced_classes.append([version2_class_name,version2_class_path])
            
    for version1_class_name,version1_class_path in version1_classes:   
        flag =False
        for version2_class_name,version2_class_path in version2_classes:
            if fuzz.ratio(version1_class_path,version2_class_path)>95:
                if version1_class_name != version2_class_name:
                    flag=True 
                else :
                    flag = False
                    break
        if flag:
            deleted_classes.append([version1_class_name,version1_class_path])    
            
    return introduced_classes,deleted_classes        
