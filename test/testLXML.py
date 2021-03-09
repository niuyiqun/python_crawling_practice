# -*- codeing = utf-8 -*-
# @Time : 2020/10/11 20:10
# @Author : niu
# @File : testLXML.py
# @Software: PyCharm

import xlwt
import xlrd
import os
if __name__ == '__main__':
    # workbook=xlwt.Workbook()
    # sheet=workbook.add_sheet('工作表1',cell_overwrite_ok=True)
    # sheet.write(0,0,"姓名")
    # sheet.write(1,0,"小猪")
    # sheet.write(1,1,"1")
    # workbook.save(os.path.join(os.getcwd(),"result.xls"))

    workbook=xlrd.open_workbook(os.path.join(os.getcwd(),"result.xls"))     #打开文件
    sheet=workbook.sheets()[0]        #拿到表1
    rows=sheet.nrows        #获取行数
    for row in range(0,rows):       #以行为单位获取内容
        print(sheet.row_values(row))
