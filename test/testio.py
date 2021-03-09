# -*- codeing = utf-8 -*-
# @Time : 2020/9/25 16:45
# @Author : niu
# @File : testio.py
# @Software: PyCharm

import os     #文件写入输出
# f = open("a.txt","wb")    #wb模式一般用于非文本文件如图片等等
# f.write("bytes('a')")
#a模式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# os.mkdir("wuwuwu")
os.chdir("wuwuwu")
path = os.getcwd()
with open(path+"\\aa.txt","a")as f:
    f.write("\nniuyq")