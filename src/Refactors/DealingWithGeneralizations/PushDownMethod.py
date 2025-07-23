from Refactor import Refactor
from util.refactors_utility import partOfClass,get_subclasses_from_superclass
from util.refactors_utility import if_line_is_in_class
from util.refactors_utility import get_method_from_a_class
from util.refactors_utility import get_class_obj_by_name
from util.refactors_utility import not_blank_and_line_type_is_equal_to


def PushDownMethod(version1_name,version2_name,block,file1,file2,name_1,name_2):
    refactors =[]
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
                if f1_line.line_type.function_name != "__init__" :
                    check_if_method_does_not_exist_in_subclasses = False
                    if_part_of_class,class_obj_f1 = partOfClass(f1_line,file1)
                    if if_part_of_class:
                        if class_obj_f1.line_type.superclass_name == None:
                            subclasses_f1 = get_subclasses_from_superclass(class_obj_f1.line_type.name_of_the_class,file1)
                            if all(False == if_line_is_in_class(f1_line,sub,file1) for sub in subclasses_f1):
                                check_if_method_does_not_exist_in_subclasses= True
                    if check_if_method_does_not_exist_in_subclasses:
                        if get_class_obj_by_name(class_obj_f1.line_type.name_of_the_class,file2) is not None:
                            class_obj_f2  = get_class_obj_by_name(class_obj_f1.line_type.name_of_the_class,file1)
                            if class_obj_f2:
                                if not if_line_is_in_class(f1_line,class_obj_f2,file2):
                                    subclasses_f2 = get_subclasses_from_superclass(class_obj_f1.line_type.name_of_the_class,file2)
                                    if any(if_line_is_in_class(f1_line,sub,file2) for sub in subclasses_f2):
                                        for sub in subclasses_f2:
                                            method=get_method_from_a_class(f1_line.line_type.function_name,sub,file2)
                                            if method!= None:
                                                refactors.append(Refactor("Push Down Method",
                                                                        name_1,
                                                                        name_2,
                                                                        version1_name,
                                                                        version2_name, 
                                                                        f1_line.line_type.start_index_of_the_declaration,
                                                                        f1_line.line_type.end_index_of_function_content,
                                                                        method.line_type.start_index_of_the_declaration,
                                                                        method.line_type.end_index_of_function_content,
                                                                        "#9900ff",
                                                                        "Dealing With Generalizations",
                                                ))
                                                break
                                
                                
                                
    return refactors        