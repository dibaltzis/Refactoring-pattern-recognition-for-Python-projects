from thefuzz import fuzz
from Refactor import Refactor
import re
from util.refactors_utility import not_blank_and_line_type_is_equal_to

def PreserveWholeObject(version1_name,version2_name,block,file1,file2,file_name_1,file_name_2,introduced_classes):
    """
    Try to find the refactor "Preserve Whole Object"

    Args:
        block (Block): The block object.
        file1 (str): The file1 path.
        file2 (str): The file2 path.
        file_name_1 (str): The name of file1.
        file_name_2 (str): The name of file2.

    Returns:
        list: The list of refactors.

    How it works:
        file 1: 
        0. min_temperature = 20
        1. max_temperature = 30
        2. temperature_difference = calculate_temperature_difference(min_temperature, max_temperature)

        file 2:
        0. temperature_range = TemperatureRange(min_temperature=20, max_temperature=30)
        1. temperature_difference = calculate_temperature_difference(temperature_range)

        Check if file1 line 2 are Declaration and file2 line 1 is Declaration.   
        Check if their variable has the same name
        check if the part after the = of file1 line 2 is a function call
        if yes ,it finds the parameters of the function call of file1 line 2
        if the parameters are not empty it checks if file2 line 1 after the = is a function call
        if yes ,it finds the parameters of the function call of file2 line 1
        if the parameters of file2 line 1 are not empty it checks if they are the same
        Check if the parameters of file1 line 2 are less than the parameters of file2 line 1 and the file2 line 1 is not empty parameters is equal with 1
        Check if the parameter of file2 line 1 is not in the parameter of file1 line 2
        Finally check if this parameter is in the list of introduced classes and  then creates the refactor object
    """
    refactors = []
    for f1l, f2l in zip(block.f1_lines_list, block.f2_lines_list):
        f1_line = f1l.line
        f2_line = f2l.line
        if not_blank_and_line_type_is_equal_to(f1_line, "Declaration"):
            if not_blank_and_line_type_is_equal_to(f2_line, "Declaration"):
                if f1_line.line_type.variable_name == f2_line.line_type.variable_name:
                    if bool(re.search(r'\w+\(', f1_line.line_type.assigned_content)):
                        match = re.search(r'\((.*?)\)', f1_line.line_type.assigned_content)
                        f1_parameters = [param.strip() for param in match.group(1).split(',') if param.strip()] if match else []
                        if f1_parameters != [] and bool(re.search(r'\w+\(', f2_line.line_type.assigned_content)):
                            match = re.search(r'\((.*?)\)', f2_line.line_type.assigned_content)
                            f2_parameters = [param.strip() for param in match.group(1).split(',') if param.strip()] if match else []
                            if f2_parameters!=[]:
                                if len(f2_parameters) ==1 and len(f2_parameters) < len(f1_parameters):
                                    if f2_parameters[0] not in f1_parameters:  
                                        for introduced_class_name,_ in introduced_classes:
                                            if f2_parameters[0] == introduced_class_name:
                                                refactors.append(Refactor("Preserve Whole Object",
                                                    file_name_1,
                                                    file_name_2,
                                                    version1_name,
                                                    version2_name, 
                                                    f1_line.line_type.start_index_of_declaration,
                                                    f1_line.line_type.end_index_of_declaration,
                                                    f2_line.line_type.start_index_of_declaration,
                                                    f2_line.line_type.end_index_of_declaration,
                                                    "#009966",  
                                                    "Simplifying Method Calls"
                                                    ))                                               
    return refactors

