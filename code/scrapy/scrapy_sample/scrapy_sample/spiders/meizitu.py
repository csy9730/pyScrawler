# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request

class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    start_urls = [#'http://www.meizitu.org/page/2/',
	'https://www.meizitu.com/a/5501.html',
                  'https://www.meizitu.com/a/5524.html'
				  ]
    def start_requests(self):      
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' 
        header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'user_agent': user_agent}
        return [Request(self.start_urls[0],headers=header,callback=self.parse)]
    def parse(self, response):
        print(response.request.headers)
        yield ImageItem(image_urls=response.css('div#picture img::attr(src)').extract())
