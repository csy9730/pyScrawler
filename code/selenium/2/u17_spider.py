

from selenium import webdriver
import os,sys
import json
from  selenium.webdriver.chrome.options import  Options
from basic_spider import *

"""
http://www.u17.com/
http://www.u17.com/comic/112874.html
"""


class cU17Spider(cBasicSpider):
    def __init__(self):
        cBasicSpider.__init__(self)
    def parse_book(self,url):
        self.browser.get( url )
        sel = '//div[@class="chapterlist_box"]//li/a'
        fd = self.browser.find_elements_by_xpath( sel)
        url_list = [ f.get_attribute('href') for f in fd]
        title = self.browser.find_element_by_xpath( "//h1").text
        dct=dict(book=title,urls=url_list,referer = url)    
        return dct
        
    def parse_chapter(self,url):
        self.browser.get(url)
        imgXpath = '//div[@id="current_read_image"]//img[@class="image_cache loading cur_img"]'
        npPath = '//div[@class="pagebar"]//a[@class="next"]'
        title = self.browser.find_element_by_xpath( '//*[@id="current_chapter_name"]').text
        img = self.browser.find_element_by_xpath( imgXpath).get_attribute('src')
        download_image(img,".")
        nums =self.browser.find_element_by_xpath( '//strong[@class="pagenum"]').text
        num = int( nums.split('/')[-1] )
        img_urls = []
        for n in range(1,num): 
            img = self.browser.find_element_by_xpath( imgXpath).get_attribute('src')
            download_image(img,".",'%s.png' % str(n+1))
            img_urls.append( img)
            next_page=self.browser.find_element_by_xpath(npPath)        
            self.browser.execute_script("arguments[0].click();", next_page)# next_page.click()
        return dict( image_urls = img_urls ,title=title,referer= url)

    def run(self,start_url):
        self._index = 0 
        Comics = self.parse_book(start_url)

        print(Comics)
        jsonlineWrite('scr_2.jl',[Comics])
        creatDir(self.basePath)
        self.bookPath = self.basePath + Comics['book']
        creatDir( self.bookPath )

        chapt_urls=Comics['urls']  
        lst = []      
        for url in chapt_urls[0:2]:       
            dc = self.parse_chapter(url)
            lst.append(dc)

        jsonlineWrite('scr_img2.jl',lst)
        print("finished") 


def main():
    spd = cU17Spider()
    url = "http://www.u17.com/comic/112874.html"
    spd.run(url)
    
    #loginBaidu()
if __name__ == '__main__':
    main()
