import xlwings as xw
import sheets_compare as sc
import overview as ov

# 旧版本路径
compared_version_path = "./05_Excel_compare/version_1.xlsx"
#新版本路径
review_version_path = "./05_Excel_compare/version_2.xlsx"

book_c = xw.Book(compared_version_path)
book_r = xw.Book(review_version_path)

ov.build(book_r)
ov.build(book_c)
Pn_r_list = ov.get_PN_list(book_r)
Pn_c_list = ov.get_PN_list(book_c)

len = max(len(Pn_c_list),len(Pn_r_list))
i = 0

for PN_r in Pn_r_list:
    if Pn_c_list.count(PN_r):
        #检查表内差异
        print("%s 差异如下："%PN_r)
        sc.sheets_compare(book_c.sheets[PN_r],book_r.sheets[PN_r])
    else:
        #Pn_c删除， Pn_r新增
        print("新增/修改零件：%s" % PN_r)
        # sc.sheets_compare(book_c.sheets["Overview"],book_r.sheets["Overview"])