from Refactor import Refactor
from util.refactors_utility import declaration_exist_in_file
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def ReplaceMagicNumberWithSymbolicConstant(version1_name, version2_name, block, file1, file2, file_name_1, file_name_2):
    refactors = []
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f2_line, "Declaration"):
            if f2_line.line_type.assigned_content.strip().replace(".", "").replace(",", "").isnumeric():
                decl_obj_f1 = declaration_exist_in_file(f2_line.line_type, file1)
                if decl_obj_f1 == False:
                    for line_f2 in file2.Lines:
                        var_name = f2_line.line_type.variable_name
                        numeric_value = f2_line.line_type.assigned_content.strip()
                        not_the_same_line = True
                        if line_f2.line_type.name == "Declaration":
                            if line_f2.line_type.variable_name == var_name:
                                not_the_same_line = False
                            else:
                                not_the_same_line = True
                        if not_the_same_line:
                            if var_name in line_f2.code.strip():
                                if line_f2.line_type.name != "Comment":
                                    for line_f1 in file1.Lines:
                                        if line_f1.line_type.name != "Comment":
                                            if line_f1.line_type.name == line_f2.line_type.name:
                                                if numeric_value in line_f1.code.strip():
                                                    if line_f1.code.strip() != line_f2.code.strip():
                                                        if line_f1.code.strip().replace(numeric_value, var_name) == line_f2.code.strip():
                                                            refactors.append(Refactor("Replace Magic Number With Symbolic Constant",
                                                                                      file_name_1,
                                                                                      file_name_2,
                                                                                      version1_name,
                                                                                      version2_name, 
                                                                                      line_f1.line_number,
                                                                                      line_f1.line_number,
                                                                                      f2_line.line_type.start_index_of_declaration,
                                                                                      f2_line.line_type.end_index_of_declaration,
                                                                                      "#ff33ff",
                                                                                      "Organizing Data"
                                                                                     ))
                                                            break
    return refactors
    