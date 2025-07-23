from Refactor import Refactor
from util.refactors_utility import Get_all_methods_from_a_class
from util.refactors_utility import get_class_obj_by_name,compare_classes
from util.refactors_utility import find_common_attributes
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_attributes_of__init__function_of_a_class

def InlineClass(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,deleted_classes,introduced_classes):
    refactors = []
    for f1l in  block.f1_lines_list:    
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Class"):
            f1b_class_obj = f1_line
            if any((f1_line.line_type.name_of_the_class == deleted_class_name and file_name_1 in deleted_class_path) for deleted_class_name,deleted_class_path in deleted_classes): 
                same_class_renamed= False
                if len(introduced_classes) > 0:
                    for introduced_class_name, introduced_class_path in introduced_classes:
                        if file_name_2 in introduced_class_path:
                            introduced_class = get_class_obj_by_name(introduced_class_name, file2)
                            if compare_classes(f1b_class_obj,introduced_class,file1,file2):
                                same_class_renamed = True
                if not same_class_renamed:
                    f1b_init_object,f1b_class_atrs = get_attributes_of__init__function_of_a_class(f1b_class_obj.line_type,file1)
                    f1b_class_atrs= [atr.line_type.variable_name for atr in f1b_class_atrs]
                    for line_f2 in file2.Lines:
                        if line_f2.line_type.name == "Class":
                            f2a_class_obj = line_f2
                            f2a_init_object,f2a_class_atrs = get_attributes_of__init__function_of_a_class(f2a_class_obj.line_type,file2)
                            f2a_class_atrs= [atr.line_type.variable_name for atr in f2a_class_atrs]
                            if f1b_init_object is not None and f2a_init_object is not None:
                                if all(f1B_atr in f2a_class_atrs for f1B_atr in f1b_class_atrs):
                                    common_attr = find_common_attributes(f1b_class_atrs,f2a_class_atrs)
                                    f1b_class_methods = Get_all_methods_from_a_class(f1b_class_obj.line_type,file1)
                                    f2a_class_methods = Get_all_methods_from_a_class(f2a_class_obj.line_type,file2)
                                    if all(f1B_method.function_name == f2A_method.function_name for f1B_method in f1b_class_methods for f2A_method in f2a_class_methods):
                                        f1a_class_obj =  get_class_obj_by_name(f2a_class_obj.line_type.name_of_the_class,file1)
                                        if f1a_class_obj:
                                            f1a_init_object,f1a_class_atrs = get_attributes_of__init__function_of_a_class(f1a_class_obj.line_type,file1)
                                            f1a_class_atrs= [atr.line_type.variable_name for atr in f1a_class_atrs]
                                            if f1a_init_object is not None:
                                                if not all(f1A_atr == common for f1A_atr in f1a_class_atrs for common in common_attr):
                                                    
                                                    #f1A_class_methods = Get_all_methods_from_a_class(f1A_class_obj.line_type,file1)
                                                    #if not any(f1B_method.function_name == f1A_method.function_name for f1A_method in f1A_class_methods for f1B_method in f1B_class_methods):
                                                    refactors.append(Refactor("Inline Class",
                                                                            file_name_1,
                                                                            file_name_2,
                                                                            version1_name,
                                                                            version2_name, 
                                                                            f1b_class_obj.line_number,
                                                                            f1b_class_obj.line_type.class_content_end_line,
                                                                            f2a_class_obj.line_number,
                                                                            f2a_class_obj.line_type.class_content_end_line,
                                                                            "#0095bf",
                                                                            "Moving Features between Objects"
                                                ))

    return refactors
