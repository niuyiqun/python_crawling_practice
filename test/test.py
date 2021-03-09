# -*- codeing = utf-8 -*-
# @Time : 2021/3/7 15:30
# @Author : niu
# @File : test.py
# @Software: PyCharm


def fact(n):
    s = 1;
    for i in range(1,n+1):
        s *= i;
    return s;


print("program begin")
result = fact(10)
print(result)
