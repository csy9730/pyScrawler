# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy_sample.items import ImageItem
from urllib.parse import quote

# 构造url时，如果搜索内容有中文，可以先单独在终端导入 
"""
name = "搜索内容"
newName = quote(name) 
print(newName) # 如中文'赵丽颖'为'%E8%B5%B5%E4%B8%BD%E9%A2%96'
# 将爬虫url中的word=后面的内容替换就行
"""

class DuduSpider(scrapy.Spider):
    name = 'baiduimage'
    # 爬虫允许的爬取域名范围，最好根据你所要爬取的网站来确定，不能乱写，否则会搜索不到内容，使爬虫不受控制
    allowed_domains = ['image.baidu.com']
    #构建url的起始值offset，具体由网页分析后确定
    base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn=%s'
    #起始url，列表内字符串的拼接    
    def __init__(self,word = "moon",**kwargs):
        super(DuduSpider, self).__init__( **kwargs)
        self.word = word
        self.offset = 90
        self.start_urls = [self.base_url % ( self.word,str(self.offset))]


    def parse(self, response):        
        #使用scrapy shell 返回的内容为json格式，正则匹配出图片链接并提取
        pattern = re.compile(r'"middleURL":"(.*?)",', re.S)
        datas = re.findall(pattern, response.text)
        img_folder =  self.word+'/'        
        item = ImageItem()
        # print("图片链接是:", data)
        item['image_urls'] = datas
        #生成器，返回给pipelineItem文件
        # 由一个url获取一个图片的url列表,列表内有若干个图片链接url，依次获取发送图片链接的url，直至发送完，跳出循环
        item['referer'] = response.url
        item['img_folder'] = img_folder
        yield item
        #跳出循环后offset自增30（网页决定）
        self.offset += 30
        
        url = self.base_url % ( self.word,str(self.offset))
        yield scrapy.Request( url, callback=self.parse)

