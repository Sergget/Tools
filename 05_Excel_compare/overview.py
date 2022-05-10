import sheet as sh
import sys

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
    # 零件表格标题列表
    PL_title_list = ["序号","中文名称","代码","规格","材料","供应商","数量","备注"]
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

if __name__ == "__main__":
    # print(sys.argv)
    if sys.argv[1] =="--build" or sys.argv[1] =="-b":
        # build本目录下所有xlsx文件
        print("Building...")