# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
import  re
import copy

class _36mhSpider(scrapy.Spider):
    name = '36mh'
    start_urls = [
            # 'https://m.36mh.com/', #'https://www.36mh.com/'
            'https://m.36mh.com/manhua/ReconglingkaishideyishijieshenghuodisanzhangTruthofZero/' ]
    allowed_domains = ['36mh.com']
    def parse(self,response):
        return parse_title(self,response)
        urls = response.xpath('//div[@class="imgBox"]//li//a/@href').getall()
        for url in urls:
            return  scrapy.Request( url,callback=self.parse_title) 
    def parse_title(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://manhua.sfacg.com/mh/LYB/
                @scrapes /mh/LYB/65407/
        """
        urls = response.xpath('//div[@class="list"]//li/a/@href').getall()
        for url in urls:
            yield  scrapy.Request( url,callback=self.parse_image)
    def parse_image(self, response):
        item = ImageItem()
        print(response.request.headers)
        item['image_urls'] = response.xpath('//mip-link//mip-img/@src').getall()
        item['referer'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        pg = response.xpath('//h1//span[@id="k_page"]/text()').get()
        item['img_folder'] = response.xpath('//title/text()').get()+'/'+pg+'_'
        # item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        yield item
        urls = response.xpath('//div[@id="action"]//li//mip-link[contains(string(),"下一页")]/@href').getall()
        print("下一页",urls)
        for url in urls:            
            yield  scrapy.Request( url ,callback=self.parse_image)

