from Refactor import Refactor
from util.refactors_utility import is_super_atr_from_subclasses
from util.refactors_utility import partOfClass
from util.refactors_utility import get_subclasses_from_superclass
from util.refactors_utility import attribute_of_class
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def PushDownField(version1_name,version2_name,block,file1,file2,name_1,name_2):
    refactors =[]
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Declaration"):
                part_of_class_bool1, line1_class = partOfClass(f1_line,file1)
                if part_of_class_bool1:
                    if line1_class.line_type.superclass_name == None:
                        flag =False
                        if f2_line =="": flag = True
                        elif f2_line.line_type.name == "Declaration":
                            if f1_line.line_type.variable_name == f2_line.line_type.variable_name: flag = False
                        else: flag=True
                        if flag:
                            subclasses_f1  = get_subclasses_from_superclass(line1_class.line_type.name_of_the_class,file1)
                            check_if_atr_initialized_in_subclasses_with_super = False
                            for sub_class in subclasses_f1:
                                sub_class_name=sub_class.line_type.name_of_the_class
                                check_if_atr_initialized_in_subclasses_with_super =  is_super_atr_from_subclasses(sub_class_name,f1_line.line_type.variable_name,file1)
                                break
                            if check_if_atr_initialized_in_subclasses_with_super:
                                subclasses_f2  = get_subclasses_from_superclass(line1_class.line_type.name_of_the_class,file2)
                                for sub_class in subclasses_f2:
                                    sub_class_name=sub_class.line_type.name_of_the_class
                                    is_atr_of_class,attr = attribute_of_class(f1_line.line_type.variable_name,sub_class,file2)
                                    if  is_atr_of_class:
                                        refactors.append(Refactor("Push Down Field",
                                                            name_1,
                                                            name_2,
                                                            version1_name,
                                                            version2_name, 
                                                            f1_line.line_type.start_index_of_declaration,
                                                            f1_line.line_type.end_index_of_declaration,
                                                            attr.line_type.start_index_of_declaration,
                                                            attr.line_type.end_index_of_declaration,
                                                            "#e3dac9",
                                                            "Dealing With Generalizations",
                                                        ))
                                                            
                                    

    return refactors
    