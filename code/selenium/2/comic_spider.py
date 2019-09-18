# -*-coding:utf-8-*-
# !/usr/bin/env python

"""
爬取腾讯漫画最新一话图片
"""
import os
import time
from datetime import time
from urllib import request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pymongo import MongoClient

from sfacg_spider import *

#MongoDB进行数据库操作
conn = MongoClient('127.0.0.1',27017)
comic_db = conn.comic
op = comic_db.op

ROOT_URL = "http://ac.qq.com"
TargetUrls = [
    ROOT_URL + "/Comic/comicInfo/id/505430",  # 海贼王
]

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "no-cache",
    'host': "ac.qq.com",
    'proxy-connection': "keep-alive",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
}

class acqqSpider(cSfacgSpider):
    def __init__(self):
        super(acqqSpider).__init__()
        self._chrome()
    def ssf(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)")
        self.browser = webdriver.PhantomJS(executable_path=r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs",
                                    desired_capabilities=dcap)
    def getUrls(self,target_url):
        result = dict()
        req = request.Request(target_url, headers=headers)
        response = request.urlopen(req)
        soup = bs(response.read(), "lxml")
        # 返回最近漫画中的最新20话
        page = soup.find(attrs={"class": "chapter-page-new works-chapter-list"}).find_all(
            "a")  # 全部漫画 chapter-page-new works-chapter-list
        title = page[-1]['title']
        result[title] = ROOT_URL + page[-1]['href']
        return result
    def getImageUrls(self,comic_url):
        '''
        通过Selenium和Phantomjs获取动态生成的数据
        '''
        urls = []        
        self.browser.get(comic_url)
        imgs = self.browser.find_elements_by_xpath("//div[@id='mainView']/ul[@id='comicContain']//img")
        for i in range(0, len(imgs) - 1):
            if i == 1:  # 略过广告图片
                continue
            urls.append(imgs[i].get_attribute("src"))
            js = 'window.scrollTo( 800 ,' + str((i + 1) * 1280) + ')'
            self.browser.execute_script(js)
            time.sleep(randint(2, 4))
        self.browser.quit()
        return urls
    def run(self):
        pic_urls = getUrls(TargetUrls[0])
        print(pic_urls)
        for title, url in pic_urls.items():
            """if op.find_one({"_id":url}):
                print("该漫画已存在")
                continue
            op.insert({"_id":url,"title":title})
            """
            dir_path = title + "/"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            img_urls = self.getImageUrls(url)
            downloadComics(dir_path, img_urls)

        # conn.close()



def getUrls(target_url):
    result = dict()
    req = request.Request(target_url, headers=headers)
    response = request.urlopen(req)
    soup = bs(response.read(), "lxml")
    # 返回最近漫画中的最新20话
    page = soup.find(attrs={"class": "chapter-page-new works-chapter-list"}).find_all(
        "a")  # 全部漫画 chapter-page-new works-chapter-list
    title = page[-1]['title']
    result[title] = ROOT_URL + page[-1]['href']
    return result
    

def getImageUrls(comic_url):
    '''
    通过Selenium和Phantomjs获取动态生成的数据
    '''
    urls = []

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)")
    browser = webdriver.PhantomJS(executable_path=r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs",
                                  desired_capabilities=dcap)
    browser.get(comic_url)

    imgs = browser.find_elements_by_xpath("//div[@id='mainView']/ul[@id='comicContain']//img")
    for i in range(0, len(imgs) - 1):
        if i == 1:  # 略过广告图片
            continue
        urls.append(imgs[i].get_attribute("src"))
        js = 'window.scrollTo( 800 ,%s)'% (i + 1) * 1280
        browser.execute_script(js)
        time.sleep(randint(2, 4))

    browser.quit()
    return urls


def downloadComics(dir_path, urls):
    for url in urls:
        request.urlretrieve(url, dir_path + url[-9:])


if __name__ == "__main__":
    spd = acqqSpider()
    spd.run()