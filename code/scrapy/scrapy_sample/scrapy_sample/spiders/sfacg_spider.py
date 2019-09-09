# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem


class Mm131Spider(scrapy.Spider):
    name = 'sgacg'

    start_urls = ['https://manhua.sfacg.com/mh/LYB/' ]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            "referer":'https://manhua.sfacg.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [scrapy.Request(self.start_urls[0],headers=self.header,callback=self.parse,meta={"cookiejar":1},)]
    def parse(self,response):
        return self.parse_title(response)
    def parse_title(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://manhua.sfacg.com/mh/LYB/
                @scrapes /mh/LYB/65407/
        """
        print(response.request.headers)
        urls = response.xpath(".//div[@class='comic_Serial_list']/a/@href").getall()
        import copy

        for url in urls:
            url2 = "https://manhua.sfacg.com"+url 
            print(url2)
            header = copy.copy(self.header  )
            header["referer"] = url2
            yield  scrapy.Request( url2, meta={"cookiejar":response.meta["cookiejar"],"referer":url2},headers=header,callback=self.parse_image)
    def parse_image(self, response):
        item = ImageItem()
        print(response.request.headers)
        item['image_urls'] = response.xpath('.//a/img/@src').getall()
        item['referer'] = response.url
        item['title'] = response.xpath('.//div[@class="wrap"]/span/text()').get()
        # item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        yield item
        urls = response.xpath(".//a[@class='page_fleet']//text()").getall()
        for url in urls:
            print(url)
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_image, meta={"cookiejar":response.meta["cookiejar"]},)

