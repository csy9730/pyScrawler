# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiaoshuos.items import BookItem,ChapterItem
import re
import bs4 as  BeautifulSoup
from scrapy.http import Request

class A23usSpider(scrapy.Spider):
    name = '23us'
    allowed_domains = ["23us.so"] #允许爬取的域名
    start_urls = ["http://www.23us.so/xiaoshuo/414.html"]#种子url
    #跟进的url
    rules=(
        Rule(LinkExtractor(allow=("xiaoshuo/\d*\.html")),callback="parse_book_message",follow=True),
        Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?.index.html")),callback="parse_book_chapter",follow=True),
        Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?/\d*?.html")),callback="parse_chapter_content",follow=True),
        # Rule(LinkExtractor(allow=(".*")),follow=True),
    )
    def parse( self,response):
        return self.parse_book_message(response)
    def parse_book_message(self,response):
        if not response.body:
            print(response.url+"已经被爬取过了，跳过")
            return;
        ht = response.body.decode("utf-8")
        text = response #html.fromstring(ht)
        novel_Url = response.url
        novel_Name = response.xpath(".//dl[@id='content']/dd[1]/h1/text()").get()
        novel_ImageUrl = response.xpath(".//a[@class='hst']/img/@src").get()
        novel_ID = int(response.url.split("/")[-1].split(".")[0])
        novel_Type = text.xpath(".//table[@id='at']/tr[1]/td[1]/a/text()").get()
        novel_Writer = (text.xpath(".//table[@id='at']/tbody//tr[1]/td[2]/text()").get()) 
        novel_Status = (text.xpath(".//table[@id='at']//tr[1]/td[3]/text()").get()) 
        # novel_Words = self.getNumber("".join(text.xpath(".//table[@id='at']/tr[2]/td[2]/text()"))) if response.xpath(".//table[@id='at']/tr[2]/td[2]/text()") else "None"
        novel_UpdateTime = (text.xpath(".//table[@id='at']//tr[2]/td[3]/text()").get())
        novel_AllClick = int((text.xpath(".//table[@id='at']//tr[3]/td[1]/text()").get()) )
        novel_MonthClick = int((text.xpath(".//table[@id='at']//tr[3]/td[2]/text()").get()) )
        novel_WeekClick = int((text.xpath(".//table[@id='at']//tr[3]/td[3]/text()").get()))
        novel_AllComm = int((text.xpath(".//table[@id='at']//tr[4]/td[1]/text()").get()) )
        novel_MonthComm = int((text.xpath(".//table[@id='at']//tr[4]/td[3]/text()").get()) )
        novel_WeekComm = int((text.xpath(".//table[@id='at']//tr[4]/td[3]/text()").get()))
        pattern = re.compile('<p>(.*)<br')
        match = pattern.search(ht)
        novel_Introduction = "".join(match.group(1).replace("&nbsp;","")) if match else "None"
        #封装小说信息类
        bookitem = BookItem(
            novel_Type = novel_Type[0],
            novel_Name = novel_Name,
            novel_ImageUrl = novel_ImageUrl,
            _id = novel_ID,   #小说id作为唯一标识符
            novel_Writer = novel_Writer,
            novel_Status = novel_Status,
            # novel_Words = novel_Words,
            novel_UpdateTime = novel_UpdateTime,
            novel_AllClick = novel_AllClick,
            novel_MonthClick = novel_MonthClick,
            novel_WeekClick = novel_WeekClick,
            novel_AllComm = novel_AllComm,
            novel_MonthComm = novel_MonthComm,
            novel_WeekComm = novel_WeekComm,
            novel_Url = novel_Url,
            novel_Introduction = novel_Introduction,
        )

        yield bookitem
        url = response.xpath(".//*[@id='content']//dd//div//a[@class='read']/@href").get()
        yield Request( url,callback= self.parse_book_chapter )  
    def parse_book_chapter(self,response):
        print( "parse_book_chapter",response.url)
        urls = response.xpath( ".//*[@id='at']//tr//td//a/@href").getall()
        print(urls)
        for url in urls:
            print(url)
            yield Request( url,callback= self.parse_chapter_content )            
    def parse_chapter_content(self,response):
        if not response.body:
            print(response.url+"已经被爬取过了，跳过")
            return;
        ht = response.body.decode('utf-8')
        text = response # html.fromstring(ht)
        soup = BeautifulSoup(ht)
        novel_ID = response.url.split("/")[-2]
        novel_Name = text.xpath(".//p[@class='fr']/following-sibling::a[3]/text()")[0]
        chapter_Name = text.xpath(".//h1[1]/text()")[0]
        '''
        chapter_Content = "".join("".join(text.xpath(".//dd[@id='contents']/text()")).split())
        if len(chapter_Content) < 25:
        chapter_Content = "".join("".join(text.xpath(".//dd[@id='contents']//*/text()")))
        pattern = re.compile('dd id="contents".*?>(.*?)</dd>')
        match = pattern.search(ht)
        chapter_Content = "".join(match.group(1).replace("&nbsp;","").split()) if match else "爬取错误"
        '''
        result,number = re.subn("<.*?>","",str(soup.find("dd",id='contents')))
        chapter_Content = "".join(result.split())
        print(len(chapter_Content))
        novel_ID = response.url.split("/")[-2]
        return ChapterItem(
            chapter_Url = response.url,
            _id=int(response.url.split("/")[-1].split(".")[0]),
            novel_Name=novel_Name,
            chapter_Name=chapter_Name,
            chapter_Content= chapter_Content,
            novel_ID = novel_ID,
            is_Error = len(chapter_Content) < 3000
            )
    

