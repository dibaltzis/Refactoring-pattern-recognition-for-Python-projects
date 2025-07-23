from Refactor import Refactor
from util.refactors_utility import get_subclasses_from_superclass
from util.refactors_utility import get_class_obj_by_name
from util.refactors_utility import not_blank_and_line_type_is_equal_to
from util.refactors_utility import class_belongs_to_deleted_or_introduced_class

def ExtractSuperclass(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,introduced_classes):
    refactors=[]
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f2_line, "Class"):
                if len(introduced_classes)>0:
                    for introduced_class_name,introduced_class_path in introduced_classes:    
                        if class_belongs_to_deleted_or_introduced_class(f2_line.line_type,file2.file_path,introduced_class_name,introduced_class_path):                   
                            if f2_line.line_type.superclass_name == None:
                                subclasses_f2 = get_subclasses_from_superclass(f2_line.line_type.name_of_the_class,file2)
                                if len(subclasses_f2)>0:
                                    for sub_f2 in subclasses_f2:
                                        class_obj = get_class_obj_by_name(sub_f2.line_type.name_of_the_class, file1)
                                        if class_obj!= None:
                                            if class_obj.line_type.superclass_name == None:
                                                refactors.append(Refactor("Extract Superclass",
                                                            file_name_1,
                                                            file_name_2,
                                                            version1_name,
                                                            version2_name, 
                                                            class_obj.line_number,
                                                            class_obj.line_type.class_content_end_line,
                                                            f2_line.line_number,
                                                            f2_line.line_type.class_content_end_line,
                                                            "#99ff00",
                                                            "Dealing With Generalizations",
                                        ))
                                            
                                        
                                    
    return refactors