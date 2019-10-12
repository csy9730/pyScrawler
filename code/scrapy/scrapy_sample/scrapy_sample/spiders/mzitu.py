# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import copy
import re

class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    urlpre = 'https://www.mzitu.com'
    start_urls = [
	        'https://www.mzitu.com',
	]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [Request(self.start_urls[0],headers=self.header,callback=self.parse)]
    def parse0(self,response):
        """ This function parses pages
            @url https://www.mzitu.com
            @scrapes https://www.mzitu.com/193336  https://www.mzitu.com/page/2/
        """
        print(response.request.headers)
        urls = response.xpath('//ul[@id="pins"]//li//span//@href').getall()
        for url in urls:
            print(url)
            yield  Request( url ,headers=self.header,callback=self.parse_article)
        page_urls= response.xpath('//div[@class="nav-links"]//a/@href').getall()
        for url in page_urls:
            yield  Request( url ,headers=self.header,callback=self.parse)
        
    def parse_article(self,response):
        l = ItemLoader(item=ImageItem(), response=response)
        l.add_xpath('image_urls', '//div[@class="main-image"]//a/img/@src')
        l.add_xpath('title', '//h2//text()')
        l.add_xpath('img_folder', '//h2//text()')
        # l.add_xpath('datetime', './/div[@class="metaLeft"]//div[@class="month_Year"]/text()')
        # count = response.xpath('//div[@class="pagenavi"]//a/span/text()').getall()[-2]
        l.add_value('referer', response.url) 
        yield l.load_item()
        page_urls = response.xpath('//div[@class="pagenavi"]//a/@href').getall() 
        for page in page_urls:             
            yield  Request( page ,headers=self.header,callback=self.parse_image, meta={"img_folder":l.get_value("img_folder")})
    def parse_image(self,response):
        l = ItemLoader(item=ImageItem(), response=response)
        l.add_xpath('image_urls', '//div[@class="main-image"]//a/img/@src')
        l.add_xpath('title', '//h2//text()')
        l.add_value('img_folder', response.meta['img_folder'])
        # l.add_xpath('datetime', './/div[@class="metaLeft"]//div[@class="month_Year"]/text()')
        l.add_value('referer', response.url) 
        return l.load_item()



class MzituSpider2(CrawlSpider):
    name = 'mzitu2'
    urlpre = 'https://www.mzitu.com'
    start_urls = [
            #'https://www.mzitu.com/193823',
            'https://www.mzitu.com/page/2/',
	        
	]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    rules = (
        # Rule(LinkExtractor(allow='/\\d+/\\d+', restrict_xpaths='//div[@class="pagenavi"]'),callback='parse_nop3'),             
        Rule(LinkExtractor(allow='/\\d+',restrict_xpaths='//ul[@id="pins"]//li//span'),callback='parse_article'), # from list get article
        Rule(LinkExtractor(allow='/page/\\d+/',restrict_xpaths='//div[@class="nav-links"]')), # next-page of list
    )
    routes = [  {"allow":"/\\d+$","callback":"parse_article"} ,
                    {"allow":"/page/\\d+/","callback":"parse_nop"} ,
        ]        
    for r in routes:
        r.update(allow_res=re.compile(r["allow"]))
    def parse_start_url(self, response):          
        for ar in self.routes:
            if ar["allow_res"].search(response.url):
                return getattr(self,  ar["callback"] ) (response) 
        return self.parse_article(response)
    def parse_nop(self,response):
        """ This function parses pages
            @url https://www.mzitu.com
            @scrapes https://www.mzitu.com/193336  https://www.mzitu.com/page/2/
        """
    def parse_article(self,response):
        """   @url  https://www.mzitu.com/193823/
              @scrapes  https://www.mzitu.com/193823/2
              
        """
        l = ItemLoader(item=ImageItem(), response=response)
        l.add_xpath('image_urls', '//div[@class="main-image"]//a/img/@src')
        l.add_xpath('title', '//h2//text()')
        l.add_xpath('img_folder', '//h2//text()')        
        l.add_xpath('datetime', '//div[@class="main-meta"]/span',re='[\\d :-]{8,}')
        l.add_value('referer', response.url) 
        lt = l.load_item()
        yield lt
        count = int( (response.xpath('//div[@class="pagenavi"]//a/span/text()').getall() or [0,0] )[-2] )
        print("count",count,)
        # page_urls = response.xpath('//div[@class="pagenavi"]//a/@href').getall() 
        for i in range(2, count):
            page = '{0}/{1}'.format(response.url, i)            
            yield  Request( page ,headers=self.header,callback=self.parse_image,meta={"item":lt }) 
    def parse_image(self,response):
        it = copy.copy( response.meta['item'])
        it['referer'] =  response.url
        it["image_urls"] = response.xpath('//div[@class="main-image"]//a/img/@src').getall()
        return it

