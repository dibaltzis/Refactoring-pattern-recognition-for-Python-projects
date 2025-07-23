from Refactor import Refactor
from util.refactors_utility import partOfClass,attribute_of_class
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def PullUpField(version1_name,version2_name,block,file1,file2,name_1,name_2):
    refactors =[]
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Declaration"):
                part_of_class_bool1, line1_class = partOfClass(f1_line,file1)
                if part_of_class_bool1:
                    if line1_class.line_type.superclass_name != None:
                            if f2_line !="":  
                                if f2_line.code.strip().startswith("super().__init__("):
                                    #check if the superclass contains the field
                                    for class_ in file1.Lines:
                                        if class_.line_type.name == "Class":
                                            if class_.line_type.name_of_the_class == line1_class.line_type.superclass_name:
                                                    if not attribute_of_class(f1_line.line_type.variable_name,class_,file2)[0]:
                                                        more_than_one_subclass_with_the_same_field=False
                                                        for class_ in file1.Lines:
                                                            if class_.line_type.name == "Class":
                                                                if line1_class.line_type.name_of_the_class != class_.line_type.name_of_the_class :
                                                                    if line1_class.line_type.superclass_name == class_.line_type.superclass_name :
                                                                        if attribute_of_class(f1_line.line_type.variable_name,class_,file1):
                                                                            more_than_one_subclass_with_the_same_field=True
                                                                            break
                                                        if more_than_one_subclass_with_the_same_field:
                                                            #version 2 of the file has not the same field in the subclasses with the same superclass
                                                            condition = False
                                                            for class_ in file2.Lines:
                                                                if class_.line_type.name == "Class":
                                                                        if line1_class.line_type.superclass_name == class_.line_type.superclass_name :
                                                                            if not attribute_of_class(f1_line.line_type.variable_name,class_,file2)[0]:
                                                                                condition=True
                                                                                break
                                                            if condition:
                                                                #now we check if the superclass in the next version has that field in it
                                                                for class_ in file2.Lines:
                                                                    if class_.line_type.name == "Class":
                                                                        if class_.line_type.name_of_the_class == line1_class.line_type.superclass_name:
                                                                            check,attr =attribute_of_class(f1_line.line_type.variable_name,class_,file2)
                                                                            if check:
                                                                                refactors.append(Refactor("Pull Up Field",
                                                                                name_1,
                                                                                name_2,
                                                                                version1_name,
                                                                                version2_name, 
                                                                                f1_line.line_type.start_index_of_declaration,
                                                                                f1_line.line_type.end_index_of_declaration,
                                                                                attr.line_type.start_index_of_declaration,
                                                                                attr.line_type.end_index_of_declaration,
                                                                                "#79443b",
                                                                                "Dealing With Generalizations",
                                                                                ))
                                        
    return refactors