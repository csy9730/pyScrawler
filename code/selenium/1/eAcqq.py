

from selenium import webdriver
import os,sys
import json
from  selenium.webdriver.chrome.options import  Options

# http://www.u17.com/
# http://www.u17.com/comic/112874.html


class spider(object):
    def __init__(self):
        self._chrome()
        
    def _chrome(self):
        os.environ['PATH'] +=';../;'
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--log-level=3")  # fatal
        chrome_options.add_argument('disable-infobars')
        # chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})       
        # 设置中文
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 更换头部
        # chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
        chrome_options.add_argument('user-agent="User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"')
        chrome_path = 'drivers/chromedriver.exe'

        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.maximize_window()
    def run(self,url = "https://ac.qq.com/Comic/comicInfo/id/505430"):
        self.browser.get( url )
        sel = '//div[@class="chapterlist_box"]//li/a'
        # sel = '//li//p//span[@class="works-chapter-item"]//a'
        fd = self.browser.find_elements_by_xpath( sel)
        urls = [ f.get_attribute('href') for f in fd]
        self.browser.get(urls[0])
        
        imgXpath = '//div[@id="current_read_image"]//img'
        imgs = self.browser.find_elements_by_xpath( imgXpath)
        sel2 =  '//div[@class="selectpage"]/a'
    def run2(self,url="http://www.u17.com/comic/112874.html"):
        self.browser.get( url )
        sel = '//div[@class="chapterlist_box"]//li/a'
        fd = self.browser.find_elements_by_xpath( sel)
        urls = [ f.get_attribute('href') for f in fd]
        self.browser.get(urls[0])
        
        imgXpath = '//div[@id="current_read_image"]//img'
        imgs = self.browser.find_elements_by_xpath( imgXpath)
        img_urls = [ f.get_attribute('src') for f in imgs]
        sel2 =  '//div[@class="selectpage"]/a'  

def main():
    spd = spider()
    url = "http://www.u17.com/comic/112874.html"
    spd.run(url)
    

    import time
    time.sleep(100)
    #loginBaidu()
if __name__ == '__main__':
    main()
