from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def ReplaceErrorCodeWithException(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Return"):
            if f2_line !="":
                if f1_line.line_type.content_of_the_return.strip().replace("-","").isnumeric():
                    if f2_line.code.strip().startswith("raise "):
                        refactors.append(Refactor("Replace ErrorCode With Exception",
                                                    file_name_1,
                                                    file_name_2,
                                                    version1_name,
                                                    version2_name, 
                                                    f1_line.line_type.start_index_of_return,
                                                    f1_line.line_type.end_index_of_return,
                                                    f2_line.line_type.index_of_line,
                                                    f2_line.line_type.index_of_line,
                                                    "#ff0000",
                                                    "Simplifying Method Calls"
                                                    ))

    return refactors