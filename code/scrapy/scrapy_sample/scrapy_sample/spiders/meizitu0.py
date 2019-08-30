# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request


class Meizitu0Spider(scrapy.Spider):
    name = 'meizitu0'
    allowed_domains = ['meizitu.com']
    start_urls =  [
                'https://www.meizitu.com/a/5504.html',
                'https://www.meizitu.com/a/5501.html',
	]
    def parse(self, response):         
        urls = response.css('div#picture img::attr(src)').extract()
        title = response.xpath(".//div[@class='metaRight']/h2/a/text()").get()
        datetime = response.xpath(".//div[@class='metaLeft']//div[@class='month_Year']/text()").get()
        print(response.url ,title,urls,datetime)
        yield ImageItem(image_urls=urls,referer =response.url,title = title,datetime=datetime)