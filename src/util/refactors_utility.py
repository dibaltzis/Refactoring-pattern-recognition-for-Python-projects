def class_belongs_to_deleted_or_introduced_class(class_obj,file_path,introduced_deleted_class_name,introduced_deleted_class_path):
    if introduced_deleted_class_name == class_obj.name_of_the_class:
            if  file_path in introduced_deleted_class_path:
                return True
    return False

def not_blank_and_line_type_is_equal_to(line,type):
    if line!="":
        return line.line_type.name == type
    else:
        return False

def partOfClass(code_line,file):
    for line_file1 in file.Lines:
        if line_file1.line_type.name == "Class":
            for part_of_content_index in range (line_file1.line_type.class_content_start_line, line_file1.line_type.class_content_end_line+1):
                if code_line.line_number in range(line_file1.line_type.class_content_start_line, line_file1.line_type.class_content_end_line+1):
                    if code_line.code.strip() == file.Lines[part_of_content_index].code.strip():
                        return True,line_file1
    return False,""

def if_function_is_in_class(function_obj,file):
    for line in file.Lines:
        if line.line_type.name == "Class":
            for part_of_content_index in range (line.line_type.class_content_start_line, line.line_type.class_content_end_line+1):
                part_of_content_line = file.Lines[part_of_content_index]
                if part_of_content_line.line_type.name == "Function":
                    if part_of_content_line.line_type.function_name == function_obj.function_name:
                        return True,line.line_type
    return False,""

def get_attributes_of__init__function_of_a_class(class_obj,file):
    attributes = []
    init_function_object=None
    init_function_exist =False
    for index in range(class_obj.class_content_start_line, class_obj.class_content_end_line+1):
        line = file.Lines[index]
        if line.line_type.name == "Function":
            if line.line_type.function_name == "__init__":
                init_function_object = line.line_type
                init_function_exist = True
                break
    if init_function_exist:
        for line in range(init_function_object.start_index_of_function_content, init_function_object.end_index_of_function_content+1):
            line = file.Lines[line]
            if line.line_type.name == "Declaration":
                if line.line_type.variable_name.startswith("self."):
                    #if line.line_type.assigned_content.split("#")[0].strip() in init_function_object.function_parameters
                    attributes.append(line)
                    
    return init_function_object,attributes
    
def Get_all_methods_from_a_class(class_obj,file):
    methods = []
    for index in range(class_obj.class_content_start_line, class_obj.class_content_end_line+1):
        line = file.Lines[index]
        if line.line_type.name == "Function":
            methods.append(line.line_type)
    methods = [obj for obj in methods if obj.function_name != "__init__"]
    return methods


def attribute_of_class(attr_name,class_obj,file):
    for index in range(class_obj.line_type.class_content_start_line, class_obj.line_type.class_content_end_line+1):
        line = file.Lines[index]
        if line.line_type.name == "Declaration":
            if line.line_type.variable_name.strip() == attr_name.strip():
                return [True,line]
    return [False,None]



def get_subclasses_from_superclass(superclass_name,file):
    subclasses = []
    for line in file.Lines:
        if line.line_type.name == "Class":
            if line.line_type.superclass_name == superclass_name:
                subclasses.append(line)
    return subclasses

def is_super_atr_from_subclasses(subclass_name,atr,file):
    atr =atr.replace("self.","")
    for line in file.Lines:
        if line.line_type.name == "Class":
            if line.line_type.name_of_the_class == subclass_name:
                for index in range(line.line_type.class_content_start_line, line.line_type.class_content_end_line+1):
                    line_of_class = file.Lines[index]
                    if line_of_class.code.strip().startswith("super().__init__("):
                        attributes= line_of_class.code.strip().split("super().__init__(")[1].replace(")","").split(",")
                        if any(atr in attribute for attribute in attributes):
                            return True
    return False
                        
def if_line_is_in_class(code_line,class_obj,file):
    for index in range(class_obj.line_type.class_content_start_line, class_obj.line_type.class_content_end_line+1):
        if index>= len(file.Lines)-1:
            return False
        line = file.Lines[index]
        if line.code.strip() == code_line.code.strip():
            return True
    return False

def get_method_from_a_class(method_name,class_obj,file):
    for index in range(class_obj.line_type.class_content_start_line, class_obj.line_type.class_content_end_line+1):
        line = file.Lines[index]
        if line.line_type.name == "Function":
            if line.line_type.function_name == method_name:
                return line
    return None


def if_class_is_sub_super_class_of_the_other(class1,class2):
    if class1.line_type.superclass_name!=None:
        if class1.line_type.superclass_name == class2.line_type.name_of_the_class:
            return True
    if class2.line_type.superclass_name!=None:
        if class2.line_type.superclass_name == class1.line_type.name_of_the_class:
            return True
    return False

def get_attributes_inside_parenthesis(code_line,file):
    attr = []
    if "(" in code_line.code.strip():
        if code_line.code.strip().startswith("super().__init__("):
            temp  = code_line.code.strip().split("super().__init__(")[1].replace("\\","")
            attr.extend(filter(None, [x.strip() for x in temp.split(')')[0].split(',')]))
        else:
            attr.append(code_line.code.strip().split("(")[1])
        if code_line.code.strip().endswith(",") or code_line.code.strip().endswith("\\") or  code_line.code.strip().endswith("("):
            index = code_line.line_number+1
            while not file.Lines[index].code.strip().endswith(")") and index<=len(file.Lines)-1:
                attr.append(file.Lines[index].code.strip().replace(",","").replace("\\",""))
                index+=1
            if file.Lines[index].code.strip().endswith(")"):
                attr.append(file.Lines[index].code.strip().replace(",","").replace("\\","").replace(")","").strip())
        return attr
    else:
        return None

def get_class_obj_by_name(class_name,file):
    for line in file.Lines:
        if line.line_type.name == "Class":
            if line.line_type.name_of_the_class == class_name:
                return line
    return None

def declaration_exist_in_file(declaration_obj,file):
    for line in file.Lines:
        if line.line_type.name == "Declaration":
            if line.line_type.variable_name.strip() == declaration_obj.variable_name.strip():
                if line.line_type.assigned_content.strip() == declaration_obj.assigned_content.strip():
                    return line.line_type
    return False

def find_common_attributes(list1, list2):
    return list(set(list1) & set(list2))



def compare_classes(class1,class2,file1,file2):
    # compare by
    # - name
    # - super/sub
    # - attributes
    # - methods
    super_sub_check = False
    attributes_check = False
    methods_check = False
    class1_length = (class1.line_type.class_content_end_line - class1.line_type.class_content_start_line)
    class2_length = (class2.line_type.class_content_end_line - class2.line_type.class_content_start_line)
    if class1.line_type.name_of_the_class == class2.line_type.name_of_the_class:
        if class1_length == class2_length:
            return True
    if class1.line_type.superclass_name!=None and class2.line_type.superclass_name!=None:
        if class1.line_type.superclass_name == class2.line_type.superclass_name:
            super_sub_check = True
    elif class1.line_type.superclass_name==None and class2.line_type.superclass_name==None:
        super_sub_check = True
 
    f1_init_function_object,f1_class_atr = get_attributes_of__init__function_of_a_class(class1.line_type,file1)
    f2_init_function_object,f2_class_atr = get_attributes_of__init__function_of_a_class(class2.line_type,file2)
    if f1_init_function_object is not None and f2_init_function_object is not None:
        if len(f1_class_atr)>0 and len(f2_class_atr)>0:
            if any (f1_atr.line_type.variable_name == f2_atr.line_type.variable_name for f1_atr,f2_atr in zip(f1_class_atr,f2_class_atr)):
                attributes_check = True
    class1_methods = Get_all_methods_from_a_class(class1.line_type,file1)
    class2_methods = Get_all_methods_from_a_class(class2.line_type,file2)
    if any(f1_method.function_name == f2_method.function_name for f1_method,f2_method in zip(class1_methods,class2_methods)):
        methods_check = True
    if  super_sub_check and attributes_check and methods_check:
        return True
    else:
        return False
