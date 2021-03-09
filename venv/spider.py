# -*- codeing = utf-8 -*-
# @Time : 2020/9/20 16:15
# @Author : niu
# @File : spider.py
# @Software: PyCharm


import urllib.request,urllib.robotparser

res=urllib.request.urlopen("http://localhost:8080/login")
print(res.read().decode("utf-8"))
# rp=urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.taobao.com/robots.txt")
# rp.read()  #该步骤无返回结果,但是必须要调用
# url="http://www.taobao.com/robots.txt"
# user_agent="Baiduspider"
# print(rp.can_fetch(user_agent,url))