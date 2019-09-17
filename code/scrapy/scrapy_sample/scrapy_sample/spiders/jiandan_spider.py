# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request

class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]

    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
     
    def parse(self, response):
        print(response.request.headers)
        
        item = ImageItem()
        urls = response.xpath('//div[@class="text"]//img//@src').getall()#提取图片链接
        item['image_urls'] =  [  "https:"+ url for url in urls]
        item['img_folder'] = 'jiandan'
        item['referer'] =  response.url
        yield item
        new_url= "https:"+response.xpath('//a[@class="previous-comment-page"]//@href').get()#翻页
        return
        # print 'new_url',new_url
        if new_url:
            yield scrapy.Request(new_url,callback=self.parse,headers=self.header)