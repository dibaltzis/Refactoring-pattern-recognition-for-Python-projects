from util.name_and_path_creator_utility import printLog
from util.html_excel_creator_utility import create_excel_output,create_html_tree
from pathlib import Path
#SimplifyingMethodCalls
from Refactors.SimplifyingMethodCalls.RenameVariable import RenameVariable
from Refactors.SimplifyingMethodCalls.AddRemoveParameter import AddRemoveParameter
from Refactors.SimplifyingMethodCalls.PreserveWholeObject import PreserveWholeObject
from Refactors.SimplifyingMethodCalls.IntroduceParameterObject import IntroduceParameterObject
from Refactors.SimplifyingMethodCalls.RemoveSettingMethod import RemoveSettingMethod
from Refactors.SimplifyingMethodCalls.HideMethod import HideMethod
from Refactors.SimplifyingMethodCalls.ReplaceErrorCodeWithException import ReplaceErrorCodeWithException
from Refactors.SimplifyingMethodCalls.ReplaceExceptionWithTest import ReplaceExceptionWithTest
#MovingFeaturesBetweenObjects
from Refactors.MovingFeaturesBetweenObjects.MoveMethod import MoveMethod
from Refactors.MovingFeaturesBetweenObjects.ExtractClass import ExtractClass
from Refactors.MovingFeaturesBetweenObjects.InlineClass import InlineClass
from Refactors.MovingFeaturesBetweenObjects.MoveField import MoveField
#OrganizingData
from Refactors.OrganizingData.ReplaceArrayWithObject import ReplaceArrayWithObject
from Refactors.OrganizingData.ReplaceMagicNumberWithSymbolicConstant import ReplaceMagicNumberWithSymbolicConstant
from Refactors.OrganizingData.EncapsulatedCollection import EncapsulatedCollection
from Refactors.OrganizingData.EncapsulatedField import EncapsulatedField
#DealingWithGeneralizations
from Refactors.DealingWithGeneralizations.PullUpField import PullUpField
from Refactors.DealingWithGeneralizations.PushDownField import PushDownField
from Refactors.DealingWithGeneralizations.PullUpMethod import PullUpMethod
from Refactors.DealingWithGeneralizations.PushDownMethod import PushDownMethod
from Refactors.DealingWithGeneralizations.PullUpConstructorBody import PullUpConstructorBody
from Refactors.DealingWithGeneralizations.ExtractSubclass import ExtractSubclass
from Refactors.DealingWithGeneralizations.ExtractSuperclass import ExtractSuperclass
from Refactors.DealingWithGeneralizations.CollapseHierarchy import CollapseHierarchy

def CheckForRefactors(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes,deleted_classes):
    rfs=[]
    rfs.extend(AddRemoveParameter(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(RenameVariable(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PreserveWholeObject(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(IntroduceParameterObject(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(RemoveSettingMethod(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(HideMethod(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(ReplaceErrorCodeWithException(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(ReplaceExceptionWithTest(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(MoveMethod(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(ExtractClass(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(InlineClass(version1_name,version2_name,block,file1,file2,name_1,name_2,deleted_classes,introduced_classes))
    rfs.extend(MoveField(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(ReplaceArrayWithObject(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(ReplaceMagicNumberWithSymbolicConstant(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(EncapsulatedCollection(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(EncapsulatedField(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PullUpField(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PushDownField(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PullUpMethod(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PushDownMethod(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(PullUpConstructorBody(version1_name,version2_name,block,file1,file2,name_1,name_2))
    rfs.extend(ExtractSubclass(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(ExtractSuperclass(version1_name,version2_name,block,file1,file2,name_1,name_2,introduced_classes))
    rfs.extend(CollapseHierarchy(version1_name,version2_name,block,file1,file2,name_1,name_2,deleted_classes))
    return  rfs

def print_the_summary_of_the_refactors(refactors,bool_print,out):
    categories = [
    ("Simplifying Method Calls", [
        ("Add/Remove Parameter", get_number_of_refactors_per_name(refactors, "Add/Remove Parameter")),
        ("Rename Variable", get_number_of_refactors_per_name(refactors, "Rename Variable")),
        ("Preserve Whole Object", get_number_of_refactors_per_name(refactors, "Preserve Whole Object")),
        ("Introduce Parameter Object", get_number_of_refactors_per_name(refactors, "Introduce Parameter Object")),
        ("Remove Setting Method", get_number_of_refactors_per_name(refactors, "Remove Setting Method")),
        ("Hide Method", get_number_of_refactors_per_name(refactors, "Hide Method")),
        ("Replace ErrorCode With Exception", get_number_of_refactors_per_name(refactors, "Replace ErrorCode With Exception")),
        ("Replace Exception With Test", get_number_of_refactors_per_name(refactors, "Replace Exception With Test")),
    ]),
    ("Moving Features between Objects", [
        ("Move Method", get_number_of_refactors_per_name(refactors, "Move Method")),
        ("Extract Class", get_number_of_refactors_per_name(refactors, "Extract Class")),
        ("Inline Class", get_number_of_refactors_per_name(refactors, "Inline Class")),
        ("Move Field", get_number_of_refactors_per_name(refactors, "Move Field")),
    ]),
    ("Organizing Data", [
        ("Replace Array With Object", get_number_of_refactors_per_name(refactors, "Replace Array With Object")),
        ("Replace Magic Number With Symbolic Constant", get_number_of_refactors_per_name(refactors, "Replace Magic Number With Symbolic Constant")),
        ("Encapsulated Collection", get_number_of_refactors_per_name(refactors, "Encapsulated Collection")),
        ("Encapsulated Field", get_number_of_refactors_per_name(refactors, "Encapsulated Field")),
    ]),
    ("Dealing with Generalizations", [
        ("Pull Up Field", get_number_of_refactors_per_name(refactors, "Pull Up Field")),
        ("Push Down Field", get_number_of_refactors_per_name(refactors, "Push Down Field")),
        ("Pull Up Method", get_number_of_refactors_per_name(refactors, "Pull Up Method")),
        ("Push Down Method", get_number_of_refactors_per_name(refactors, "Push Down Method")),
        ("Pull Up Constructor Body", get_number_of_refactors_per_name(refactors, "Pull Up Constructor Body")),
        ("Extract Subclass", get_number_of_refactors_per_name(refactors, "Extract Subclass")),
        ("Extract Superclass", get_number_of_refactors_per_name(refactors, "Extract Superclass")),
        ("Collapse Hierarchy", get_number_of_refactors_per_name(refactors, "Collapse Hierarchy")),
    ]),
    ]
    printLog("---------------------------------------------",bool_print,out)
    printLog("             Found "+str(len(refactors))+" Refactors.",bool_print,out)
    printLog("---------------------------------------------",bool_print,out)
    for category, subcategories in categories:
        printLog(category,bool_print, out)
        for subcategory, count in subcategories:
            printLog("\t"+subcategory +" : "+ str(count),bool_print, out)
    printLog("---------------------------------------------",bool_print,out)

    table_string ="<h2>Total <span style='color: #ffffff'>" + str(len(refactors)) + "</span> refactors has been found</h2>\n"
    table_string += '<table class="Mytable">\n'
    table_string += "<thead>\n"
    table_string += "    <tr>\n"
    table_string += "        <th>Category</th>\n"
    table_string += "        <th>Refactor</th>\n"
    table_string += "        <th>Total</th>\n"
    table_string += "        <th>Refactor location list</th>\n"
    table_string += "    </tr>\n"
    table_string += "</thead>\n<tbody>\n"

    for category, subcategories in categories:
        table_string += "    <tr>\n"
        table_string += f"        <td>{category}</td>\n"
        table_string += "    </tr>\n"

        for subcategory, count in subcategories:
            table_string += "    <tr>\n"
            table_string += "        <td></td>\n"
            table_string += f"        <td>{subcategory}</td>\n"
            table_string += f'        <td style="text-align: center;">{count}</td>\n'
            table_string += f'{links_per_refactor(refactors,subcategory)}'
            table_string += "    </tr>\n"
    
    table_string += "</tbody>\n</table>"
    return table_string

def links_per_refactor(refactors,subcategory):
    string_="<td>"
    c=1 
    for r in refactors:
        if r.name == subcategory:
            html = Path("html_files") / Path(r.name.replace(" ","_").replace("/","_")+"_id_"+str(id(r))+".html")
            string_+="<a href='"+str(html)+"'target='_blank'"+">"+str(c)+"\n</a>&ensp;"
            c+=1
    string_+="</td>\n"
    return string_
    

def get_number_of_refactors_per_name(refactors,name):
    count =0
    for ref in refactors:
        if ref.name == name:
            count+=1
    return count


def create_and_print_summary(refactors,export_folder_path,bool_print,out,directory1=None,directory2=None,project_name_folder=None,releases=None):
    if len(refactors)>0:
        create_excel_output(refactors,export_folder_path,project_name_folder)
        refactors_html_table = print_the_summary_of_the_refactors(refactors,bool_print,out)
        create_html_tree(export_folder_path,refactors_html_table,directory1,directory2,project_name_folder,releases)
        printLog("Output folder :",bool_print,out)
        printLog("Results/",bool_print,out)
        printLog(f"└──{project_name_folder if project_name_folder!=None else ('['+directory1.name+']['+directory2.name+']/')}",bool_print,out)
        printLog("   ├──html_files/",bool_print,out)
        printLog("   │  ├──RefactorName_id_numbers.html",bool_print,out)
        printLog("   │  └──...",bool_print,out)
        printLog("   ├──Execution.txt",bool_print,out)
        printLog(f"   ├──{'['+project_name_folder+']' if project_name_folder!=None else ''}Refactors_tree.html",bool_print,out)
        printLog(f"   └──{'['+project_name_folder+']' if project_name_folder!=None else ''}Refactors.xlsx",bool_print,out)
    else:
        printLog("No refactors found.",bool_print,out)
    printLog("---------------------------------------------",bool_print,out)