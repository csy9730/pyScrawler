# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem,BookItem

import execjs
import json,os
os.environ["EXECJS_RUNTIME"] = 'Node'
# @todo https://manhua.dmzj.com/haizeiwang/
# @todo m.dmzj.com
class dmzjSpider(scrapy.Spider):
    name = 'dmzj'
    url = 'https://manhua.dmzj.com'
    start_urls = [ 
                   # 'https://manhua.dmzj.com/tags/maoxian/139.shtml',
                    'https://manhua.dmzj.com/yaojingdeweibabainianrenwu',
                   # 'https://manhua.dmzj.com/yaojingdeweiba',
                  #'https://www.mm131.net/xinggan/2746.html',
                 ]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def __init__(self, book=None, *args, **kwargs):
        super(dmzjSpider, self).__init__(*args, **kwargs)
        if book is not None:
            books = book.split(';')
            self.start_urls = ['%s/%s' % (self.url,b) for b in books if len(b)>0]
    def start_requests(self): 
        for url in     self.start_urls:
            yield scrapy.Request(url,headers=self.header,callback=self.parse_book)
    def parse_page(self,response):
        """ 
            @url https://manhua.dmzj.com/tags/maoxian.shtml
            @scrapes  /haizeiwang/   /yaojingdeweiba/   /tags/maoxian/1.shtml
        """
        urls = response.xpath("//div[@class='leftmiddle']//ul/li/a/@href").getall()
        print(urls)
        for url in urls:
            if url.find(self.url)<0:
                url = self.url+url
            yield scrapy.Request( url ,headers=self.header,callback=self.parse_book)
        page_urls =response.xpath("//div[@class='pages']/a/@href").getall()
        for url in page_urls:
            if url.find(self.url)<0:
                url = self.url+url
            yield scrapy.Request( url ,headers=self.header,callback=self.parse_page)
    def parse_book(self,response):
        """ 
            @url https://manhua.dmzj.com/yaojingdeweiba
            @scrapes /yaojingdeweiba/24622.shtml
        """
        # print(response.request.headers)
        urls = response.xpath(".//div[@class='cartoon_online_border_other']/ul/li/a/@href|.//div[@class='cartoon_online_border']/ul/li/a/@href").getall()
        
        title = response.xpath("//div[@class='line_height_content']//text()").get()
        des = response.xpath("//div[@class='line_height_content']//text()").get()
        misc = response.xpath('.//table//text()').getall()
        yield BookItem( misc = misc,descrption=des,title=title)
        self.header["referer"] = response.url
        for url in urls:
            if url.find(self.url)<0:
                url = self.url+url
            yield scrapy.Request( url ,headers=self.header,callback=self.parse_image)
        # author = response.xpath('//table//tr[3]//td/a/text()').getall()
        # tag = response.xpath('//table//tr[7]//a/@text').getall()
        # datetime = response.xpath('//table//tr[9]//span/text()').get()

    def parse_image(self, response):
        """
            @url https://manhua.dmzj.com/yaojingdeweiba/21148.shtml
            @scrapes //images.dmzj.com/y/%E5%A6%96%E7%B2%BE%E7%9A%84%E5%B0%BE%E5%B7%B4/%E5%A6%96%E7%B2%BE%E7%9A%84%E5%B0%BE%E5%B7%B4%20%E7%AC%AC12%E5%8D%B7/0001.jpg
        """
        # print("response.url",response.url)
        scripts = response.xpath('.//script/text()').getall() 
        ctx = execjs.compile(scripts[0])
        pages = ctx.eval('pages')        
        pg = json.loads( pages)
        img_url = ['https://images.dmzj.com/'+ p for p in pg ]
        item = ImageItem()
        item['image_urls'] = img_url# response.css('div.content-pic img::attr(src)').extract()
        item['referer'] = response.url
        item['img_folder'] = response.xpath('//title/text()').get()+'/'
        # item['title'] = response.xpath(".//div [@class='content']/h5/text()").get()
        # item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        yield item
