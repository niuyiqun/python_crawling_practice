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
base_url="https://www.biqukan.com"
url="https://www.biqukan.com/50_50096/"
headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    'Host' : "www.biqukan.com",
    }


def getUrl(chapter_url_list):    #获取了每个章节内容的网址
    req = urllib.request.Request(url, headers=headers)
    html = lxml.html.parse(urllib.request.urlopen(req))
    hrefs =html.xpath('//dd/a/@href')
    for href in hrefs:
        chapter_url_list.append(urllib.parse.urljoin(base_url,href))


def getContent(url): #获取每个章节的内容，传入的url参数是每个章节内容网页的网址
        request_novel = urllib.request.Request(url, headers=headers)
        html_novel = lxml.html.parse(urllib.request.urlopen(request_novel))
        novel_title = html_novel.xpath('//h1/text()')[0]
        content = html_novel.xpath('//*[@id="content"]/text()')
        novel_content=""
        for i in content:
            novel_content+=i.strip()
        saveData(novel_title,novel_content)


def saveData(name,content):
    try:
        with open("D:/python爬虫/myown/novel/"+name+'.txt',"w+") as f:
            f.write(content.strip())
    except(urllib.error.HTTPError,OSError) as reason:
        print(str(reason))
    else:
        print("下载完成："+name)


def main():
    getUrl(chapter_url_list)
    print("yes")
    for url in chapter_url_list:
        getContent(url)

if __name__ == '__main__':
    main()









