# -*- coding: utf-8 -*-
import os,sys,time
import json
from selenium import webdriver
from  selenium.webdriver.chrome.options import  Options
import requests
import json_lines

""" 批量下载漫画,广度优先策略
https://manhua.sfacg.com/
https://manhua.sfacg.com/mh/wqds/
nextpage: https://manhua.sfacg.com/mh/wqds/66039/
"""
# todo add json export dict item
def creatDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def jsonlineWrite(pfn,lst):
    with open( pfn,'w') as fp:
        for item in lst:
            fp.write(json.dumps(item)+'\n')

def jsonlineShow(pfn,dct):
    with open(pfn, 'rb') as f:
        # lst = json_lines.reader(f)
        for item in json_lines.reader(f):
            lst.append(item)
            #print(item)
    return lst
def fStrip(s,replaced_char='_'):
    valid_filename = s
    invalid_characaters = '\\/:*?"<>|'
    for c in invalid_characaters:
        valid_filename = valid_filename.replace(c, replaced_char)
    return valid_filename 

# 保存图片的方法

def download_image(url,path,pfn=None):
    if pfn is None:
        pfn = url.split('/')[-1]
    r = requests.get(url)   
    pth = os.path.join(path,pfn) 
    with open(pth, 'wb') as f:
        f.write(r.content)
###       
def savePic(path,page,url):
    content=requests.get(url).content  
    path=path+'//'+page+'.png'
    with open(path,'wb') as f:
        f.write(content) 

class cBasicSpider(object):
    def __init__(self):
        self._chrome()
        self.basePath = 'images/'
        
    def _chrome(self):
        os.environ['PATH'] +=';../;'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--log-level=3")  # fatal
        chrome_options.add_argument('disable-infobars')
        # chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})   # 禁用 js脚本
        chrome_options.add_argument('lang=zh_CN.UTF-8') # 设置中文
        # 更换头部
        # chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
        chrome_options.add_argument('user-agent="User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"')
        chrome_path = 'drivers/chromedriver.exe'

        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.minimize_window()
    def parse_book(self,url):
        '''
            获取漫画的目录中的每一章节的url连接
            并返回一个字典类型k：漫画名 v：章节链接
        '''        
        self.browser.get(url)
        book=self.browser.find_element_by_tag_name('h1').text
        li_list=self.browser.find_elements_by_class_name('comic_Serial_list')

        print(book,len(li_list)) 
        url_list = []
        for li in li_list:
            a_list=li.find_elements_by_tag_name('a');
            for a in a_list:
                url_list.append(a.get_attribute('href'))
        dct=dict(book=book,urls=url_list,referer = url)                
        return dct
    def parse_chapter(self,url):
        '''
        打开每个章节的url，
        找到漫画图片的地址，
        并写入到本地
        '''
        self.browser.get(url)
        self.browser.implicitly_wait(3)
        title = self.browser.find_element_by_xpath('//div[@id="AD_j1"]//span').get_attribute('textContent') or ''; #  .get_attribute("innerHTML") 
        self._index += 1 
        print(self._index ,title)
        chapterPath="{0}//{2}_第{1}章".format( self.bookPath , self._index,fStrip(title))  # path +"//"+'第'+ str(a) +'章'
        creatDir(chapterPath)
        #查看总共有多少页,
        '''
        <select id="pageSel" οnchange="GoSelPage()"><option value="1">第1页</option><option value="2">第2页</option>
        <option value="3">第3页</option><option value="4">第4页</option><option value="5">第5页</option><option value="6">第6页
        </option><option value="7">第7页</option><option value="8">第8页</option><option value="9">第9页</option></select>
        
        '''
        pages = self.browser.find_elements_by_tag_name('option')
        # 找到下一页的按钮
        #<a href="javascript:NextPage();" class="redfont_input">下一页</a>
        nextpage = self.browser.find_element_by_xpath('//*[@id="AD_j1"]/div/a[4]')
        urls = []
        for page in range(len(pages)): 
            #图片的地址
            #<img alt="快捷键：A下翻页，Q上翻页" border="0" id="curPic" src="http://coldpic.sfacg.com/Pic/OnlineComic4/wqds/ZP/0072_4701/023_997.jpg">
            pic_url = self.browser.find_element_by_id('curPic').get_attribute('src')
            urls.append( pic_url)
            # savePic(chapterPath ,str(page),pic_url)        
            download_image(pic_url,chapterPath,'%s.png' % page)
            nextpage.click()
        return dict( image_urls = urls ,title=title,referer= url)

    def run(self,start_url):
        self._index = 0 
        Comics = self.parse_book(start_url)
        print(Comics)
        jsonlineWrite('scr_1.jl',[Comics])

        creatDir(self.basePath)
        self.bookPath = self.basePath + Comics['book']
        creatDir( self.bookPath )

        chapt_urls=Comics['urls']  
        lst = []      
        for url in chapt_urls:       
            dc = self.parse_chapter(url)
            lst.append(dc)

        jsonlineWrite('scr_img.jl',lst)
        print("finished")    

def main():
    url = 'https://manhua.sfacg.com/mh/wqds/' 
    url = 'https://manhua.sfacg.com/mh/CYYHL/'
    spd= cBasicSpider()
    spd.run(url)
if __name__ == '__main__':
    main()

