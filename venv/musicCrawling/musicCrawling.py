# -*- codeing = utf-8 -*-
# @Time : 2020/10/11 20:24
# @Author : niu
# @File : musicCrawling.py
# @Software: PyCharm

import xlrd
import xlwt
import os
import requests
import re
from bs4 import BeautifulSoup

baseUrl = "https://music.douban.com/top250?start="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Host':'music.douban.com'
}
response=requests.get("https://music.douban.com/top250?start=").text

bs = BeautifulSoup(response,'html.parser')    #这里用html.parser和lxml有什么区别吗

savepath = os.path.join(os.getcwd(),'music.xls')
def getData():
    datalist = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)  # 拿到所有网页的地址
        response = requests.get(url, headers=headers).text
        bs = BeautifulSoup(response, 'html.parser')  # 这里用html.parser和lxml有什么区别吗
        # print(type(bs))
        trs = bs.select("div.indent table tr")  # 成功拿到trs
        for tr in trs:
            data = []
            tds = tr.select('td')  # 拿到td
            imageSrc = tds[0].img.get('src')
            musicName = tds[1].div.a.contents[0].strip()  # .strip()方法除去多余的空格
            # musicName = tds[1].div.a.text.strip().split('\n')[0]  # .strip()方法除去多余的空格
            info = tds[1].div.p.string.split('/')
            singer = info[0]
            issueTime = info[1]
            # form = info[2] + "/" + info[3] + "/" + info[4]
            form = info[2]
            mark = tds[1].select('div span.rating_nums')[0].string
            number = tds[1].select('div span.pl')[0].string.strip().replace(' ', '').replace("\n", '')
            number_regex = re.compile("^\((\d*)人评价\)$")  # 正则表达式还是不太行噢
            true_number = number_regex.findall(number)[0]  # 这个是拿到的评价人数
            detail = tds[1].a.get('href')
            data.append(musicName)  # 歌曲名
            data.append(singer)  # 演唱者
            data.append(issueTime)  # 发行时间
            data.append(form)  # 类型
            data.append(mark)  # 评分
            data.append(true_number)  # 评价人数
            data.append(imageSrc)  # 图片(地址)
            data.append(detail)  # 详情页       #一共八列
            datalist.append(data)  # 所有的数据均保存到datalist里面了
            # print(data)
            # 目前拿到了所有的信息
            # print("图片地址",regex.findall(str(tds[0])))
            # print("图片地址",re.findall(regex,str(tds[0])))
    # i=1
    # for data in datalist:
    #     print(i,data)
    #     i+=1

    saveData(datalist)


def saveData(datalist):         #这边存储数据的方法是用一个列表存储所有的信息，然后一次性保存
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("豆瓣音乐top250",cell_overwrite_ok=True)
    col = ['歌曲名','演唱者','发行时间','类型','评分','评价人数','图片(地址)','详情页']
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,246):      #豆瓣太不靠谱了，居然不是250条
        print("正在存储第",i+1,"条")
        data=datalist[i]
        for j in range(0, 8):
            sheet.write(i+1,j,data[j])
    workbook.save(savepath)

if __name__ == '__main__':
    getData()