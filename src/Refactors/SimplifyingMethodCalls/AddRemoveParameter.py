from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def AddRemoveParameter(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
            if not_blank_and_line_type_is_equal_to(f2_line, "Function"):
                    if f1_line.line_type.function_name == f2_line.line_type.function_name:
                        if set(f1_line.line_type.function_parameters) != set(f2_line.line_type.function_parameters):
                            refactors.append(Refactor("Add/Remove Parameter",
                                                                file_name_1,
                                                                file_name_2,
                                                                version1_name,
                                                                version2_name,
                                                                f1_line.line_type.start_index_of_the_declaration,
                                                                f1_line.line_type.start_index_of_function_content-1,
                                                                f2_line.line_type.start_index_of_the_declaration,
                                                                f2_line.line_type.start_index_of_function_content-1,
                                                                "#007744",
                                                                "Simplifying Method Calls"
                                                                ))

    return refactors