# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request
from ..utils import removeDirtyChar
from scrapy.loader import ItemLoader
import logging
_log = logging.getLogger(__name__)
class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    urlpre = 'https://www.meizitu.com'
    start_urls = [#'http://www.meizitu.org/page/2/',
	'https://www.meizitu.com',
               #   'https://www.meizitu.com/a/5524.html'
	]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [Request(self.start_urls[0],headers=self.header,callback=self.parse)]
    def parse(self,response):
        """ This function parses pages
            @url https://www.meizitu.com
            @scrapes /a/list_1_1.html
        """
        _log.info(response.request.headers)
        urls = response.xpath('.//*[@id="wp_page_numbers"]/ul/li/a/@href').getall()
        for url in urls:
            _log.info(url)
            yield  Request(self.urlpre+ url ,headers=self.header,callback=self.parse_page)
    def parse_page(self, response):
        """ This function parses pages
            @url https://www.meizitu.com/a/list_1_1.html
            @scrapes https://www.meizitu.com/a/5521.html
        """
        print(response.url)
        urls = response.xpath('.//li//h3[@class="tit"]/a/@href').getall()
        # title = response.xpath('.//li//h3[@class="tit"]/a/text()').getall()
        for url in urls:
            print(url)
            yield  Request( url ,headers=self.header,callback=self.parse_title)
    def parse_title(self, response): 
        l = ItemLoader(item=ImageItem(), response=response)
        l.add_css('image_urls', 'div#picture img::attr(src)')
        l.add_xpath('title', './/div[@class="metaRight"]/h2/a/text()')
        l.add_xpath('img_folder', './/div[@class="metaRight"]/h2/a/text()')
        l.add_xpath('datetime', './/div[@class="metaLeft"]//div[@class="month_Year"]/text()')
        l.add_value('referer', response.url) # you can also use literal values
        return l.load_item()        

class MeizituSpider0(scrapy.Spider):
    name = 'meizitu0'
    urlpre = 'https://www.meizitu.com'
    start_urls = [#'http://www.meizitu.org/page/2/',
                  'https://www.meizitu.com/a/5296.html'
                  ,'https://www.meizitu.com/a/5323.html'
                  ,'https://www.meizitu.com/a/5133.html'
	]
    def parse(self, response): 
        l = ItemLoader(item=ImageItem(), response=response)
        l.add_css('image_urls', 'div#picture img::attr(src)')
        l.add_xpath('title', './/div[@class="metaRight"]/h2/a/text()')
        l.add_xpath('img_folder', './/div[@class="metaRight"]/h2/a/text()')
        l.add_xpath('datetime', './/div[@class="metaLeft"]//div[@class="month_Year"]/text()')
        l.add_value('referer', response.url) # you can also use literal values
        return l.load_item()
