from Refactor import Refactor
from util.refactors_utility import if_class_is_sub_super_class_of_the_other
from util.refactors_utility import get_class_obj_by_name,compare_classes
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_attributes_of__init__function_of_a_class

def MoveField(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors  = []
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Class"):
                f1a_class_obj = f1_line
                f1a_init_function_object,f1a_class_atr = get_attributes_of__init__function_of_a_class(f1a_class_obj.line_type,file1)
                if f1a_init_function_object is not None:
                    common_atr1 = None
                    common_atr2 = None
                    if len(f1a_class_atr) >0:
                        f2a_class_obj =get_class_obj_by_name(f1_line.line_type.name_of_the_class,file2)
                        if f2a_class_obj != None:
                            f2a_init_function_object,f2a_class_atr = get_attributes_of__init__function_of_a_class(f2a_class_obj.line_type,file2)
                            if f2a_init_function_object is not None:
                                if len(f2a_class_atr)>0:
                                    not_common_atr = [atr for atr in f1a_class_atr if atr.line_type.variable_name not in [f2_atr.line_type.variable_name for f2_atr in f2a_class_atr]]
                                    if len(not_common_atr)>0:    
                                        for line_f2 in file2.Lines:
                                            if line_f2.line_type.name == "Class":
                                                f2b_class_obj = line_f2                               
                                                if not compare_classes(f2a_class_obj,f2b_class_obj,file2,file2):
                                                    if not if_class_is_sub_super_class_of_the_other(f2a_class_obj,f2b_class_obj):
                                                        f2b_init_function_object,f2b_class_atr = get_attributes_of__init__function_of_a_class(f2b_class_obj.line_type,file2)
                                                        if f2b_init_function_object is not None:
                                                            if len(f2b_class_atr)>0:
                                                                common_atr =[atr for atr in not_common_atr if atr.line_type.variable_name  in [f2_atr.line_type.variable_name for f2_atr in f2b_class_atr]]
                                                                if len(common_atr)>0:
                                                                    if all(c_atr.line_type.variable_name == not_c_atr.line_type.variable_name for c_atr in common_atr for not_c_atr in not_common_atr):
                                                                        common_atr1 = common_atr[0]
                                                                        common_atr2 = next((atr for atr in f2b_class_atr if atr.line_type.variable_name == common_atr1.line_type.variable_name), None)
                                                                        f1b_class_obj = get_class_obj_by_name(f2b_class_obj.line_type.name_of_the_class,file1)
                                                                        if f1b_class_obj:
                                                                            f1b_init_function_object,f1b_class_atr = get_attributes_of__init__function_of_a_class(f1b_class_obj.line_type,file1)
                                                                            if f1b_init_function_object is not None:
                                                                                if not any(common_atr2.line_type.variable_name == f1B_atr.line_type.variable_name for f1B_atr in f1b_class_atr):
                                                                                    refactors.append(Refactor("Move Field",
                                                                                                            file_name_1,
                                                                                                            file_name_2,
                                                                                                            version1_name,
                                                                                                            version2_name, 
                                                                                                            common_atr1.line_type.start_index_of_declaration,
                                                                                                            common_atr1.line_type.end_index_of_declaration,
                                                                                                            common_atr2.line_type.start_index_of_declaration,
                                                                                                            common_atr2.line_type.end_index_of_declaration,
                                                                                                            "#669999",
                                                                                                            "Moving Features between Objects"
                                                                                                            ))
                                                                                    break

                                                                                        

                                                    
    return refactors
