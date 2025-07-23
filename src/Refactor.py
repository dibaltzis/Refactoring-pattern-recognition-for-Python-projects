class Refactor:
    def __init__(self, refactor_name,file1_path,file2_path,version1_name,version2_name, f1_startline,f1_endline,f2_startline,f2_endline,color,subname=None,extra =None):
        self.name = refactor_name
        self.color = color#self.refactor_color()
        self.sub_name = subname
        self.file1 = file1_path
        self.file2 = file2_path
        self.extra = extra
        self.version1_name = version1_name
        self.version2_name = version2_name
        if type(f1_startline) is int:
             self.f1_startline = f1_startline+1
        else:
            self.f1_startline = f1_startline
        if  type(f1_endline) is int:
            self.f1_endline = f1_endline+1
        else:
            self.f1_endline = f1_endline
        if  type(f2_startline) is int:
            self.f2_startline = f2_startline+1
        else:
            self.f2_startline = f2_startline
        if  type(f2_endline) is int:
            self.f2_endline = f2_endline+1
        else:
            self.f2_endline = f2_endline

        
    def __getattr__(self, attr):
        return self.attr

    def __str__(self) -> str:
        return self.name+" " +self.sub_name
