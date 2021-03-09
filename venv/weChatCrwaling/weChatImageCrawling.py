# -*- codeing = utf-8 -*-
# @Time : 2020/9/23 20:34
# @Author : niu
# @File : weChatImageCrawling.py
# @Software: PyCharm
import urllib

import requests
from lxml import html




def getTitle(url,headers):       #拿到文章标题并实行接下去的方法
    response = requests.get(url, headers=headers).text  # 是转化成unicode型数据,可以被表示bs4和lxml解析#  .content返回的是二进制文件
    et = html.etree
    htm = et.HTML(response)  # 解析成xpath可以获取节点的内容
    h2 = htm.xpath('//*[@id="activity-name"]/text()')  # 获取微信文章的标题，以便对文件夹进行命名
    title = h2[0].strip()
    getImageSrc(title,htm)



def getImageSrc(title,html):   #得到图片的url地址
    imageSrc = html.xpath('//img/@data-src')
    for i in imageSrc:
        # image = requests.get(i).content
        saveImage(i,title)




def saveImage(url,title):    #这边可以从url里面获取图片的题目和图片格式
    try:
        picName= url.split("/")[4]
        fmt=url.split("=")[1]
        image = requests.get(url).content

        with open ("D:/python爬虫/myown/venv/weChatCrwaling/"+"yes"+"/"+picName+"."+fmt,"wb") as f:   #这边下载图片只能是二进制文件，不然执行时会报错
            f.write(image)
    except (urllib.error.HTTPError,OSError) as reason:
        print(reason)
    else:
        print("下载成功")




    # image = requests.get(imageSrc[0]).content
    # try:
    #     with open ("pic2.png","wb") as f:   #这边下载图片只能是二进制文件，不然执行时会报错
    #         f.write(image)
    # except (urllib.error.HTTPError,OSError) as reason:
    #     print(reason)
    # else:
    #     print("下载成功")
    # # print(image)



if __name__ == '__main__':   #程序开始执行的地方
    url = "https://mp.weixin.qq.com/s/hjRDFRWKwPSij2NO06fvXg"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    getTitle(url,headers)



