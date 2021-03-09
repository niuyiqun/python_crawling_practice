# -*- codeing = utf-8 -*-
# @Time : 2020/11/1 18:31
# @Author : niu
# @File : testFakeuseragent.py
# @Software: PyCharm

from fake_useragent import UserAgent

# 实例化 UserAgent 类
ua = UserAgent()

# 对应浏览器的头部信息
print("ie:----",ua.ie)
print("opera:----",ua.opera)
print("chrome:----",ua.chrome)
print("firefox:----",ua.firefox)
print("safari:----",ua.safari)

# 随机返回头部信息，推荐使用
print(ua.random)
