from Refactor import Refactor
from util.refactors_utility import partOfClass
from util.refactors_utility import get_subclasses_from_superclass
from util.refactors_utility import if_line_is_in_class,get_method_from_a_class
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_class_obj_by_name

def PullUpMethod(version1_name,version2_name,block,file1,file2,name_1,name_2):
    refactors=[]
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f2_line, "Function"):
                if f2_line.line_type.function_name != "__init__" :
                    check_if_method_does_not_exist_in_subclasses = False
                    if_part_of_class,class_obj_f2 = partOfClass(f2_line,file2)
                    if if_part_of_class:
                        if class_obj_f2.line_type.superclass_name == None:
                            subclasses_f2 = get_subclasses_from_superclass(class_obj_f2.line_type.name_of_the_class,file2)
                            if all(False == if_line_is_in_class(f2_line,sub,file2) for sub in subclasses_f2):
                                check_if_method_does_not_exist_in_subclasses= True
                    if check_if_method_does_not_exist_in_subclasses:
                            class_obj_f1  = get_class_obj_by_name(class_obj_f2.line_type.name_of_the_class,file1)
                            if class_obj_f1:
                                if not if_line_is_in_class(f2_line,class_obj_f1,file1):
                                    subclasses_f1 = get_subclasses_from_superclass(class_obj_f2.line_type.name_of_the_class,file1)
                                    if any(if_line_is_in_class(f2_line,sub,file1) for sub in subclasses_f1):
                                        for sub in subclasses_f1:
                                            method=get_method_from_a_class(f2_line.line_type.function_name,sub,file1)
                                            if method!= None:
                                                refactors.append(Refactor("Pull Up Method",
                                                                        name_1,
                                                                        name_2,
                                                                        version1_name,
                                                                        version2_name, 
                                                                        method.line_type.start_index_of_the_declaration,
                                                                        method.line_type.end_index_of_function_content,
                                                                        f2_line.line_type.start_index_of_the_declaration,
                                                                        f2_line.line_type.end_index_of_function_content,
                                                                        "#ffccff",
                                                                        "Dealing with Generalizations"
                                                ))
                                                break

                        

            
            
            
            
    return refactors
