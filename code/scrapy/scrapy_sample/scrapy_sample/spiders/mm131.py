# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem


class Mm131Spider(scrapy.Spider):
    name = 'mm131'

    start_urls = ['https://www.mm131.net/',
                  #'https://www.mm131.net/xinggan/2746.html',
                  'https://www.mm131.net/xinggan/3331.html']
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [scrapy.Request(self.start_urls[0],headers=self.header,callback=self.parse)]
    def parse(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://www.mm131.net
                @scrapes https://www.mm131.net/xinggan/
        """
        print(response.request.headers)
        urls = response.xpath(".//li[@class='column-title public-title']/a[@class='more']/@href").getall()
        for url in urls:
            print(url)
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_title)
    def parse_title(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://www.mm131.net/xinggan/
                @scrapes https://www.mm131.net/xinggan/
        """
        # urls = response.css("dl.list-left.public-box dd a::(href)").getall() 
        urls = response.xpath(".//dl[@class='list-left public-box']//dd//a/@href").getall()        
        for url in urls:
            if url.find("https://www.mm131.net")<0:
                url = self.start_urls[0]+url
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_image)
        next_pages = response.xpath(".//dd[@class='page']/a/@href").getall()
        for page in next_pages:
            if page.find("https://www.mm131.net")<0:
                page = self.start_urls[0]+page
            print( page )
            yield  scrapy.Request( page ,headers=self.header,callback=self.parse_title)
    def parse_image(self, response):
        item = ImageItem()
        item['image_urls'] = response.css('div.content-pic img::attr(src)').extract()
        item['referer'] = response.url
        item['title'] = response.xpath(".//div [@class='content']/h5/text()").get()
        item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        yield item
        total_page = int(response.css('span.page-ch::text').extract_first()[1:-1])
        current_page = int(response.css('span.page_now::text').extract_first())
        print( current_page,'~',total_page)
        if current_page < total_page:
            rp ='.' if response.url.rfind('_') == -1 else  '_'
            head, sep, tail = response.url.rpartition(rp)
            url = head + f'_{current_page+1}.html'
            print( 'parse_image_next:',url)
            yield scrapy.Request(url,headers=self.header,callback=self.parse_image)
