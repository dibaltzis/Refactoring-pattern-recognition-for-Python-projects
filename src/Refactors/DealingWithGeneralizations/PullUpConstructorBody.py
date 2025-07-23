from Refactor import Refactor
from util.refactors_utility import partOfClass,get_attributes_inside_parenthesis
from util.refactors_utility import get_attributes_of__init__function_of_a_class

def PullUpConstructorBody(version1_name,version2_name,block,file1,file2,name_1,name_2):
    refactors =[]
    for f2l in block.f2_lines_list:
        f2_line = f2l.line
        if f2_line !="":
            if f2_line.code.strip().startswith("super().__init__("):
                check_if_it_is_in_a_class ,class_name2 = partOfClass(f2_line,file2)
                if check_if_it_is_in_a_class:
                    if class_name2.line_type.superclass_name != None:
                        init_obj_2,init_attr_f2 = get_attributes_of__init__function_of_a_class(class_name2.line_type,file2)
                        attr_f2=[]
                        if init_obj_2 is not None:
                            attr_f2=get_attributes_inside_parenthesis(f2_line,file2)
                        if attr_f2!= []:    
                            for line_f1 in file1.Lines:
                                if line_f1.line_type.name == "Class":
                                    if line_f1.line_type.name_of_the_class == class_name2.line_type.name_of_the_class:
                                        init_obj_1,init_attr_f1 = get_attributes_of__init__function_of_a_class(line_f1.line_type,file1)
                                        if init_obj_1 is not None:
                                            if not any(file1.Lines[index].code.strip() == f2_line.code.strip() for index in range(init_obj_1.start_index_of_function_content, init_obj_1.end_index_of_function_content+1)):
                                                attr_f1=[]
                                                if init_obj_1 is not None:
                                                    for atr in init_attr_f1 :
                                                        attr_f1.append(atr.line_type.assigned_content)
                                                    if all(atr2 in attr_f1 for atr2 in attr_f2):
                                                        refactors.append(Refactor("Pull Up Constructor Body",
                                                            name_1,
                                                            name_2,
                                                            version1_name,
                                                            version2_name, 
                                                            init_obj_1.start_index_of_the_declaration,
                                                            init_obj_1.end_index_of_the_declaration,
                                                            init_obj_2.start_index_of_the_declaration,
                                                            init_obj_2.end_index_of_the_declaration,
                                                            "#993333",
                                                            "Dealing With Generalizations",              
                                                        ))
                                                        break    
                                            else:
                                                    break

                    
    
    return refactors

