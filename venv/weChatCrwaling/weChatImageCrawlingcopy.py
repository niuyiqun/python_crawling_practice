# -*- codeing = utf-8 -*-
# @Time : 2020/9/23 20:34
# @Author : niu
# @File : weChatImageCrawling.py
# @Software: PyCharm
import urllib

import requests
from lxml import html

url = "https://mp.weixin.qq.com/s/hjRDFRWKwPSij2NO06fvXg"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}
response = requests.get(url, headers=headers).text  # 说是转化成unicode型数据   .content返回的是二进制文件42
et = html.etree
htm = et.HTML(response)  # 解析成xpath可以获取节点的内容
h2 = htm.xpath('//*[@id="activity-name"]/text()')  # 获取微信文章的标题，以便对文件夹进行命名
title = h2[0].strip()
imageSrc = html.xpath('//img/@data-src')
for i in imageSrc:
    try:
        picName = url.split("/")[4]
        fmt = url.split("=")[1]
        image = requests.get(url).content
        with open("D:/python爬虫/myown/venv/weChatCrwaling/" + title + "/" + picName + "." + fmt,"wb") as f:  # 这边下载图片只能是二进制文件，不然执行时会报错
            f.write(image)
    except (urllib.error.HTTPError, OSError) as reason:
        print(reason)
    else:
        print("下载成功")






