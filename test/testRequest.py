# -*- codeing = utf-8 -*-
# @Time : 2020/9/23 19:21
# @Author : niu
# @File : testRequest.py
# @Software: PyCharm

import requests
import urllib.request
from lxml import html

r1=requests.get("http://www.baidu.com",params={"a":1,"b":2}).text

# r2=requests.get("http://www.baidu.com",params={"a":1,"b":2}).text

# print(r1.url)
# print(r1.reason)
# print(r1.status_code)
# print(r1.json())
# for key,value in r1.headers.items():
#     print(key +"="+ value)
# r2=urllib.request.urlopen("http://www.baidu.com")
et=html.etree
r2=et.HTML(r1)

print(r1)
print("---------------------------------")
print(r2)
# print(r2.read().decode("utf-8"))