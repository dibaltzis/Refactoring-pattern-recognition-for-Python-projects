import xlsxwriter
from File import File
from pathlib import Path
import minify_html
import config
import os

#creates Excel output to file Refactors.xlsx
#the Refactors variable is a list of refactor objects
def create_excel_output(Refactors,export_folder_path,project_name=None):
  
    filename = f"{('['+project_name+']') if project_name!=None else ''}Refactors.xlsx"
    workbook = xlsxwriter.Workbook(export_folder_path / filename)
    worksheet = workbook.add_worksheet()
    data=[]
    #for refactor in Refactors:
    projectName = project_name
    for refactor in sorted(Refactors, key=lambda x: x.name):
        link = str( Path("html_files") / Path(refactor.name.replace(" ","_").replace("/","_")+"_id_"+str(id(refactor))+".html"))
        link_cell = f'=HYPERLINK("{link}", "→")'
        if project_name!=None:
          if project_name.count("_") == 1:
            project_link = "https://github.com/"+project_name.split("_")[0]+"/"+project_name.split("_")[1]
            projectName = f'=HYPERLINK("{project_link}", "{project_name}")'
          else:
            projectName = project_name
        projectName = projectName if projectName!=None else '-' 
        data.append([refactor.name,refactor.sub_name,projectName,refactor.version1_name,refactor.version2_name,link_cell,refactor.file1,refactor.file2,refactor.f1_startline,refactor.f1_endline,refactor.f2_startline,refactor.f2_endline])
    # Set the columns widths.
    centered_format = workbook.add_format({'align': 'center'})
    worksheet.set_column('A:A',45)
    worksheet.set_column('B:B',32)
    worksheet.set_column('C:C',15, centered_format)
    worksheet.set_column('D:E',10, centered_format)
    worksheet.set_column('F:F',25, centered_format)
    worksheet.set_column('G:H',45)
    worksheet.set_column('I:L',12, centered_format)
    
    table_size_cells = "A1:L"+str(len(data)+1)
    # Add a table to the worksheet.
    worksheet.add_table(table_size_cells, {'data': data,
                            'autofilter': False,
                            'style': 'Table Style Medium 9',
                            'header_row': True,
                                'columns': [{'header': 'Refactor name'},
                                            {'header': 'Category'},
                                            {'header': 'Project name'},
                                            {'header': 'version 1'},
                                            {'header': 'version 2'},
                                            {'header': 'Link to html comparison file'},
                                            {'header': 'File 1 Path'},
                                            {'header': 'File 2 Path'},
                                            {'header': 'File 1 start line'},
                                            {'header': 'File 1 end line'},
                                            {'header': 'File 2 start line'},
                                            {'header': 'File 2 end line'},
                                            ]})
    workbook.close()   

#creates the main html file Refactors_Tree.html
def create_html_tree(folder_path,refactors_html_table,directory1=None,directory2=None,project_name=None,releases=None):
    if directory1 != None and directory2 != None:
      description= "<h1>Comparing : <span style='color: #ffffff'>"+directory1.name+("</span> and <span style='color: #ffffff'>")+directory2.name+"</span></h1>"
    elif project_name != None and releases != None:
      releases_list_string = "<span style='color: #ffffff'>"+str(", ".join(releases))+"</span>"     
      description="<h1>Project name : <span style='color: #ffffff'>"+ project_name+ "</span></h1> \
        <h2> Comparing  <span style='color: #ffffff'>"+str(len(releases))+"</span> releases</h2>"+ \
        "<h3>Releases : "+releases_list_string+"</h3>"
    else:
      description=""
      
    first_part = """
    <!DOCTYPE html>
<html>
<style>
       body {
        background-color: #2c2e34 ;
      }
    h1 {
        font-size: 25px;
        color:#7491e8;
        text-align: center;
      }
    h2 {
        font-size: 20px;
        color:#7491e8;
        text-align: center;
      }
    h3 {
        font-size: 18px;
        color:#7491e8;
        text-align: center;
      }
      a:before {
    content:"• ";
    }
    a {
  outline: none;
  text-decoration: none;
  padding: 2px 1px 0;
  color:#ffffff;
  text-align: center;
}
table.Mytable {
  border: 1px solid #7491E8;
  background-color: #2C2E34;

  margin-left: auto;
  margin-right: auto;
}
table.Mytable td, table.Mytable th {
  border: 0.1px solid #FFFFFF;
}
table.Mytable tbody td {
  font-size: 18px;
  color: #FFFFFF;
}
table.Mytable thead {
  background: #7491E8;
  background: -moz-linear-gradient(top, #97acee 0%, #829cea 66%, #7491E8 100%);
  background: -webkit-linear-gradient(top, #97acee 0%, #829cea 66%, #7491E8 100%);
  background: linear-gradient(to bottom, #97acee 0%, #829cea 66%, #7491E8 100%);
}
table.Mytable thead th {
  font-size:25px;
  font-weight: bold;
  color: #FFFFFF;
  border-left: 1px solid #D0E4F5;
}
</style>      
<body>

"""+description+"""
"""+refactors_html_table+"""
"""

    third_part="""

</body>
</html>
    """
    to_write_string = first_part
    to_write_string =to_write_string +third_part
    name = f"{('['+project_name+']') if project_name!=None else ''}Refactors_Tree.html"
    foutput = open(folder_path / name,'w',encoding="utf-8")
    foutput.writelines(str(to_write_string))
    foutput.close()

def create_html_per_refactor(file1,file2,name1,name2,Diffblocks,output_folder_path):#,project_name=None):
    
    blank_space = "&nbsp;"
    def first_part(filename1,filename2,project_name):
            in_title =str(project_name if project_name != None else "")
            return  """
        <head>
        <title>"""+in_title+""" Refactors</title>
    <style>
        body {
            background-color: #2c2e34 ;
        }
        table {
            border-collapse: collapse;
            background-color:#4f4f58 ;
            border-spacing: 10px;
            width: 100%;
        }
        th {
            border: 2px solid #1F1F1E;
            text-align: center;
            padding: 18px;
            font-size: 20px;
            color:#7491e8;
        }
        .inside_table
        {  
            background-color:#1F1F1E;
        } 
        .code {
            font-family: Consolas, 'Courier New', monospace;
            color:#ffffff;
            font-size: 16px;
        }
        .line_number {
            color: #848485;
        }
        .refactor {
            font-family: Consolas, 'Courier New', monospace;
            vertical-align: middle;
            text-align: left;
            color:red;
            background-color: #1F1F1F;
            border: 2px solid #4f4f58;
            
        }
        .block {
            vertical-align: top;
        }
        .Add {
            background-color:#aaffaa70;

        }
        .Sub {
            background-color:#ffaaaa73
        }
        .None {
            background-color:#1F1F1E;
        }
        </style>
    </head>
    <body>
        <table>
            <tr>
            <th>"""+filename1+"""</th>
            <th>"""+filename2+"""</th>
            <th>Refactors</th>
            </tr> 
            
        """  
    table_start ="""
            <td>
                    <table class="inside_table">
        """
    def line_code(line_number,content,line_above=None,line_bellow=None):
            to_return ="""
            <tr class="code">
                <td nowrap="nowrap">
                    """
            if line_above != None:
                to_return+= """<hr style="height:2px;border-width:0;background-color:"""+line_above+"""">"""
            to_return+="""<span class="line_number">"""+str(line_number)+"""</span>"""
            to_return+="""<span class='None'>&nbsp;"""+str(content.replace(" ",blank_space))+"""</span>"""
            if line_bellow != None:
                to_return+= """<hr style="height:2px;border-width:0;background-color:"""+line_bellow+"""">"""
            to_return +="""</td> 
            </tr>
            """
            return to_return
    table_end ="""
    </table>
            </td>
    """
    end= """
    </tr>
    </table>
  </body>
</html>
</body>

</html>
    """
    for b in Diffblocks:
        for refactor in b.refactors:
            to_write_string = first_part(name1,name2,refactor.name.replace(" ","_").replace("/","_")+"_id_"+str(id(refactor)))
            to_write_string +=table_start
            f1_blank_list = Get_blanks_from_diffblock(Diffblocks,1)
            for l in file1.Lines:
                line_above =None
                line_bellow=None
                if type(refactor.f1_startline) is int:
                    if refactor.f1_startline-1 ==  l.line_number:
                                line_above = refactor
                if type(refactor.f1_endline) is int:
                    if refactor.f1_endline-1 ==  l.line_number:
                                line_bellow =refactor
                to_write_string += line_code(l.editors_line_number,l.code,line_above.color if line_above!=None else None,line_bellow.color if line_bellow!=None else None)            
                for blank in f1_blank_list:
                    if l.line_number == blank[0]:
                        to_write_string += line_code(blank_space, blank_space) * blank[1]
            to_write_string += table_end
            to_write_string +=table_start
            f2_blank_list = Get_blanks_from_diffblock(Diffblocks,2)
            for l in file2.Lines:
                line_above =None
                line_bellow=None
                if type(refactor.f2_startline) is int:
                    if refactor.f2_startline-1 ==  l.line_number:
                        line_above = refactor
                if type(refactor.f2_endline) is int:
                    if refactor.f2_endline-1 ==  l.line_number:
                        line_bellow =refactor

                to_write_string += line_code(l.editors_line_number,l.code,line_above.color if line_above!=None else None,line_bellow.color if line_bellow!=None else None)           
                for blank in f2_blank_list:
                    if l.line_number == blank[0]:
                        to_write_string += line_code(blank_space, blank_space) * blank[1]
            to_write_string += table_end
            to_write_string +=table_start
            for l in file1.Lines:
                line_above =None
                line_bellow=None
                if type(refactor.f1_startline) is int:
                    if refactor.f1_startline-1 ==  l.line_number:
                                line_above = refactor
                if type(refactor.f1_endline) is int:
                    if refactor.f1_endline-1 ==  l.line_number:
                                line_bellow =refactor

                if line_above!=None:
                    content = line_above.name+"&nbsp; : <br><br>"+line_above.extra.replace("\n","<br>") if line_above.extra!= None else line_above.name
                    to_write_string += line_code(blank_space,content,line_above.color,line_bellow.color if line_bellow!=None else None)
                else:
                    to_write_string += line_code(blank_space,blank_space,line_above.color if line_above!=None else None,line_bellow.color if line_bellow!=None else None)            
                for blank in f1_blank_list:
                    if l.line_number == blank[0]:
                        to_write_string += line_code(blank_space, blank_space) * blank[1]
                
            to_write_string += table_end
            to_write_string +=end
            filename = output_folder_path / Path(refactor.name.replace(" ","_").replace("/","_")+"_id_"+str(id(refactor))+".html")
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            foutput = open(filename,'w',encoding="utf-8")
            if config.MINIFY_HTML_BOOL:
                to_write_string = str(minify_html.minify(str(to_write_string), minify_js=True, remove_processing_instructions=True))
            foutput.writelines(str(to_write_string))
            foutput.close()


def Get_blanks_from_diffblock(Diffblocks,i):
        flag =True
        list_=[]
        for b in Diffblocks:
            if i == 1:
                lines_list =b.f1_lines_list
            elif i==2:
                lines_list =b.f2_lines_list
            count=0
            line_number =0
            for l in lines_list:
                if l.line != "":
                    flag = True
                    line_number = l.line.line_number
                    count=0
                else :
                    flag = False
                    count+=1
                if not flag:
                    if len( list_)>0:
                        if  list_[-1][0]==line_number and list_[-1][1] <count:
                            del  list_[-1]
                    list_.append([line_number,count])
        return list_
