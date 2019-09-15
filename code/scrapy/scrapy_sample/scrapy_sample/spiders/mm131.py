# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem

import os

class Mm131Spider(scrapy.Spider):
    name = 'mm131'
    url = "https://www.mm131.net"
    start_urls = ['https://www.mm131.net/',
                  #'https://www.mm131.net/xinggan/2746.html',
                  'https://www.mm131.net/xinggan/3331.html']
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [scrapy.Request(self.start_urls[0],headers=self.header,callback=self.parse_index)]
    def parse(self,response):
        return         
    def parse_index(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://www.mm131.net
                @scrapes https://www.mm131.net/xinggan/
        """
        print(response.request.headers)
        urls = response.xpath(".//li[@class='column-title public-title']/a[@class='more']/@href").getall()
        for url in urls:
            print(url)
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_page)
    def parse_page(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://www.mm131.net/xinggan/
                    https://www.mm131.net/xiaohua/list_2_3.html
                @scrapes https://www.mm131.net/xinggan/
        """
        # urls = response.css("dl.list-left.public-box dd a::(href)").getall() 
        urls = response.xpath(".//dl[@class='list-left public-box']//dd//a/@href").getall()        
        for url in urls:
            if url.find( self.url)<0:
                url = self.url +'/' +url
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_title)
        next_pages = response.xpath(".//dd[@class='page']/a/@href").getall()
        for page in next_pages:
            if page.find( self.url )<0:
                page = self.url+'/' +page
            print( page )
            yield  scrapy.Request( page ,headers=self.header,callback=self.parse_page)
    def parse_title(self, response):
        img_folder = (response.xpath(".//div [@class='content']/h5/text()").get() or '')+'/'     
        total_page = int(response.css('span.page-ch::text').extract_first()[1:-1])
        current_page = int(response.css('span.page_now::text').extract_first())

        # pth = 'images/full/'+item['img_folder']
        # if not os.path.exists(pth):
            # os.mkdir( pth )
        rp ='.' if response.url.rfind('_') == -1 else  '_'
        head, sep, tail = response.url.rpartition(rp)
        for current_page in range(total_page):
            url = head + f'_{current_page+1}.html'
            print( 'parse_image_next:',url)
            yield scrapy.Request(url,headers=self.header,callback=self.parse_image,meta={"img_folder":img_folder})
    def parse_image(self,response):
        """ This function parses images
                @url https://www.mm131.net/xiaohua/616.html
                @scrapes https://img1.mmmw.net/pic/616/1.jpg
        """
        item = ImageItem()
        item['image_urls'] = response.css('div.content-pic img::attr(src)').extract()
        item['referer'] = response.url
        item['title'] = response.xpath(".//div [@class='content']/h5/text()").get()
        item['img_folder'] = response.meta['img_folder']
        item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        return item