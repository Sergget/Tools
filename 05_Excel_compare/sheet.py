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

if __name__ == "__main__":
    sheet = xw.Book("./05_Excel_compare/version_1.xlsx").sheets[1]
    check_order(sheet)
    print(get_column_len(sheet,1))
    print(get_row_len(sheet,1))