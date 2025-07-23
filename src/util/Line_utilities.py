from Line import *
import re
#recognize the type of the given line
def Line_type_separation(line, codelist, index, index_of_line_comment_to_skip):
    """
    Checks what type is each line and returns the appropriate Line type object.
    
    Args:
        line (str): The line of code to process.
        codelist (list): The list of code lines.
        index (int): The index of the current line.
        index_of_line_comment_to_skip (int): The index of the line comment to skip.
        
    Returns:
        tuple: The comment object and the index of the line comment to skip.
    """
    line = line.strip().replace("\n", "")
    if "#" in line:
        line =line.split("#")[0].strip()
    # Check if line is a comment
    if codelist[index].strip().startswith("#") or ('"""') in codelist[index].strip():
        comment_obj, index_of_line_comment_to_skip = check_if_is_comment(line, codelist, index, index_of_line_comment_to_skip)
        return comment_obj, index_of_line_comment_to_skip
    else:
        # Check if line is an exception
        if line.startswith("try:"):
            exception_obj = check_if_it_is_exception(line, codelist, index)
            return exception_obj, index_of_line_comment_to_skip
            
        # Check if line is a Conditional
        elif line.startswith("if") or line.startswith("elif"):# or ("else:") in line:
            condition_obj = check_if_it_is_conditional(line, codelist, index)
            return condition_obj, index_of_line_comment_to_skip
        
        # Check if line is an Assertion
        elif line.strip().startswith("assert"):
            assertion_obj = check_if_it_is_assertion(line, codelist, index)
            return assertion_obj, index_of_line_comment_to_skip

        # Check if line is a Return
        elif line.startswith("return "):
            content_of_the_return = line[7:].strip()
            start_index_of_return = index
            if not content_of_the_return.endswith(",") or not content_of_the_return.endswith("\\") :
                end_index_of_return = index
            else:
                end_index_of_return = endline_by_the_number_of_blanks(codelist, start_index_of_return)    
            return Return_(content_of_the_return,start_index_of_return,end_index_of_return), index_of_line_comment_to_skip
        
        # Check if line is a Class
        elif "class " in line:
            class_obj = check_if_it_is_a_class(line, codelist, index)
            return class_obj, index_of_line_comment_to_skip
        
        # Check if line is a For or While loop
        elif line.startswith('while') or line.startswith('for'):
            loop_obj = check_if_it_is_loop(line, codelist, index)
            return loop_obj, index_of_line_comment_to_skip
        
        # Check if line is a Function
        elif (line.startswith("def ") or line.startswith("async def ") and (line.endswith('(') or line.endswith(":") or line.endswith(',') or line.endswith(',')) ):
                function_obj = check_if_is_function(line, codelist, index)
                return function_obj, index_of_line_comment_to_skip
        
        # Check if line is an Import
        elif line.startswith("import") or line.startswith("from"):
            return Import_(), index_of_line_comment_to_skip
        
        # Check if line is a Declaration
        elif ("=" in line and not any(x in line for x in {"==", "!=", "+=", "-=", "*=", "/=", "//=", "%=", "**="})) or line.strip().startswith("global ") or line.strip().startswith("nonlocal "):
            declaration_obj = check_if_it_is_declaration(line, codelist, index)
            return declaration_obj, index_of_line_comment_to_skip
        
        # Check if line is a blank line
        elif line == "" or line  == " " or line =="\n":
            return Blank(), index_of_line_comment_to_skip
        



    return determine_what_other_it_is(line,  index), index_of_line_comment_to_skip


def endline_by_the_number_of_blanks(list,index):
    end_line_index=index+1
    start_line_index = index+1
    if end_line_index < len(list):
        for i in range(index+1,len(list)):
            if list[i].strip().startswith("#") or list[i].strip().startswith('"""') :
                start_line_index=i
            elif list[i].isspace():
                start_line_index=i+1
            else :       
                break
        if start_line_index < len(list):
            num_of_spaces=len(list[start_line_index]) - len(list[start_line_index].lstrip())
        else: 
            return len(list)-1
        for i in range(start_line_index+1,len(list)):
            l = list[i]
            if not l.lstrip().startswith("#") and not l.lstrip().startswith('"""'):
                if l.rstrip() !="":
                    if len(l) - len(l.lstrip()) >=num_of_spaces:
                        end_line_index =i
                    else:
                        break
    else :
        end_line_index = len(list)-1
    return end_line_index

def endline_by_the_number_of_blanks_for_functions(list,index):
    end_line_index=index+1
    if end_line_index < len(list):
        i=index+1
        while list[i].strip().startswith("#") or list[i].strip().startswith('"""'):
            i +=1
        start_line_index = i
        i = start_line_index
        while not list[i].strip().endswith(":"):
            i+=1
            if i >= len(list)-1:
                i = len(list)-1
                break
        end_line_index = i
    else:
        end_line_index = len(list)-1
    return end_line_index

def getParams(codelist, start_index, end_index):
    """
    Extracts the parameters from a given list of code lines.

    Args:
        codelist (List[str]): The list of code lines.
        start_index (int): The starting index in the code list.
        end_index (int): The ending index in the code list.

    Returns:
        List[str]: The extracted parameters.

    """
    
    # Parameters are in the same line example: 'def test(param1, param2)'
    if start_index == end_index:
        match = re.search(r"def\s+\w+\(([^)]*)\)", codelist[start_index])
        parameters = [param.strip() for param in match.group(1).split(',') if param.strip()] if match else []
    else:
        simpler_list_to_a_single_string = "\n".join(codelist[start_index:end_index + 1])
        match = re.search(r"def\s+\w+\(([^)]*)\)", simpler_list_to_a_single_string, re.DOTALL)
        parameters = [param.strip() for param in match.group(1).replace('\n', '').split(',') if param.strip()] if match and match.group(1) else []
    #example def test(param1, param2: int):
    parameters_with_out_annotations = []
    for parameter in parameters:
        if ":" in parameter:
            parameter = parameter.split(":")[0].strip()
        if "=" in parameter:
            parameter = parameter.split("=")[0].strip()
        if "]" in parameter or "[" in parameter:
            pass
        else:
            parameters_with_out_annotations.append(parameter)
    return parameters_with_out_annotations

def check_if_it_is_a_class(line, codelist, index):
    """
    Checks if a line is a class.+9*-

    Parameters:
        line (str): The line of code containing the class definition.
        codelist (list): The list of code lines.
        index (int): The index of the current line.

    Returns:
        tuple: A tuple containing the name of the class, the line number where the class content starts, and the line number where the class content ends.
    """
    #name_of_the_class =  if ":" in line.split("class")[1] else line.split("class")[1].strip()

    if "(" in line.split("class")[1]:
        name_of_the_class =line.split("class")[1].split("(")[0].strip()
    elif ":" in line.split("class")[1]:
        name_of_the_class =line.split("class")[1].strip(":").strip()
    else:
        name_of_the_class =line.split("class")[1].strip()
    
    superclass_name = re.search(r'\((.*?)\)', line).group(1) if re.search(r'\((.*?)\)', line) else None
    class_content_start_line = index
    class_content_end_line = endline_by_the_number_of_blanks(codelist, index)
    return Class_(name_of_the_class, class_content_start_line, class_content_end_line,superclass_name)
    


def check_if_it_is_conditional(line,codelist,index):
    """
        Checks if a line is Conditional.

        Parameters:
        - line: The current line being processed.
        - codelist: The list of lines of code.
        - index: The index of the current line.

        Returns:
        - A Conditional object representing the if statement.

        Raises:
        - AssertionError: If the end index of a multi-lined 'if' statement is None.
    """
    start_index_of_if_expression = index
    # if the line ends with ":" it means that 'if' is not multiline and its content is on a new line
    if line.endswith(':'):            
        matches = re.findall(r"(if|elif)\s+(.+):", line)
        conditional_expressions = [condition.strip() for _, conditions in matches for condition in re.split(r'\s+(?:and|or)\s+', conditions)]
        end_index_of_if_expression = index
        if_content_start_index = index+1
        if_content_end_index = endline_by_the_number_of_blanks(codelist, index)
    # the 'if' is multi-lined example 'if test==1 and \'
    elif line.endswith('\\'):
        splitted_if_end_index = None
        for i in range(index, len(codelist)):
            l = codelist[i].strip()
            if l != "" and ":" in l:
                    splitted_if_end_index = i
                    break        
        assert splitted_if_end_index is not None, "Function check_if_it_is_conditional when checking if 'if' is multi-lined: splitted_if_end_index is None"
        end_index_of_if_expression = splitted_if_end_index
        conditional_expressions = []
        for item in codelist[start_index_of_if_expression:end_index_of_if_expression + 1]:
            item = item.strip()
            conditional_expression_for_each_line = re.split(r'\s+and\s+|\s+or\s+', item) 
            conditional_expression_for_each_line = [ce.replace("if ", "").replace("elif ", "").replace(":", "") for ce in conditional_expression_for_each_line if ce and ce != '\\']
            for i in conditional_expression_for_each_line:
                conditional_expressions.append(i)
        end_index_of_if_expression = splitted_if_end_index
        if_content_start_index = end_index_of_if_expression+1
        if_content_end_index = endline_by_the_number_of_blanks(codelist, if_content_start_index)

    # the if is one line and it has its content in the same line
    # example if test==1:    return something
    else:
        matches = re.findall(r"(if|elif)\s+(.+):", line)
        if not matches:
            return determine_what_other_it_is(line, index)
        conditional_expressions = [condition.strip() for _, conditions in matches for condition in re.split(r'\s+(?:and|or)\s+', conditions)]
        end_index_of_if_expression = index
        if_content_start_index = index
        if_content_end_index = index
    return Conditional_(start_index_of_if_expression, end_index_of_if_expression, if_content_start_index, if_content_end_index, conditional_expressions)
                
                
                
def check_if_is_comment(line,codelist,index,index_of_line_comment_to_skip):
    """
    Checks if a line is a comment.
    
    Args:
        line (str): The line of code to check.
        codelist (list): The list of code lines.
        index (int): The index of the current line being checked.
        index_of_line_comment_to_skip (int): The index of the line comment to skip.
    
    Returns:
        tuple: A tuple containing the result of the check and the updated index_of_line_comment_to_skip.
    """
    if index_of_line_comment_to_skip != index :
            if index==len(codelist)-1: 
                index_of_line_comment_to_skip= -1 
                return determine_what_other_it_is(line, index) , index_of_line_comment_to_skip
            content_of_the_comment = ""
            end_index_of_comment = index
            if line.startswith("#"):
                    content_of_the_comment = line[1:]
            else:

                        for line_of_code_index in range(index+1, len(codelist)-1):
                                    line  = codelist[line_of_code_index]
                                    line = line.strip()
                                    if '"""' in line :
                                        content_of_the_comment += line.replace('"""', "")
                                        end_index_of_comment = line_of_code_index
                                        index_of_line_comment_to_skip =line_of_code_index
                                        break
                                    else :
                                        content_of_the_comment += line + "\n"   
            content_of_the_comment=content_of_the_comment.strip()
            start_index_of_comment = index
            return Comment(start_index_of_comment,end_index_of_comment,content_of_the_comment), index_of_line_comment_to_skip
    else:
            index_of_line_comment_to_skip= -1
            return determine_what_other_it_is(line, index) , index_of_line_comment_to_skip

def check_if_is_function(line,codelist,index):
    """
    Checks if a given line is a function declaration.
    
    Parameters:
    - line: A string representing the line of code to check.
    - codelist: A list of strings representing the entire code.
    - index: An integer representing the index of the line in the codelist.
    
    Returns:
    - If the line is a function declaration, returns an instance of the Function_ class.
    """
    one_line_function_bool=False
    if line.endswith('(') or line.endswith(',') or line.endswith("\\"):
        end_index_of_function_declaration= endline_by_the_number_of_blanks_for_functions(codelist,index)
        function_parameters = getParams(codelist,index,end_index_of_function_declaration)
    elif line.endswith(":"):
        end_index_of_function_declaration = index
        function_parameters = getParams(codelist,index,index)
    else: #function is one line
        one_line_function_bool=True
        end_index_of_function_declaration = index
        function_parameters = getParams(codelist,index,index)
    if re.search(r"(async\s+)?def\s+(\w+)\(", line)!=None:
        function_name = re.search(r"(async\s+)?def\s+(\w+)\(", line).group(2)
    else:
        function_name = "Error getting the function name line["+str(line)+"]"
    start_index_of_function=index
    if not one_line_function_bool:      
        start_index_of_function_content = end_index_of_function_declaration+1
        end_index_of_function=endline_by_the_number_of_blanks(codelist,end_index_of_function_declaration)
        end_index_of_function_content=end_index_of_function
    else:
        start_index_of_function_content=index
        end_index_of_function=index
        end_index_of_function_content=index
    return Function_(function_name,function_parameters,start_index_of_function,end_index_of_function,start_index_of_function_content,end_index_of_function_content)

def check_if_it_is_loop(line,codelist,index):
    """
    Checks if given line is a loop.
    
    Parameters:
        line (str): The current line of code being processed.
        codelist (list): The list of code lines.
        index (int): The index of the current line of code.
    
    Returns:
        Loop: An object representing the loop with its start and end indices, as well as the start and end indices of its content.
    """
    loop_expression = re.search(r"(for|while)\s+(.+?):", line).group(2).strip() if re.search(r"(for|while)\s+(.+?):", line) else None
    if loop_expression == None:
        return determine_what_other_it_is(line,index)
    start_index_of_loop = index
    end_index_of_loop = index
    if  line.endswith(':'):
        start_index_of_loop_content = index+1
        if start_index_of_loop_content >= len(codelist)-1:
            end_index_of_loop_content = len(codelist)-1
            start_index_of_loop_content = len(codelist)-1
        else:
            end_index_of_loop_content = endline_by_the_number_of_blanks(codelist,start_index_of_loop_content)
    else:
        start_index_of_loop_content = index
        end_index_of_loop_content = index
    return Loop_(start_index_of_loop,end_index_of_loop,start_index_of_loop_content,end_index_of_loop_content,loop_expression)

def check_if_it_is_assertion(line, codelist, index):
    """
    Checks if a given line is an assertion statement.

    Args:
        line (str): The line of code to be checked.
        code_lines (list): The list of all code lines.
        index (int): The index of the line in the code_lines list.

    Returns:
        Assertion : An instance of the Assertion class if the line is an assertion statement,

    """
    assertion_regex= r'assert\s+(.+)$'
    if line.endswith("{") or line.endswith("(") or line.endswith("\\"): 
        start_index_of_the_assertion = index
        if start_index_of_the_assertion >= len(codelist)-1:
            end_index_of_the_assertion = len(codelist)-1
        else:
            end_index_of_the_assertion  = endline_by_the_number_of_blanks(codelist,start_index_of_the_assertion)+1
        assertion_content =""
        list_to_string = "\n".join(codelist[start_index_of_the_assertion+1:end_index_of_the_assertion+1])
        assertion_content = [re.search(assertion_regex, line).group(1) if re.search(assertion_regex, line) else None][0]
        if assertion_content != None:
            assertion_content = assertion_content+"\n"+list_to_string
    else:
        assertion_content = [re.search(assertion_regex, line).group(1) if re.search(assertion_regex, line) else None][0]
        start_index_of_the_assertion = index
        end_index_of_the_assertion = index
    return Assertion_(start_index_of_the_assertion, end_index_of_the_assertion, assertion_content)


def check_if_it_is_exception(line, codelist, index):
    """
    Checks if the given line is an exception block.

    Args:
        line (str): The line of code to check.
        codelist (list): The list of code lines.
        index (int): The index of the line in the code list.

    Returns:
        int or Exception_: The start and end indices of the exception block,
        start and end indices of the except block, start and end indices of the
        finally block, start and end indices of the else block.
        Returns -1 if no exception is found.
    """
    start_index_of_exception = index
    start_index_of_finally = None
    end_index_of_finally = None
    start_index_of_else = None
    end_index_of_else  = None
    index_of_except = index
    while (not codelist[index_of_except].strip().startswith("except ")) :
        index_of_except += 1
        if index_of_except >= len(codelist):
            return determine_what_other_it_is(line, index)
    start_index_of_except = index_of_except
    end_index_of_except = endline_by_the_number_of_blanks(codelist,index_of_except)
    expected_finally_or_else_index =None
    if  end_index_of_except!= len(codelist)-1:
        expected_finally_or_else_index = endline_by_the_number_of_blanks(codelist,start_index_of_except)+1
        if codelist[expected_finally_or_else_index].strip().startswith("finally:"):
            start_index_of_finally = expected_finally_or_else_index
            end_index_of_finally = endline_by_the_number_of_blanks(codelist,start_index_of_finally)
        elif codelist[expected_finally_or_else_index].strip().startswith("else:"):
            start_index_of_else = expected_finally_or_else_index
            end_index_of_else = endline_by_the_number_of_blanks(codelist,start_index_of_else)
    if  end_index_of_finally != None:
        end_index_of_exception =  end_index_of_finally
    elif end_index_of_else != None:
        end_index_of_exception = end_index_of_else
    else:
        end_index_of_exception = end_index_of_except
    return Exception_(start_index_of_exception,end_index_of_exception,start_index_of_except,end_index_of_except,start_index_of_finally,end_index_of_finally,start_index_of_else,end_index_of_else)

def check_if_it_is_declaration(line, codelist, index):
    """
    Check if the given line of code is a variable declaration.
    
    Args:
        line (str): The current line being processed.
        codelist (list): The list of code lines.
        index (int): The index of the current line in the codelist.
    
    Returns:
        Declaration: An instance of the Declaration class that represents the declaration found in the given line of code.
    """
    if "=" in line:
        variable_name = line.split("=")[0].strip()
        if any(char in variable_name for char in (",", "(","]")):
            return determine_what_other_it_is(line, index)
        if ":" in variable_name:
            variable_name = variable_name.split(":")[0].strip()
        
    elif line.strip().startswith("global ") or line.strip().startswith("nonlocal "):
        variable_name = line.split(" ")[0].strip()
    
    if line.endswith("{") or line.endswith("(") or line.endswith("\\"):
        start_index_of_declaration = index
        end_index_of_declaration = endline_by_the_number_of_blanks(codelist, start_index_of_declaration) + 1
        if "=" in line:
            assigned_content = line.split("=")[1].strip()
        elif line.strip().startswith("global ") or line.strip().startswith("nonlocal "):
            assigned_content = line.split(" ")[1].strip()
        list_to_string = "\n".join(codelist[start_index_of_declaration+1:end_index_of_declaration+1])
        assigned_content = assigned_content + "\n" + list_to_string
    else:
        if "=" in line:
            assigned_content = line.split("=")[1].strip()
        elif line.strip().startswith("global ") or line.strip().startswith("nonlocal "):
            assigned_content = line.split(" ")[1].strip()
        start_index_of_declaration = index
        end_index_of_declaration = index
    return Declaration(variable_name, assigned_content, start_index_of_declaration, end_index_of_declaration)


def determine_what_other_it_is(line, index):
    """
    Determine what other it is based on the given line, codelist, and index.

    Args:
        line (str): The line of code to be analyzed.
        index (int): The index of the line in the code list.

    Returns:
        Other: An instance of the Other class with the determined description.

    """
    description = ""
    line= line.strip()
    if "print(" in line:
        description = "print"
    elif line.startswith("except") or line.startswith("finally") or line.startswith("raise"):
        description = "Part of an exception"
    elif ")" == line or "(" == line:
        description = "Parenthesis"
    elif "}" == line or "{" == line:
        description = "Curly brace"
    elif "]" == line or "[" == line:
        description = "Square bracket"
    elif '\"""' in line:
        description = "Docstring symbol or start of multiline string"
    elif line.endswith(","):
        description = "Part of list,tuple,dictionary or part of multiple variables in function declaration"
    elif line.endswith("):"):
        description  = "End of function declaration"
    elif any(x in line for x in { "+=", "-=", "*=", "/=", "//=", "%=", "**="}):
        description = "Arithmetic operation between variables"
    elif "." in line and (line.endswith(")") or line.endswith("(")) :
        description = "Function call"
    else:
        description = "Uncategorized, probable part of a comment or something else"
    return Other(description,index)
        
    