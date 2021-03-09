# -*- codeing = utf-8 -*-
# @Time : 2020/9/26 19:26
# @Author : niu
# @File : wallpaperCrawling.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import os

baseUrl = "http://www.win4000.com/"
themeBaseUrl = "http://www.win4000.com/zt/xiaoqingxin.html"
themeUrlList =[]   #用来放套图地址
for i in range(1,6):    #左开右闭
    themeUrlList.append("http://www.win4000.com/zt/xiaoqingxin_"+str(i)+".html")
    # print(themeUrlList)

seriesUrlLists=[]

def getSeriesUrlLists(url):    #拿到所有的副页面的网址
    r=requests.get(url)
    if r is not None:
        response=r.text
        bs=BeautifulSoup(response,"html.parser")   #用html.parser解析过后的文件
        ul = bs.find("div",attrs={"class":"tab_tj"})
        a_s=ul.find_all("a")
        for a in a_s:
            seriesUrlLists.append(a.get('href'))   #对标签可以直接用get方法获取标签里面的属性值

def getImage(url):
    i=1
    while True:
        currentUrl=url.replace(".html",'_'+str(i)+".html")
        response = requests.get(currentUrl)
        if response.status_code!=404:
            result=response.text
            bs=BeautifulSoup(result,"lxml")
            a = bs.select('img.pic-large')
            title = a[0].get('title')
            imageAdd=a[0].get("src")
            saveImage(imageAdd,title)
            i=i+1
        else:
            break

def saveImage(url,path):   #url指的是图片的地址，path是保存路径
    print("下载图片"+url)
    image = requests.get(url).content
    if not os.path.exists(os.getcwd()+"\\tmp\\"+path):
        os.makedirs(os.getcwd()+"\\tmp\\"+path)
    with open (os.getcwd()+"\\tmp\\"+path+"\\"+url.split("/")[-1], "wb") as f:
        f.write(image)







if __name__ == '__main__':
    for item in themeUrlList:
        getSeriesUrlLists(item)
    for item in seriesUrlLists:
        getImage(item)


