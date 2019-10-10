# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem
import  re

class SfacgSpider(scrapy.Spider):
    name = 'sgacg'

    start_urls = ['https://manhua.sfacg.com/mh/LYB/', ]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # "referer":'https://manhua.sfacg.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        self.fJsonUrl= lambda x: x.find("Utility")>=0
        return [scrapy.Request(self.start_urls[0],headers=self.header,callback=self.parse,meta={"cookiejar":1}),]
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
            yield  scrapy.Request( url2, meta={"cookiejar":response.meta["cookiejar"],"referer":url2},headers=header,callback=self.parse_js)
    def parse_js(self,response):
        jsUrl =response.xpath(".//head//script/@src").getall()
        title = response.xpath('.//div[@class="wrap"]/span/text()').get()
        urls =filter(self.fJsonUrl, jsUrl)
        print(urls)
        for url in urls:
            yield  scrapy.Request( "https:"+url, meta={"cookiejar":response.meta["cookiejar"],"referer":response.url,"title":title},
            headers=self.header,callback=self.parse_jsonImg)
    def parse_jsonImg(self,response):        
        """var comicName = "琅琊榜";var nextVolume="#";var preVolume="#";var picCount = 9;var picAy = new Array();var hosts = ["http://coldpic.sfacg.com","http://coldpic.sfacg.com", "http://ltpic.sfacg.com"];picAy[0] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/001_764.jpg";picAy[1] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/002_761.jpg";picAy[2] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/003_340.jpg";picAy[3] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/004_581.jpg";picAy[4] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/005_985.jpg";picAy[5] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/006_672.jpg";picAy[6] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/007_272.jpg";picAy[7] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/008_851.jpg";picAy[8] = "/Pic/OnlineComic4/LYB/ZP/0003_7815/009_256.jpg";"""
        print(response.text)
        imgUrl = re.findall(r"=\s\"([\w\d_/]+.jpg)\"",response.text)
        print(imgUrl,len(imgUrl))
        item = ImageItem()
        print(response.request.headers)
        item['image_urls'] = ["http://coldpic.sfacg.com"+img for img in imgUrl]
        item['title'] = response.meta["title"]
        item['referer'] = response.url
        return item

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

