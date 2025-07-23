from Refactor import Refactor
from util.refactors_utility import Get_all_methods_from_a_class
from util.refactors_utility import get_class_obj_by_name
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import class_belongs_to_deleted_or_introduced_class

def ExtractSubclass(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,introduced_classes):
    refactors=[]
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f2_line, "Class"):
            if len(introduced_classes)>0:
                for introduced_class_name,introduced_class_path in introduced_classes:
                    if class_belongs_to_deleted_or_introduced_class(f2_line.line_type,file2.file_path,introduced_class_name,introduced_class_path):
                        if f2_line.line_type.superclass_name != None:
                            superclass_f2 = get_class_obj_by_name(f2_line.line_type.superclass_name,file2)
                            if superclass_f2 is not None:
                                superclass_methods_f2 = Get_all_methods_from_a_class(superclass_f2.line_type,file2)
                                subclass_methods_f2=Get_all_methods_from_a_class(f2_line.line_type,file2)
                                if any(super_method.function_name == sub_method.function_name for super_method in superclass_methods_f2 for sub_method in subclass_methods_f2):
                                    superclass_f1 = get_class_obj_by_name(f2_line.line_type.superclass_name,file1)
                                    if superclass_f1 is not None:
                                        refactors.append(Refactor("Extract Subclass",
                                                        file_name_1,
                                                        file_name_2,
                                                        version1_name,
                                                        version2_name, 
                                                        superclass_f1.line_number,
                                                        superclass_f1.line_type.class_content_end_line,
                                                        f2_line.line_number,
                                                        f2_line.line_type.class_content_end_line,
                                                        "#99cccc",
                                                        "Dealing With Generalizations",
                                        ))
                                break
    return refactors
