import scrapy
from scrapy_sample.items import BodyItem
import urllib.parse

class DocScrapySpider(scrapy.Spider):
    """我的CSDN所有文章和链接的爬虫"""
    name = 'doc_scrapy'
    start_urls = [#'https://doc.scrapy.org/' ,
                    'https://scrapy-chs.readthedocs.io',
                ]

    def parse(self, response):     
        content = response.css('div.document').get()
        title = response.css('title').get()
        href =  response.css('div.document dt a::attr(href)').getall()
        image_urls = response.css('div.document img::attr(src)').getall()
        yield  {"content":content,"title":title,"image_urls":image_urls,"referer":response.url }
        #return 
        for h in href:
            yield scrapy.Request( urllib.parse.urljoin(response.url,h) )
       

