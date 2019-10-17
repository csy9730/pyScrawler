from urllib.parse import *
import os
def eParse():
    url = "http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0"
    print( urlparse(url))
    url2 = "https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html"
    print( urlparse(url2))
    pth2 = 'files:' + os.path.basename(urlparse(url2).path)
    print(pth2)

    url3 = "http://tieba.baidu.com/p/6213434183"
    print(urlparse(url3))
    pth2 = 'files:' + os.path.basename(urlparse(url3).path)
    print(pth2)
def eUrljoin():
    url = urljoin("https://www.abc.com","a/wi.html")
    print(url)

eParse()
eUrljoin()