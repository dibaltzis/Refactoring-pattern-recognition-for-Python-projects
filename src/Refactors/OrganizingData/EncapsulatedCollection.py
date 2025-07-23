from Refactor import Refactor
from util.refactors_utility import Get_all_methods_from_a_class
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_attributes_of__init__function_of_a_class

def EncapsulatedCollection(version1_name, version2_name, block, file1, file2, name_1, name_2):
    refactors = []
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Class"):
            f1_init_function_object, f1_class_atr = get_attributes_of__init__function_of_a_class(f1_line.line_type, file1)
            if f1_init_function_object is not None:
                for line_f2 in file2.Lines:
                    if line_f2.line_type.name == "Class" and line_f2.line_type.name_of_the_class == f1_line.line_type.name_of_the_class:
                        _f2_init_function_object,_f2_class_atr = get_attributes_of__init__function_of_a_class(line_f2.line_type, file2)
                        if _f2_init_function_object is not None:
                            for f1_atr in f1_class_atr:
                                f1_atr_name = f1_atr.line_type.variable_name.replace("self.", "").strip()
                                for _f2_atr in _f2_class_atr:
                                    _f2_atr_name = _f2_atr.line_type.variable_name.replace("self.", "").strip()
                                    if "_"+f1_atr_name == _f2_atr_name:
                                        decl_content_f1 = f1_atr.line_type.assigned_content.split("#")[0].strip()
                                        decl_content_f2 = _f2_atr.line_type.assigned_content.split("#")[0].strip()
                                        if decl_content_f1.endswith("]" or ")" or "}") and decl_content_f2.endswith("]" or ")" or "}"):
                                            methods_of_f2_class = Get_all_methods_from_a_class(line_f2.line_type, file2)
                                            if (any("get" in method.function_name for method in methods_of_f2_class) or \
                                                any("Get" in method.function_name for method in methods_of_f2_class)) and\
                                                any(f1_atr_name.lower() in method.function_name.lower() for method in methods_of_f2_class):
                                                refactors.append(Refactor("Encapsulated Collection",
                                                                         name_1,
                                                                         name_2,
                                                                         version1_name,
                                                                         version2_name, 
                                                                         f1_atr.line_type.start_index_of_declaration,
                                                                         f1_atr.line_type.end_index_of_declaration,
                                                                         _f2_atr.line_type.start_index_of_declaration,
                                                                         _f2_atr.line_type.end_index_of_declaration,
                                                                         "#ff6600",
                                                                         "Organizing Data"
                                                                         ))
                                                break
    return refactors
