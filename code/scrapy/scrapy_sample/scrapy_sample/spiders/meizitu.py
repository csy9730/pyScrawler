# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request

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
        print(response.request.headers)
        urls = response.xpath('.//*[@id="wp_page_numbers"]/ul/li/a/@href').getall()
        for url in urls:
            print(url)
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
        urls = response.css('div#picture img::attr(src)').extract()
        title = response.xpath(".//div[@class='metaRight']/h2/a/text()").get()
        datetime = response.xpath(".//div[@class='metaLeft']//div[@class='month_Year']/text()").get()
        img_folder = title+'/'
        print(response.url ,title,urls,datetime)
        yield ImageItem(image_urls=urls,referer =response.url,title = title,datetime=datetime,img_folder=img_folder)


