# -*- codeing = utf-8 -*-
# @Time : 2020/9/20 18:43
# @Author : niu
# @File : testUrllib.py
# @Software: PyCharm


import urllib.request
from http.client import HTTPResponse

response= urllib.request.urlopen("http://www.baidu.com")   #返回的是一个HTTPResponse对象
# print(response)
# print(response.read().decode("utf-8"))
# print(response.geturl())
# print(dir(HTTPResponse))

#这个可以用来下载图片hhh
#抓取二进制文件
res=urllib.request.urlopen("http://img.netbian.com/file/newc/c8e0fd544aeeee62d1efe23d229efe4c.jpg")
print(type(res))
# pic=res.read()
# with open ("papercut.png","wb") as f:
#     f.write(pic)


