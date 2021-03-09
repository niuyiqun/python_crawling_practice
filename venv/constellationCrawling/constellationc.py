# -*- codeing = utf-8 -*-
# @Time : 2020/10/4 14:47
# @Author : niu
# @File : constellationc.py
# @Software: PyCharm

import csv
from bs4 import BeautifulSoup
import re
import os
import requests as r


baseUrl = "https://www.xzw.com/fortune/"

response=r.get(baseUrl).text
bs= BeautifulSoup(response,'lxml')
dls = bs.select('div.alb div dl')         #子标签之间直接加空格即可

savePath = os.path.join(os.getcwd(),'constellation.csv')

headers= ['星座','生日时间','运势评分','今日运势']
# print(dls[0].select('strong')[0].string)    #这样可以顺利拿到标签内的文字了
res = [headers]
data = []
for dl in dls:
    xingzuo=dl.select('strong')[0].string
    date=dl.select('small')[0].text
    yunshi=dl.select('em.star_m em')[0].get('style')
    # detials=dl.select('p')[0].text     这个还包括了子标签里面的文本内容
    details = dl.find('p').contents[0]
    yunshi_regex = re.compile("")
    data.append({'星座':xingzuo,'生日时间':date,'运势评分':yunshi,'今日运势':details})
    #到此，我们所有的数据均已经爬取下来了
    #之后只需要将其存储在CSV文件里即可

with open(savePath,'w',newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
