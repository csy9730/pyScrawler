# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ImageSpider(CrawlSpider):
    name = 'images'
    
    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = configv
        self.rules = rules.get(config.get('rules'))
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allowed_domains = config.get('allowed_domains')
        super(ImageSpider, self).__init__(*args, **kwargs)
    
    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()


class Meizitu3Spider(scrapy.Spider):
    name = 'meizitu3'
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
        for url in self.start_urls:
            if url ==  "https://www.meizitu.com":
                callback_index =  0
            elif 1:
                pass
                

            yield Request( url ,callback=self.parse, meta={"callback_index": 0 })
    def parse(self,response):
        """ This function parses pages
            @url https://www.meizitu.com
            @scrapes /a/list_1_1.html
        """

    def parse_page(self, response):
        """ This function parses pages
            @url https://www.meizitu.com/a/list_1_1.html
            @scrapes https://www.meizitu.com/a/5521.html
        """
        
    def parse_title(self, response): 

        if callback_index ==0:
            urls = response.xpath('.//*[@id="wp_page_numbers"]/ul/li/a/@href').getall()
            for url in urls:
                yield  Request(self.urlpre+ url ,callback=self.parse_page)
        elif callback_index ==1:
            urls = response.xpath('.//li//h3[@class="tit"]/a/@href').getall()
            # title = response.xpath('.//li//h3[@class="tit"]/a/text()').getall()
            for url in urls:
                yield  Request( url ,callback=self.parse_title)
        elif 2:
            l = ItemLoader(item=ImageItem(), response=response)
            l.add_css('image_urls', 'div#picture img::attr(src)')
            l.add_xpath('title', './/div[@class="metaRight"]/h2/a/text()')
            l.add_xpath('img_folder', './/div[@class="metaRight"]/h2/a/text()')
            l.add_xpath('datetime', './/div[@class="metaLeft"]//div[@class="month_Year"]/text()')
            l.add_value('referer', response.url) # you can also use literal values
            yield l.load_item()    
