from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import partOfClass,get_class_obj_by_name
from util.refactors_utility import Get_all_methods_from_a_class
from util.refactors_utility import if_class_is_sub_super_class_of_the_other
from util.refactors_utility import compare_classes
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def MoveMethod(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors = []
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
                if not f1_line.line_type.function_name.strip().startswith("__init__"):
                    part_of_class_bool1 , class_obj1 = partOfClass(f1_line,file1)
                    if part_of_class_bool1:
                        number_of_lines_of_function_from_file1 = f1_line.line_type.end_index_of_function_content - f1_line.line_type.start_index_of_the_declaration
                        class_obj2 = get_class_obj_by_name(class_obj1.line_type.name_of_the_class,file2)
                        if class_obj2 != None:
                            methods_of_the_same_class = Get_all_methods_from_a_class(class_obj2.line_type,file2)
                            if methods_of_the_same_class!=[]:
                                if not any((f1_line.line_type.function_name == f2_method.function_name) and \
                                       (set(f1_line.line_type.function_parameters) == set(f2_method.function_parameters)) for f2_method in methods_of_the_same_class):
                                    for line_f2 in file2.Lines:
                                        if line_f2.line_type.name == "Function":
                                            if f1_line.line_type.function_name == line_f2.line_type.function_name:
                                                if set(f1_line.line_type.function_parameters) == set(line_f2.line_type.function_parameters):
                                                    number_of_lines_of_function_from_file2 = line_f2.line_type.end_index_of_function_content - line_f2.line_type.start_index_of_the_declaration
                                                    if number_of_lines_of_function_from_file1==number_of_lines_of_function_from_file2:
                                                        part_of_class_bool2, class_obj2 = partOfClass(line_f2,file2)
                                                        if part_of_class_bool2:
                                                            if class_obj1.line_type.name_of_the_class != class_obj2.line_type.name_of_the_class:
                                                                if not if_class_is_sub_super_class_of_the_other(class_obj1,class_obj2):
                                                                    class_obj1_from_file2 = get_class_obj_by_name(class_obj2.line_type.name_of_the_class,file1)
                                                                    if class_obj1_from_file2!= None:
                                                                        methods_of_the_same_class_1 = Get_all_methods_from_a_class(class_obj1_from_file2.line_type,file1)
                                                                        if not any((line_f2.line_type.function_name == method.function_name) and \
                                                                                    (set(line_f2.line_type.function_parameters) == set(method.function_parameters)) for method in methods_of_the_same_class_1):
                                                                            if not compare_classes(class_obj1,class_obj2,file1,file2):
                                                                                refactors.append(Refactor("Move Method",
                                                                                                            file_name_1,
                                                                                                            file_name_2,
                                                                                                            version1_name,
                                                                                                            version2_name, 
                                                                                                            f1_line.line_type.start_index_of_the_declaration,
                                                                                                            f1_line.line_type.end_index_of_function_content,
                                                                                                            line_f2.line_type.start_index_of_the_declaration,
                                                                                                            line_f2.line_type.end_index_of_function_content,
                                                                                                            "#000066",
                                                                                                            "Moving Features between Objects"
                                                                                ))
                                                                                break
    return refactors

 