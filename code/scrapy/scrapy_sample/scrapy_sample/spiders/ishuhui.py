# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem

# 需要添加 ajax捕抓

class IshuhuiSpider(scrapy.Spider):
    name = 'ishuhui'

    start_urls = [
               # 'https://www.ishuhui.com/',
             'https://www.ishuhui.com/comics/anime/1',
                  #'https://www.mm131.net/xinggan/2746.html',
                  #'https://www.mm131.net/xinggan/3331.html'
                  ]
    header = { #'accept-encoding': 'gzip, deflate, br', 
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer':'https://www.ishuhui.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def start_requests(self):      
        return [scrapy.Request(self.start_urls[0],headers=self.header,meta={"cookiejar":1},callback=self.parse),]
    def parse(self,response):
        print( response.url,"parse")
        id =  response.url.split('/')[-1]
        # print( "id=",id)
        url = "https://prod-api.ishuhui.com/ver/7a801002/anime/detail?id=1&type=comics&.json" #% id
        self.header["referer"] = response.url
        yield  scrapy.Request( url ,headers=self.header,meta={"cookiejar":response.meta["cookiejar"],"referer":response.url},callback=self.parse_title)
    def parse_title(self,response):
        """ This function parses a sample response. Some contracts are mingled
                with this docstring.
                @url https://www.mm131.net
                @scrapes https://www.mm131.net/xinggan/
        """
        print( response.url,"parse_title")
        import json
        #print(response.text)
        dct = json.loads(response.text)
        #print(dct)
        dc = dct["data"]["comicsIndexes"]["1"]["nums"]
        self.header["referer"]=response.meta["referer"]
        for pg in dc:
            d = dc[pg]
            for p in d:                             
                url = d[p][0]["url"].replace("http:","https:")
                print("url=",url)
                if len(url)>7:                
                    yield  scrapy.Request( url ,meta={"cookiejar":response.meta["cookiejar"],"referer":response.meta["referer"]},headers=self.header,callback=self.parse_image)
        print("finished")
        return
        url = dct["data"]["comicsIndexes"]["1"]["nums"]["1-50"]["1"][0]["url"]
        urls = response.xpath('.//div[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//div//a/@href').getall()
        for url in urls:
            print(url)
            yield  scrapy.Request( url ,headers=self.header,callback=self.parse_image)
    def parse_image(self, response):
        print(" parse_image")
        item = ImageItem()
        item['image_urls'] = response.xpath('.//ul[@class="comit-contain"]//li//img/@src').getall()
        item['referer'] = response.url
        item['title'] = response.xpath('.//h1[@id="comicTitle"]//span[@class="title-comicHeading"/text()').get()
        # item['datetime'] = response.xpath(".//div [@class='content']/div[@class='content-msg']/text()").get()
        yield item

