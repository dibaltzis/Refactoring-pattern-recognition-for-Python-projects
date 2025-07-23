from thefuzz import fuzz
from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def RenameVariable(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2):
    refactors = []
    #for index,b in enumerate(block.f1_lines_list):
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Declaration"):
            if not_blank_and_line_type_is_equal_to(f2_line, "Declaration"):
                if f1_line.line_type.variable_name != f2_line.line_type.variable_name:
                    if fuzz.ratio(f1_line.line_type.assigned_content, f2_line.line_type.assigned_content) >95:
                        refactors.append(Refactor("Rename Variable",
                            file_name_1,
                            file_name_2,
                            version1_name,
                            version2_name,                                    
                            f1_line.line_type.start_index_of_declaration,
                            f1_line.line_type.end_index_of_declaration,
                            f2_line.line_type.start_index_of_declaration,
                            f2_line.line_type.end_index_of_declaration,
                            "#003300",
                            "Simplifying Method Calls"
                            ))
    return refactors