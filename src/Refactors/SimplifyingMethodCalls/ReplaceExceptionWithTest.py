from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def ReplaceExceptionWithTest(version1_name, version2_name, block, file1, file2, file_name_1, file_name_2):
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Exception"):
            if not_blank_and_line_type_is_equal_to(f2_line, "Conditional"):
                if f1_line.line_type.start_index_of_except is not None and f1_line.line_type.end_index_of_except is not None:
                    start_index = f1_line.line_type.start_index_of_except
                    end_index = f1_line.line_type.end_index_of_except
                    if end_index < len(file1.code_list) - 1:
                        except_content = "\n".join(file1.code_list[start_index + 1:end_index + 1]).strip()
                    else:
                        except_content = "\n".join(file1.code_list[start_index + 1:]).strip()
                    if f2_line.code.strip().startswith("if "):
                        start_index = f2_line.line_type.if_content_start_index
                        end_index = f2_line.line_type.if_content_end_index
                        if end_index < len(file2.code_list) - 1:
                            if_content = "\n".join(file2.code_list[start_index:end_index + 1]).strip()
                        else:
                            if_content = file2.code_list[start_index:].strip()
                        if except_content == if_content:
                            refactors.append(Refactor("Replace Exception With Test",
                                                     file_name_1,
                                                     file_name_2,
                                                     version1_name,
                                                     version2_name,
                                                     f1_line.line_type.start_index_of_exception,
                                                     f1_line.line_type.end_index_of_exception,
                                                     f2_line.line_type.start_index_of_if_expression,
                                                     f2_line.line_type.if_content_end_index,
                                                     "#ff3300",
                                                     "Simplifying Method Calls"
                                                    ))
    return refactors
    