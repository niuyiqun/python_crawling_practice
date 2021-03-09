# -*- codeing = utf-8 -*-
# @Time : 2020/9/22 21:02
# @Author : niu
# @File : novel_crawling.py
# @Software: PyCharm

import urllib.request
import urllib.error
import lxml.html
import urllib.parse


# res = urllib.request.urlopen("https://www.biqukan.com/50_50096/")
from lxml.doctestcompare import strip

chapter_url_list=[]
novel_content_list =""
base_url="https://www.biqukan.com"
url="https://www.biqukan.com/50_50096/"
headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    'Host' : "www.biqukan.com",
    }
req = urllib.request.Request(url,headers=headers)
#该方法无法获取页面内容-->页面经过gzip目前不知道如何读取

#
# response = urllib.request.urlopen(req)
# html = ""
# response = urllib.request.urlopen(req, timeout=10)
# html=response.read().decode("utf-8")
# print(html)


html = lxml.html.parse(urllib.request.urlopen(req))
hrefs =html.xpath('//dd/a/@href')

for href in hrefs:
    chapter_url_list.append(urllib.parse.urljoin(base_url,href))
# print(chapter_url_list)

for i in chapter_url_list:
    request_novel=urllib.request.Request(i,headers=headers)
    html_novel=lxml.html.parse(urllib.request.urlopen(request_novel))
    novel_content=html_novel.xpath('//*[@id="content"]/text()')
    print("获取的内容")
    print(novel_content)
    # novel_content_list+=strip(novel_content)
    break

# print(novel_content_list)
print("执行完毕")



# print(html)






