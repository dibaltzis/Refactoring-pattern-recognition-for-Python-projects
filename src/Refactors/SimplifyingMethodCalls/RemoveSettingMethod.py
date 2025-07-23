from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import Get_all_methods_from_a_class
from util.refactors_utility import get_class_obj_by_name
from util.refactors_utility import if_function_is_in_class
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def RemoveSettingMethod(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors = []
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
            part_of_class_bool, class1_object = if_function_is_in_class(f1_line.line_type, file1)
            if part_of_class_bool:
                if f1_line.line_type.function_name.startswith("set" or "Set"):
                    f2_class_obj = get_class_obj_by_name(class1_object.name_of_the_class,file2)
                    if f2_class_obj != None:
                        f2_class_methods = Get_all_methods_from_a_class(f2_class_obj.line_type, file2)
                        if not any(f1_line.line_type.function_name == f2_method.function_name for f2_method in f2_class_methods):
                            refactors.append(Refactor("Remove Setting Method",
                                                                file_name_1,
                                                                file_name_2,
                                                                version1_name,
                                                                version2_name, 
                                                                f1_line.line_type.start_index_of_the_declaration,
                                                                f1_line.line_type.end_index_of_function_content,
                                                                f2_class_obj.line_type.class_content_start_line,
                                                                f2_class_obj.line_type.class_content_end_line,
                                                                "#ffff55",
                                                                "Simplifying Method Calls"
                                                                ))
    return refactors

 