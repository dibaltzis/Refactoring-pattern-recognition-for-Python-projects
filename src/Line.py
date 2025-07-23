class Line:
    def __init__(self,line_number,code,line_type):
        self.line_number=line_number
        self.editors_line_number= line_number+1
        self.code=code
        self.line_type=line_type
        
    def __getattr__(self, attr):
        return self.attr

    def __str__(self):
        return str(self.editors_line_number)+"->'"+self.code.strip()+"' -> "+self.line_type.name+ ("->Description : "+str(self.line_type.description) if self.line_type.name == "Other" else "")
   


class Conditional_:
    def __init__(self,start_index_of_if_expression, end_index_of_if_expression, if_content_start_index, if_content_end_index, conditional_expressions):
        self.name = "Conditional"
        self.start_index_of_if_expression = start_index_of_if_expression
        self.end_index_of_if_expression = end_index_of_if_expression
        self.if_content_start_index = if_content_start_index
        self.if_content_end_index = if_content_end_index
        self.conditional_expressions = conditional_expressions
        
    def __str__(self):
        return  ("\tThe type of the line is : %s \n\tIf expression start line : %d \n\tIf expression end line : %d \n\tIf content start line : %d \n\tIf content end line : %d \n\tConditional expressions : %s") % (self.name,self.start_index_of_if_expression,self.end_index_of_if_expression,self.if_content_start_index,self.if_content_end_index,self.conditional_expressions)


class Class_:
    def __init__(self,name_of_the_class,class_content_start_line,class_content_end_line,superclass_name):
        self.name = "Class"
        self.name_of_the_class = name_of_the_class
        self.class_content_start_line =class_content_start_line
        self.class_content_end_line = class_content_end_line
        self.superclass_name = superclass_name
           
    def __str__(self):
        string_to_put_in_return=""
        if self.superclass_name!= None:
            string_to_put_in_return = "Superclass name : %s \n\t"%self.superclass_name
        return ('\tThe type of the line is : %s \n\tName of the class : %s \n\t'+ string_to_put_in_return+'Startline : %d \n\tEndline : %d') % (self.name,self.name_of_the_class,self.class_content_start_line,self.class_content_end_line)

class Loop_:
    def __init__(self,start_index_of_the_loop,end_index_of_the_loop,start_index_of_loop_content,end_index_of_loop_content,loop_expression):
        self.name=  "Loop"
        self.start_index_of_the_loop = start_index_of_the_loop
        self.end_index_of_the_loop = end_index_of_the_loop
        self.start_index_of_loop_content = start_index_of_loop_content
        self.end_index_of_loop_content = end_index_of_loop_content
        self.loop_expression = loop_expression
        
    def __str__(self):
        return "\tThe type of the line is : %s \n\tStart_index_of_the_loop : %d \n\tEnd_index_of_the_loop : %d \n\tStart_index_of_loop_content : %d \n\tEnd_index_of_loop_content : %d \n\tLoop expression : %s" % (self.name,self.start_index_of_the_loop,self.end_index_of_the_loop,self.start_index_of_loop_content,self.end_index_of_loop_content,self.loop_expression)       


class Declaration:
    def __init__(self,variable_name, assigned_content,start_index_of_declaration,end_index_of_declaration):
        self.name=  "Declaration"
        self.variable_name= variable_name
        self.assigned_content = assigned_content
        self.start_index_of_declaration = start_index_of_declaration
        self.end_index_of_declaration = end_index_of_declaration
        
    def __str__(self):
        return "\tThe type of the line is : %s \n\tVariable name : %s \n\tAssigned content : %s \n\tStart_index_of_declaration : %d \n\tEnd_index_of_declaration : %d" % (self.name,self.variable_name,self.assigned_content,self.start_index_of_declaration,self.end_index_of_declaration)

class Other:
    def __init__(self,description,index_of_line):
        self.name= "Other"
        self.description= description
        self.index_of_line = index_of_line
    def __str__(self):
        return "\tThe type of the line is : %s \n\tDescription : %s" % (self.name,  self.description)
    
class Import_:
    def __init__(self):
        self.name = "Import"
    def __str__(self):
        return "\tThe type of the line is : %s \n" % (self.name)

    
class Comment:
    def __init__(self,start_index_of_comment,end_index_of_comment,content_of_the_comment):
        self.name = "Comment"
        self.start_index_of_comment = start_index_of_comment
        self.end_index_of_comment = end_index_of_comment
        self.content_of_the_comment = content_of_the_comment
        
    def __str__(self):
        return "\tThe type of the line is : %s \n\tStart_index_of_comment : %d \n\tEnd_index_of_comment : %d \n\tContent_of_the_comment : %s" % (self.name,self.start_index_of_comment,self.end_index_of_comment,self.content_of_the_comment)

class Blank:
    def __init__(self):
        self.name= "Blank"
    def __str__(self):
        return "\tThe type of the line is : %s line\n" % (self.name)
 
class Return_:
    def __init__(self,content_of_the_return,start_index_of_return,end_index_of_return):
        self.name=  "Return"
        self.start_index_of_return = start_index_of_return
        self.end_index_of_return = end_index_of_return
        self.content_of_the_return = content_of_the_return
    def __str__(self):
        return "\tThe type of the line is : %s \n\tContent of the return : %s" % (self.name,self.content_of_the_return)

    
class Assertion_:
    def __init__(self,start_index_of_the_assertion, end_index_of_the_assertion, assertion_content):
        self.name=  "Assertion"
        self.start_index_of_the_assertion = start_index_of_the_assertion
        self.end_index_of_the_assertion = end_index_of_the_assertion
        self.assertion_content = assertion_content
        
    def __str__(self):
        return "\tThe type of the line is : %s \n\tStart_index_of_the_assertion : %d \n\tEnd_index_of_the_assertion : %d \n\tAssertion content : \n' %s '" % (self.name,self.start_index_of_the_assertion,self.end_index_of_the_assertion,self.assertion_content)

class Function_:
    def __init__(self,function_name,function_parameters,start_index_of_the_declaration,end_index_of_the_declaration,start_index_of_function_content,end_index_of_function_content):
        self.name=  "Function"
        self.function_name = function_name
        self.function_parameters = function_parameters
        self.start_index_of_the_declaration = start_index_of_the_declaration
        self.end_index_of_the_declaration = end_index_of_the_declaration
        self.start_index_of_function_content = start_index_of_function_content
        self.end_index_of_function_content = end_index_of_function_content

    def __str__(self):
        return "\tThe type of the line is : %s \n\tFunction name : %s\n\tFunction parameters %s \n\tStart_index_of_the_declaration : %d\n\tEnd_index_of_the_declaration : %d\n\tStart_index_of_function_content : %d\n\tEnd_index_of_function_content : %d\n\t" % (self.name,self.function_name,self.function_parameters,self.start_index_of_the_declaration,self.end_index_of_the_declaration,self.start_index_of_function_content,self.end_index_of_function_content)
    
    
class Exception_:
    def __init__(self,start_index_of_exception,end_index_of_exception,start_index_of_except,end_index_of_except,start_index_of_finally,end_index_of_finally,start_index_of_else,end_index_of_else):
        self.name=  "Exception"
        self.start_index_of_exception  = start_index_of_exception
        self.end_index_of_exception = end_index_of_exception
        self.start_index_of_except = start_index_of_except
        self.end_index_of_except = end_index_of_except
        self.start_index_of_finally = start_index_of_finally
        self.end_index_of_finally = end_index_of_finally
        self.start_index_of_else = start_index_of_else
        self.end_index_of_else = end_index_of_else
        
    def __str__(self):
        string_to_put_in_return = ""
        exception_start_end ="\tstart_index_of_exception: %d  \tend_index_of_exception: %d"%(self.start_index_of_exception,self.end_index_of_exception)
        except_start_end = "\tstart_index_of_except: %d  \tnd_index_of_except: %d"%(self.start_index_of_except,self.end_index_of_except)
        string_to_put_in_return = string_to_put_in_return + exception_start_end
        string_to_put_in_return = string_to_put_in_return +"\n"+ except_start_end
        if self.end_index_of_finally is not None:
            finally_start_end = "\tstart_index_of_finally: %d  \tend_index_of_finally: %d"%(self.start_index_of_finally,self.end_index_of_finally)
            string_to_put_in_return = string_to_put_in_return +"\n"+ finally_start_end
        if self.end_index_of_else is not None:
            else_start_end = "\tstart_index_of_else: %d  \tend_index_of_else: %d"%(self.start_index_of_else,self.end_index_of_else)
            string_to_put_in_return = string_to_put_in_return +"\n"+ else_start_end
            
        return "\tThe type of the line is : %s \n%s" % (self.name,string_to_put_in_return)