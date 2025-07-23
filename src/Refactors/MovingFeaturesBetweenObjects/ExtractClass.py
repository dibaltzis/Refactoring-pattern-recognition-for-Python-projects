from Refactor import Refactor
from util.refactors_utility import get_class_obj_by_name,find_common_attributes
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_attributes_of__init__function_of_a_class
from util.refactors_utility import class_belongs_to_deleted_or_introduced_class

def ExtractClass(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,introduced_classes):
    """
    Extracts classes from the given block and compares them to the introduced classes.
    If a match is found, the attributes of the __init__ function of the class in file2 are checked against the attributes of the __init__ function of all the classes with different name in file1.
    If the attributes of file's 2 class __init__ function match with the attributes of file's 1 class __init__ function, a refactor is added to the refactors list.
    
    Args:
        block (Block): The block containing the lines to extract classes from.
        file1 (File): The first file object.
        file2 (File): The second file object.
        file_name_1 (str): The name of the first file.
        file_name_2 (str): The name of the second file.
        introduced_classes (list): A list of introduced classes.
    
    Returns:
        list: A list of refactors.
    """
    refactors=[]
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f2_line, "Class"): 
                if len(introduced_classes)>0:
                    for introduced_class_name,introduced_class_path in introduced_classes:
                        if class_belongs_to_deleted_or_introduced_class(f2_line.line_type,file2.file_path,introduced_class_name,introduced_class_path):
                            if f2_line.line_type.superclass_name == None:
                                f2b_class_obj= f2_line
                                f2b_init_function_object,f2b_class_atr = get_attributes_of__init__function_of_a_class(f2_line.line_type,file2)
                                if f2b_init_function_object is not None:
                                    f2b_class_atr = [f2Batr.line_type.variable_name for f2Batr in f2b_class_atr]
                                    for line_f1 in file1.Lines:
                                        if line_f1.line_type.name == "Class": 
                                            f2a_class_obj= get_class_obj_by_name(line_f1.line_type.name_of_the_class,file2)
                                            if  f2a_class_obj!= None:
                                                f1a_class_obj = line_f1
                                                f1a_init_function_object,f1a_class_atr = get_attributes_of__init__function_of_a_class(line_f1.line_type,file1)
                                                if f1a_init_function_object is not None:
                                                    f1a_class_atr = [f1Aatr.line_type.variable_name for f1Aatr in f1a_class_atr]
                                                    common_attributes_of_f2b_f1a = find_common_attributes(f1a_class_atr, f2b_class_atr)
                                                    if common_attributes_of_f2b_f1a!=[]:
                                                        f2a_init_function_object,f2a_class_atr = get_attributes_of__init__function_of_a_class(f2a_class_obj.line_type,file2)
                                                        if f2a_init_function_object is not None:
                                                            f2a_class_atr = [f2Aatr.line_type.variable_name for f2Aatr in f2a_class_atr]
                                                            if not any(item in f2a_class_atr for item in common_attributes_of_f2b_f1a):
                                                                extra_information =f"The introduced class of file2 is '{f2b_class_obj.line_type.name_of_the_class}'"
                                                                extra_information+=f"\nfile1 class '{f1a_class_obj.line_type.name_of_the_class}' attributes: [{ ', '.join(f1a_class_atr) }]"
                                                                extra_information+=f"\nfile2 class '{f2a_class_obj.line_type.name_of_the_class}' attributes: [{ ', '.join(f2a_class_atr) }]"
                                                                extra_information+=f"\nfile2 class '{f2b_class_obj.line_type.name_of_the_class}' attributes: [{ ', '.join(f2b_class_atr) }]"
                                                                extra_information+=f"\n[{', '.join(common_attributes_of_f2b_f1a)}] deleted from class '{f1a_class_obj.line_type.name_of_the_class}' and introduced to class '{f2b_class_obj.line_type.name_of_the_class}'"
                                                                refactors.append(Refactor("Extract Class",
                                                                file_name_1,
                                                                file_name_2,
                                                                version1_name,
                                                                version2_name, 
                                                                f1a_init_function_object.start_index_of_the_declaration,
                                                                f1a_init_function_object.end_index_of_function_content,
                                                                f2b_class_obj.line_number,
                                                                f2b_class_obj.line_type.class_content_end_line,
                                                                "#ff2052",
                                                                "Moving Features between Objects",
                                                                extra_information
                                                                
                                                            ))
                                
    return refactors



"""
print(find_common_attributes(f1_class_atr, f2_class_atr))
                                                            if any(item in f1_class_atr for item in f2_class_atr):
                                                                flag = True
                                                            else:
                                                                f2_class_atr=[item.replace("self.","self."+f2_line.line_type.name_of_the_class.lower()+"_") for item in f2_class_atr]
                                                                if all(item in f1_class_atr for item in f2_class_atr):
                                                                    flag = True
                                                            if flag:
                                                                refactors.append(Refactor("Extract Class",
                                                                    file_name_1,
                                                                    file_name_2,
                                                                    version1_name,
                                                                    version2_name, 
                                                                    f1_init_function_object.start_index_of_the_declaration,
                                                                    f1_init_function_object.end_index_of_function_content,
                                                                    f2_line.line_number,
                                                                    f2_line.line_type.class_content_end_line,
                                                                    "#ff2052",
                                                                    "Moving Features between Objects"
                                                                ))


"""