# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
from scrapy.http import Request

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
    def parse(self,response):
        """ This function parses pages
            @url https://www.mzitu.com
            @scrapes https://www.mzitu.com/193336  https://www.mzitu.com/page/2/
        """
        print(response.request.headers)
        urls = response.xpath('//ul[@id="pins"]//li//span//@href').getall()
        for url in urls:
            print(url)
            yield  Request(self.urlpre+ url ,headers=self.header,callback=self.parse_article)
        page_urls= response.xpath('//div[@class="nav-links"]//a/@href').getall()
        for url in page_urls:
            yield  Request( url ,headers=self.header,callback=self.parse)
        
    def parse_article(self,response):
        image_urls = response.xpath('//div[@class="main-image"]//a/img/@src').getall()
        title = response.xpath("//h2//text()").get()
        # datetime = response.xpath(".//div[@class='metaLeft']//div[@class='month_Year']/text()").get()
        # count = response.xpath('//div[@class="pagenavi"]//a/span/text()').getall()[-2]
        page_urls = response.xpath('//div[@class="pagenavi"]//a/@href').getall() 
        for page in page_urls:             
            yield  Request( page ,headers=self.header,callback=self.parse_image, meta={"img_folder":img_folder})
    def parse_image(self,response):
        image_urls = response.xpath('//div[@class="main-image"]//a/img/@src').getall()
        title = response.xpath("//h2//text()").get()
        img_folder = title+'/'
        # datetime = response.xpath(".//div[@class='metaLeft']//div[@class='month_Year']/text()").get()
        return ImageItem(image_urls=image_urls,referer =response.url,title = title,img_folder = response.meta['img_folder'])
