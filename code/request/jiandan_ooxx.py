import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
import random

#pth = r'C:\Program Files (x86)\Google\Chrome\Application'
#pth =r'D:\GreenSoftware\Chrome45_v2015.06.01\Browser'
#sys.path.append(pth)
DST_PATH ='jiandan2/'
import binascii
def _crc32(v):
    return '%x' % (binascii.crc32(v.encode('UTF-8')) & 0xffffffff)  # 取crc32的八位数据 %x返回16进制
url = 'http://jandan.net/ooxx/page-50689418#comments'
url = 'http://jandan.net/ooxx/page-20#comments'

browser = webdriver.Chrome()
# 设置网站等待时间
wait = WebDriverWait(browser, 10)

def get_one(url):
    print('正在爬取...',url)
    try:
        print(url)
        browser.get(url)
        html = browser.page_source
        if html:
            return html
    except EOFError:
        return None

def pares_one(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.select('img')
    url = soup.select('#body #comments .comments .cp-pagenavi a')[1]
    href = re.findall('href="(.*?)"', str(url))
    next_url = 'https:' + href[0]
    percent_num = re.findall('\d+', str(url))[-1]
    count = 0
    for img in imgs:
        img_url = re.findall('src="(.*?)"', str(img))
        if not img_url[0][-3:] == 'gif':
            if not img_url[0][-3:] == 'png':
                print('正在下载：%s 第 %s 张' % (img_url[0], count))
                #write_fo_file(img_url[0], '0.0', count)
                write_fo_file2(img_url[0], DST_PATH + percent_num)
        count += 1
    return next_url

def pares_one_of_num(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.select('img')
    print("next_url=",soup.select('#body #comments .comments .page-meter-title'))

    url = soup.select('#body #comments .comments .cp-pagenavi a')[1]
    href = re.findall('href="(.*?)"', str(url))
    next_url = 'https:' + href[0]

    #num = soup.select('#body #comments .comments .page-meter-title')[0].getText()
    #percent = re.findall('\d+', num)
    url = soup.select('#body #comments .comments .cp-pagenavi a')[1]
    href = re.findall('href="(.*?)"', str(url))
    #percent_num = percent[0] + '.' + percent[1]
    #percent_num = str((float(random.randint(100,1000))))
    percent_num = re.findall('\d+',str(url))[-1]
    next_url = 'https:' + href[0]

    count = 0
    for img in imgs:
        img_url = re.findall('src="(.*?)"', str(img))
        if not img_url[0][-3:] == 'gif':
            if not img_url[0][-3:] == 'png':
                if img_url[0][-3:]:
                    print('正在下载：%s 第 %s 张' % (img_url[0], count))
                    #write_fo_file(img_url[0], percent_num, count)
                    write_fo_file2(img_url[0], DST_PATH+percent_num)
        count += 1
    return percent_num, next_url

def write_fo_file2(url, dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filename = url[url.rfind('/') + 1:]
    filename = '%s/%s/%s' % (os.path.abspath('.'), dirName, filename)
    print(filename)
    with open(filename, 'wb+') as jpg:
        jpg.write(requests.get(url).content)

def write_fo_file(url, num, count):
    dirName = u'{}/{}'.format('jiandan', num)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, count)
    print(filename)
    with open(filename, 'wb+') as jpg:
        jpg.write(requests.get(url).content)

def next(url):
    html = get_one(url)
    percent_num, next_url = pares_one_of_num(html)
    while percent_num != '100.0':
        next(next_url)

def main():

    html = get_one(url)
    next_url = pares_one(html)
    #print(next_url)
    next(next_url)

if __name__ == '__main__':
   main()
