# -*- codeing = utf-8 -*-
# @Time : 2020/9/23 18:15
# @Author : niu
# @File : qinyuniancrawling.py
# @Software: PyCharm

import urllib.request
import urllib.error
import lxml.html
import urllib.parse

url="https://read.qidian.com/chapter/kpwCq4fKJk01/LGKHGy9k73Q1"
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'referer': 'https://book.qidian.com/info/114559'
}
request =urllib.request.Request(url,headers=headers)
html = lxml.html.parse(urllib.request.urlopen(request))
# content = html.xpath('//p')
content = html.xpath('//div[@class="read-content j_readContent"]/p/span[@class="content-wrap"]/text()')
    #为什么这里获取不了文本呜呜呜
    #以后用靓汤来试试
    #历史遗留问题


# content = html.xpath('//*[@id="chapter-2987319"]/div/div[2]/p[1]/span[1]/text()')
print(content)