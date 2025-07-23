class DiffBlock:
    def __init__(self,f1_list,f2_list):
        self.f1_lines_list=f1_list
        self.f2_lines_list=f2_list
        self.refactors= []

    def set_refactors(self,Refactor):
        self.refactors.append(Refactor)

    def __getattr__(self, attr):
        return self.attr

    def __str__(self):
        return " ".join(str(l) for l in self.f1_lines_list)+"\n"+" ".join(str(l) for l in self.f2_lines_list)
class BlockLine:
    def __init__(self,type,line):
        self.type= type
        self.line = line
        
    def __str__(self):
        return "line : "+str(self.line)+" type : "+str(self.type)
    