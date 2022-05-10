import xlwings as xw
import sheet as sh

# 定义检查sheet_review 相对于 sheet_compare的变化点, 并返回变化日志列表
def sheets_compare(sheet_compare,sheet_review):
    # 获取表格标题长度、内容
    title_len = max(sh.get_row_len(sheet_compare,1),sh.get_row_len(sheet_review,1))
    title_list = sh.get_row_list(sheet_review,1)
    
    # 检查序号是否正确
    sh.check_order(sheet_compare)
    sh.check_order(sheet_review)
    
    rows_qty_1 = sh.get_column_len(sheet_compare,1)
    rows_qty_2 = sh.get_column_len(sheet_review,1)
    
    
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
    
    return change_logs

if __name__ == "__main__":
    sheets_compare(xw.Book("./05_Excel_compare/version_1.xlsx").sheets[1], xw.Book(
        "./05_Excel_compare/version_2.xlsx").sheets[1])