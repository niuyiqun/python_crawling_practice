# -*- codeing = utf-8 -*-
# @Time : 2020/10/4 11:21
# @Author : niu
# @File : testCSV.py
# @Software: PyCharm

import csv
import os
# from _csv import writer
# import cs

saveFileName1 = os.path.join(os.getcwd(),'1.csv')
saveFileName2 = os.path.join(os.getcwd(),'2.csv')
saveFileName3 = os.path.join(os.getcwd(),'3.csv')
data1=[
    ['id','性别','姓名','年龄','工作'],
    ['1','男','小米','15','学生'],
    ['2','男','华为','23','学生'],
    ['3','男','三星','25','学生'],
    ['4','男','苹果','36','学生']
]


# 用csv写入列表
# with open(saveFileName1,'w',newline='') as f:   #只写，会清除之前写的内容
#     writer=csv.writer(f)
#     for row in data1:
#         writer.writerow(row)          #单行写入
#
# with open(saveFileName2,'w',newline='')as f:       #newline参数避免在写入每一行后自动补全的一行
#     writer = csv.writer(f)
#     writer.writerows(data1)  # 多行写入

#用csv写入字典

headers = ['id','性别','姓名','年龄','工作']
data2 = [{'id':1,'性别':'男','姓名':'niu1','年龄':15,'工作':'工程hi四'},
         {'id':2,'性别':'男','姓名':'niu2','年龄':16,'工作':'工程hi四'},
         {'id':3,'性别':'男','姓名':'niu3','年龄':17,'工作':'工程hi四'},
         {'id':4,'性别':'男','姓名':'niu4','年龄':18,'工作':'工程hi四'}
        ]


# with open(saveFileName3,'w',newline='') as f:
#     writer=csv.DictWriter(f,headers)
#     writer.writeheader()
#     for row in data2:
#         writer.writerow(row)

#读取CSV文件
with open(saveFileName1)as f:
    # reader= csv.reader(f)
    # # print(list(reader))      #用list强制类型转换转换成list对象，然后再直接输出
    # for row in reader:
    #     print(reader.line_num,row)     #获取行号

    reader= csv.DictReader(f)
    for row in reader:
        print(reader.line_num,row['姓名'])
