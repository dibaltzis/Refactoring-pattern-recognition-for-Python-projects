from Refactor import Refactor
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def ReplaceArrayWithObject(version1_name, version2_name, block, file1, file2, name_1, name_2, introduced_classes):
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Declaration"):
            if f1_line.line_type.assigned_content.strip().startswith("[") and f1_line.line_type.assigned_content.strip().endswith("]"):
                if not_blank_and_line_type_is_equal_to(f2_line, "Declaration"):
                    if f1_line.line_type.variable_name == f2_line.line_type.variable_name:
                        if not f2_line.line_type.assigned_content.strip().startswith("[") or not f2_line.line_type.assigned_content.strip().endswith("]"):
                            if "(" in f2_line.line_type.assigned_content:
                                name_of_object = f2_line.line_type.assigned_content.strip().split("(")[0].strip()
                                if name_of_object != "":
                                    if any(name_of_object in introduced_class_name for introduced_class_name,_ in introduced_classes):
                                        refactors.append(Refactor("Replace Array With Object",
                                                                 name_1,
                                                                 name_2,
                                                                 version1_name,
                                                                 version2_name,
                                                                 f1_line.line_type.start_index_of_declaration,
                                                                 f1_line.line_type.end_index_of_declaration,
                                                                 f2_line.line_type.start_index_of_declaration,
                                                                 f2_line.line_type.end_index_of_declaration,
                                                                 "#993366",
                                                                 "Organizing Data"
                                                                 ))

    return refactors
