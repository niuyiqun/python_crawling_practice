# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 17:32
# @Author : niu
# @File : testre.py
# @Software: PyCharm


import re
#简单验证手机号码格式

# phone_number_regex = re.compile("^(13\d{9}|14[579]\d{8}|15\d{9}|17[01678]\d{8}|18\d{9})$")
# print(phone_number_regex.search("15170020077"))
# print(phone_number_regex.search("15779331208"))
# print(phone_number_regex.search("15170387252"))

a="<img src='ssssss'"
regex=re.compile("<img src='(.*?)?'")
print("图片地址",regex.findall(a))

