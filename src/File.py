from Line import Line
from util.Line_utilities import Line_type_separation
class File:
    def __init__(self,file_path):
        self.file_path = file_path
        self.code_list = self.__file_to_list()
        self.code_length = len(self.code_list)
        self.Lines = []
        self.init_lines()
    #initialize lines 
    def init_lines(self):
        index_of_line_comment_to_skip= -1
        for index,l in enumerate(self.code_list):
            line_type_object, index_of_line_comment_to_skip = Line_type_separation(l,self.code_list,index, index_of_line_comment_to_skip)
            self.Lines.append(Line(index,l,line_type_object))

    def __getattr__(self, attr):
        return self.attr
    
    #reads the file and returns its contents to a list - from the file path
    def __file_to_list(self):
            code = open(self.file_path, "r", encoding='utf-8',errors="ignore")
            code_list =  code.readlines()
            code.close()
            return code_list
    
    def __str__(self):
        return "\n".join(str(line) for line in self.Lines)