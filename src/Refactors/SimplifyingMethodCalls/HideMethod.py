from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import partOfClass

def HideMethod(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    """
    HideMethod is a function that takes in several parameters: `block`, `file1`, `file2`, `file_name_1`, and `file_name_2`.
    It iterates through the lines in `block.f1_lines_list` and `block.f2_lines_list` simultaneously using the `zip` function.
    For each pair of lines, it checks if the `f1_line` is not empty and is a function declaration.
    If it is, it further checks if it is part of a class in the `file1`.
    If the `f2_line` is not empty and is also a function declaration, it checks if the function names of `f1_line` and `f2_line` are different. 
    If they are different and `f2_line`'s function name starts with `__`(which mean that the method is private in python) and is the same as `f1_line`'s function name, it appends a `Refactor` object to the `refactors` list.

    The function then returns the `refactors` list.
    """
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Function"):
            if partOfClass(f1_line,file1)[0]:
                if not_blank_and_line_type_is_equal_to(f2_line, "Function"):
                    if f1_line.line_type.function_name != f2_line.line_type.function_name:
                        if f2_line.line_type.function_name =="__"+f1_line.line_type.function_name:
                                   refactors.append(Refactor("Hide Method",
                                                            file_name_1,
                                                            file_name_2,
                                                            version1_name,
                                                            version2_name, 
                                                            f1_line.line_type.start_index_of_the_declaration,
                                                            f1_line.line_type.end_index_of_the_declaration,
                                                            f2_line.line_type.start_index_of_the_declaration,
                                                            f2_line.line_type.end_index_of_the_declaration,
                                                            "#ffffbf",
                                                            "Simplifying Method Calls"
                                   ))
    return refactors


                    
