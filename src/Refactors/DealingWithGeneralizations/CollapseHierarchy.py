from Refactor import Refactor
from util.refactors_utility import get_class_obj_by_name
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import get_attributes_of__init__function_of_a_class
from util.refactors_utility import class_belongs_to_deleted_or_introduced_class

def CollapseHierarchy(version1_name,version2_name,block,file1,file2,name_1,name_2,deleted_classes):
    refactors=[]
    for f1l in block.f1_lines_list:
        f1_line = f1l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Class"):
            if len(deleted_classes)>0:
                for deleted_class_name,deleted_class_path in deleted_classes:
                    if class_belongs_to_deleted_or_introduced_class(f1_line.line_type,file1.file_path,deleted_class_name,deleted_class_path):  
                        if f1_line.line_type.superclass_name!=None:
                            del_sub_init_function_object_f1,del_sub_attributes_f1 = get_attributes_of__init__function_of_a_class(f1_line.line_type,file1)
                            super_class_obj_f1 = get_class_obj_by_name(f1_line.line_type.superclass_name,file1)
                            if super_class_obj_f1 is not None:
                                sup_init_function_object_f1,sup_attributes_f1 = get_attributes_of__init__function_of_a_class(super_class_obj_f1.line_type,file1)
                                if del_sub_init_function_object_f1 is not None and sup_init_function_object_f1 is not None:
                                    if not all(del_sub_attr.line_type.variable_name == sup_attr.line_type.variable_name for del_sub_attr in del_sub_attributes_f1 for sup_attr in sup_attributes_f1 ):
                                        super_class_obj_f2 = get_class_obj_by_name(super_class_obj_f1.line_type.name_of_the_class,file2)
                                        if super_class_obj_f2 is not None:
                                            sup_init_function_object_f2,sup_attributes_f2 = get_attributes_of__init__function_of_a_class(super_class_obj_f2.line_type,file2)
                                            if sup_init_function_object_f2 is not None:
                                                if any(del_sub_attr.line_type.variable_name == sup_attr.line_type.variable_name for del_sub_attr in del_sub_attributes_f1 for sup_attr in sup_attributes_f2 ):
                                                    refactors.append(Refactor("Collapse Hierarchy",
                                                        name_1,
                                                        name_2,
                                                        version1_name,
                                                        version2_name, 
                                                        f1_line.line_number,
                                                        f1_line.line_type.class_content_end_line,
                                                        super_class_obj_f2.line_number,
                                                        super_class_obj_f2.line_type.class_content_end_line,
                                                        "#99ffff",
                                                        "Dealing With Generalizations",
                                                        ))
                                                                
                                                                
    return refactors                    