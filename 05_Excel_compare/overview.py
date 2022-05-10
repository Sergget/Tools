import sheet as sh
import xlwings as xw
import os

# 零件表格标题列表
PL_title_list = ["序号","中文名称","代码","规格","材料","R","供应商","数量","备注"]

# 返回零件号列表
def get_PN_list(book):
    sheet_o = book.sheets["Overview"]
    title_list = sh.get_row_list(sheet_o,1) 
    # 零件号所在的列号
    part_number_column = title_list.index("零件号")+1

    # 零件号列表
    part_number_list = sh.get_column_list(sheet_o,part_number_column)[1:]

    return part_number_list

def build(book):
    # 检查现有的sheet列表
    sheets_name_list = []
    for sheet in book.sheets:
        sheets_name_list.append(sheet.name)
    PN_list = get_PN_list(book)
    PN_list.reverse()
            
    for PN in PN_list:
        if sheets_name_list.count(PN) == 0:
            book.sheets.add(PN)
            book.sheets[PN].range(1,1).value = PL_title_list

# 汇总各零件内的子零件类型数量
def get_PN_componets(book):
    components_type = ["类型1","类型2","类型3"]
    
    name_col = PL_title_list.index("中文名称")+1
    qty_col = PL_title_list.index("数量")+1

    PN_list = get_PN_list(book)

    components_dict = dict.fromkeys(components_type,0)

    for PN in PN_list:
        current_sheet = book.sheets[PN]
        no = sh.get_column_len(current_sheet,1)
        
        components_names = current_sheet.range((2,name_col),(no,name_col)).value
        components_qty = current_sheet.range((2,qty_col),(no,qty_col)).value
        i = 0
        length = len(components_names)
        while i<length:
            for type in components_type:
                if components_names[i] != None and components_names[i].find(type) != -1:
                    components_dict[type]+=components_qty[i]
            i+=1
    return components_dict

if __name__ == "__main__":
    files = os.listdir(".")
    for filename in files:
        if filename[0:2]!="~$" and filename.endswith(".xlsx"):
            build(xw.Book(filename))
            print("%s中组件概况：%s" % (filename,get_PN_componets(xw.Book(filename))))