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
        print(response.request.headers)
        urls = response.xpath('.//*[@id="wp_page_numbers"]/ul/li/a/@href').getall()
        for url in urls:
            print(url)
            yield  Request(self.urlpre+ url ,headers=self.header,callback=self.parse_page)
    def parse_page(self, response):
        print(response.url)
        urls = response.xpath('.//li//h3[@class="tit"]/a/@href').getall()
        # title = response.xpath('.//li//h3[@class="tit"]/a/text()').getall()
        for url in urls:
            print(url)
            yield  Request( url ,headers=self.header,callback=self.parse_img)
    def parse_img(self, response):   
         
        urls = response.css('div#picture img::attr(src)').extract()
        title = response.xpath(".//div[@class='metaRight']/h2/a/text()").get()
        datetime = response.xpath(".//div[@class='metaLeft']//div[@class='month_Year']/text()").get()
        print(response.url ,title,urls,datetime)
        yield ImageItem(image_urls=urls,referer =response.url,title = title,datetime=datetime)


