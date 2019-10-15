# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_sample.items import NovelItem,ChapterItem
import re
from scrapy.http import Request
from scrapy.loader import ItemLoader
# https://www.23us.so/
# "https://www.23us.so/top/allvisit_1.html",https://www.23us.so/list/3_1.html
# http://www.23us.so/xiaoshuo/414.html
# https://www.23us.so/files/article/html/0/414/index.html
# https://www.23us.so/files/article/html/0/414/5361947.html
# 
class A23usSpider(CrawlSpider):
    name = '23us'
    allowed_domains = ["23us.so","ddxsku.com"] #允许爬取的域名
    start_urls = [
        "https://www.ddxsku.com/xiaoshuo/41562.html",
        #"http://www.23us.so/xiaoshuo/414.html"
    # "https://www.23us.so/",
    #        "https://www.23us.so/top/allvisit_1.html"
    ]
    rules=(
        # Rule(LinkExtractor(allow=("list/\d*_\d*.html"),restrict_xpaths=".//div[@class='main m_menu']//li")),
        # Rule(LinkExtractor(allow=("list/\d*_\d*.html"),restrict_xpaths=".//div[@id ='pagelink']")),
        
        Rule(LinkExtractor(allow=("xiaoshuo/\d*\.html") ,restrict_xpaths=".//dl[@id='content']//dd"),callback="parse_book_message",follow=True),
        Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?.index.html"),restrict_xpaths=".//*[@id='content']//dd//div"),follow=True),
        Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?/\d*?.html"),restrict_xpaths=(".//*[@id='at']//tr//td")),callback="parse_chapter_content",follow=False),
        # Rule(LinkExtractor(allow=(".*")),follow=True),
    )
    def parse_start_url(self, response):          
        return self.parse_book_message(response)
    def parse_book_message(self,response):
        l = ItemLoader(item=NovelItem(), response=response)
        l.add_xpath('novel', "//dl[@id='content']/dd[1]/h1/text()")
        l.add_xpath('cover', "//a[@class='hst']/img/@src")
        l.add_xpath('tags', '//table[@id="at"]/tr[1]/td[1]/a/text()') 
        l.add_xpath('author', '//table[@id="at"]/tbody//tr[1]/td[2]/text()') 
        l.add_xpath('status', '//table[@id="at"]//tr[1]/td[3]/text()') 
        l.add_xpath('updateTime', ".//table[@id='at']//tr[2]/td[3]/text()") 

        l.add_xpath('novel_AllClick', ".//table[@id='at']//tr[3]/td[1]/text()") 
        l.add_xpath('novel_MonthClick', ".//table[@id='at']//tr[3]/td[2]/text()") 
        l.add_xpath('novel_WeekClick', ".//table[@id='at']//tr[3]/td[3]/text()") 
        l.add_xpath('novel_AllComm', ".//table[@id='at']//tr[4]/td[1]/text()") 
        l.add_xpath('novel_MonthComm', ".//table[@id='at']//tr[4]/td[3]/text()") 
        l.add_xpath('novel_WeekComm', ".//table[@id='at']//tr[4]/td[3]/text()") 

        l.add_xpath('introduction', '//dl//dd/p[2]')  # .replace("&nbsp;","")
        l.add_value('referer', response.url)
        return l.load_item()
        # _id = int(response.url.split("/")[-1].split(".")[0])
        # wordCount = self.getNumber("".join(text.xpath(".//table[@id='at']/tr[2]/td[2]/text()"))) if response.xpath(".//table[@id='at']/tr[2]/td[2]/text()") else "None"       
        # url = response.xpath(".//*[@id='content']//dd//div//a[@class='read']/@href").get()
        # yield Request( url,callback= self.parse_book_chapter )  
    def parse_book_chapter(self,response):
        print("parse_book_chapter")
        return
        urls = response.xpath( ".//*[@id='at']//tr//td//a/@href").getall()
        print(urls)
        for url in urls:
            yield Request( url,callback= self.parse_chapter_content )            
    def parse_chapter_content(self,response):
        l = ItemLoader(item=ChapterItem(), response=response)
        l.add_xpath('novel', ".//p[@class='fr']/following-sibling::a[3]/text()")
        l.add_xpath('chapter', ".//h1[1]/text()")
        l.add_xpath('text', './/dd[@id="contents"]/text()')        
        l.add_value('referer', response.url)
        return l.load_item()
        # _id=int(response.url.split("/")[-1].split(".")[0]),
        # novel_ID = response.url.split("/")[-2]
        
    


class BiqukanSpider(scrapy.Spider):
    name = 'biqukan'
    allowed_domains = ["biqukan.com"] #允许爬取的域名
    base_url = "https://www.biqukan.com"
    start_urls = [
        "https://www.biqukan.com/69_69348/",
    ]
    def parse(self,response):
        l = ItemLoader(item=NovelItem(), response=response)
        l.add_xpath('novel', '//div[@class="info"]//h2/text()')
        l.add_xpath('introduction', '//div[@class="info"]//div[@class="intro"]//text()')
        l.add_xpath('cover', '//div[@class="cover"]//img/@src')  
        _info = l.nested_xpath('//div[@class="info"]//div[@class="small"]')
        _info.add_xpath('author', '//span[1]/text()')
        _info.add_xpath('tags', '//span[2]/text()')
        _info.add_xpath('status', '//span[3]/text()')
        _info.add_xpath('wordCount', '//span[4]/text()')
        _info.add_xpath('updateTime', '//span[5]/text()')
        _info.add_xpath('latestChapter', '//span[6]/a/text()')   
        yield l.load_item()
        urls = response.xpath( '//div[@class="listmain"]//a/@href').getall() # '/69_69348/44099638.html'
        for url in urls:
            yield Request( self.base_url+url,callback= self.parse_chapter_content )         
    def parse_chapter_content(self,response):
        l = ItemLoader(item=ChapterItem(), response=response)
        l.add_xpath('novel', '//div[@class="path"]//a[2]/text()')
        l.add_xpath('chapter', '//h1/text()')
        l.add_xpath('text', '//div[@id="content"]/text()')        
        l.add_value('referer', response.url) 
        return l.load_item()
        
