from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def IntroduceParameterObject(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,introduced_classes):
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
            if not_blank_and_line_type_is_equal_to(f2_line, "Function"):
                if f1_line.line_type.function_name == f2_line.line_type.function_name:
                    if set(f1_line.line_type.function_parameters) != set(f2_line.line_type.function_parameters):
                        if len(f2_line.line_type.function_parameters) < len(f1_line.line_type.function_parameters) and len(f2_line.line_type.function_parameters)==1:
                            if f2_line.line_type.function_parameters[0] not in f1_line.line_type.function_parameters:
                                for introduced_class_name,_ in introduced_classes:
                                    if f2_line.line_type.function_parameters[0] == introduced_class_name:
                                        refactors.append(Refactor("Introduce Parameter Object",
                                                file_name_1,
                                                file_name_2,
                                                version1_name,
                                                version2_name, 
                                                f1_line.line_number,
                                                f1_line.line_number,
                                                f2_line.line_number,
                                                f2_line.line_number+1,
                                                "#ffff00",
                                                "Simplifying Method Calls"
                                        ))
    return refactors