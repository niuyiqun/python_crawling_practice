# -*- codeing = utf-8 -*-
# @Time : 2020/9/22 22:45
# @Author : niu
# @File : douban_crawling.py
# @Software: PyCharm

import urllib.request
import urllib.error
import lxml.html

url = "https://movie.douban.com/top250?start="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
req=urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
html = lxml.html.parse(response)
href_list=[]
# hrefs = html.xpath('//div[@class="item"]/div[@class="pic"]/a/@href')
hrefs = html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/@href')   #chrome自动copy的xpath---只能获取一个，不能全局获取
# for item in hrefs:
#     href_list.append(item)
# print(href_list)
print(hrefs)
# print(html.read().decode("utf-8"))


