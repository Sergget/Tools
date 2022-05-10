import xlwings as xw

class OrderError(IndexError):
    def __init__(self, sheet, line_number):
        self.sheet = sheet
        self.line_number = line_number
    def __str__(self):
        return repr("工作簿%s 表格%s, 序号错误：第%d行,应为%d" %(self.sheet.book.name,self.sheet.name,self.line_number,self.line_number-1))

# 获得某行左侧连续的的长度
def get_row_len(sheet, row):
    i = 0
    while sheet.range(row, i+1).value != None:
        i += 1
    return i

# 将某行左侧连续值作为一个列表返回，含首列序号列
def get_row_list(sheet, row):
    return sheet.range((row, 1), (row, get_row_len(sheet, row))).value

################
# 获得某列连续的的长度，含首行标题
def get_column_len(sheet, column):
    i = 0
    while sheet.range(i+1,column).value != None:
        i += 1
    return i

# 将某列上方连续的值作为一个列表返回，含首行标题
def get_column_list(sheet, column):
    return sheet.range((1,column), (get_column_len(sheet, column),column)).value

# 在第一列检查序号直至出现空值,返回序号的数量
def check_order(sheet,column=1):
    count = 1
    len = get_column_len(sheet,column)
    content_list = sheet.range((2,column), (len,column)).value
    while count<len:
        if count == content_list[count-1]:
            pass
        else:
            raise OrderError(sheet,count+1)
        count += 1

# 定义检查sheet_review 相对于 sheet_compare的变化点, 并返回变化日志列表
def sheets_compare(sheet_compare,sheet_review):
    # 获取表格标题长度、内容
    title_len = max(get_row_len(sheet_compare,1),get_row_len(sheet_review,1))
    title_list = get_row_list(sheet_review,1)
    
    # 检查序号是否正确
    check_order(sheet_compare)
    check_order(sheet_review)
    
    rows_qty_1 = get_column_len(sheet_compare,1)
    rows_qty_2 = get_column_len(sheet_review,1)
    
    
    # 2个表格的最大行数
    rows_r = max(rows_qty_1, rows_qty_2)

    #日志列表
    change_logs = []
    change_logs_titles=["序号","中文名称","变更前","变更后","变更时间"]

    # 清空表格内所有格式
    sheet_review.clear_formats()
    # 清空内容对应右侧区域内的内容和格式
    sheet_review.range((1,title_len+2),(rows_r,title_len+len(change_logs_titles))).clear()

    # 进行行检查
    # 内容行起始行号
    row = 2
    while row <= rows_r:
        
        # 获得本行内容，注意这里不能使用sheet模块中的get_row_list方法，该方法只能获得行内的连续非空内容
        row_1 = sheet_compare.range((row,1),(row,title_len)).value
        row_2 = sheet_review.range((row,1),(row,title_len)).value
        if row_1 == row_2:
            pass
        else:
            name_zh_index = title_list.index("中文名称")
            if row_1[name_zh_index]==None:
                change_logs.append([row-1,"新增 "+row_2[name_zh_index]])
            elif row_2[name_zh_index]==None:
                change_logs.append([row-1,"删除 "+row_1[name_zh_index]])
            else:
                # 进行单元格检查
                column = 2
                while column <= title_len:
                    value_1 = row_1[column-1]
                    value_2 = row_2[column-1]
                    if value_1 == value_2:
                        pass
                    else:
                        name_zh = row_2[title_list.index("中文名称")]
                        sheet_review.range(row,column).font.color=(255,0,0)
                        change_logs.append([row-1,name_zh,value_1,value_2])
                    column+=1
        row = row+1

    if change_logs!=[]:
        sheet_review.range(1,title_len+2).value = "变化点："
        sheet_review.range(2,title_len+2).value = change_logs_titles
        log_start = 3
        for log in change_logs:
            sheet_review.range(log_start,title_len+2).value = log
            log_start+=1

if __name__ == "__main__":
    sheet = xw.Book("./05_Excel_compare/version_1.xlsx").sheets[1]
    check_order(sheet)
    sheets_compare(xw.Book("./05_Excel_compare/version_1.xlsx").sheets[1], xw.Book("./05_Excel_compare/version_2.xlsx").sheets[1])