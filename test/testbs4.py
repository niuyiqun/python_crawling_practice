# -*- codeing = utf-8 -*-
# @Time : 2020/9/26 19:03
# @Author : niu
# @File : testbs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import os

baseUrl = "http://www.win4000.com/wallpaper_detail_174092_1.html"

resp=requests.get(baseUrl).text
bs = BeautifulSoup(resp,"lxml")
a=bs.select('img.pic-large')
print(a[0].get("src"))
print(a[0].get("title"))

# with open ("a.png","wb") as f:
#     f.write(requests.get(a[0].get("src")).content)
# os.mkdir(os.getcwd()+"\\tmp")