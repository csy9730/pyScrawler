# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem,TieItem
from scrapy.http import Request
import os

class Tb2Spider(scrapy.Spider):
    name = 'tie'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/6232744345?see_lz=0',]# https://tieba.baidu.com/p/6132114763
    url_set = { start_urls[0]}
    custom_settings = {
        'ITEM_PIPELINES': {
            'tieba.pipelines.MyImagesPipeline': 400,
        }
    }
    def __init__(self,tie ="6232744345",page = 1,*args, **kwargs):
        super(Tb2Spider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://tieba.baidu.com/p/%s?pn=%s' % (tie, page ) ] #  ?see_lz=0         
        self.page = page
    def parse(self, response):
        url = response.url
        allTie = response.xpath("//*[@id='j_p_postlist']/div")  
        for tie in allTie:
            item = TieItem()
            tail_info=tie.xpath(".//div[@class='post-tail-wrap']/span[@class='tail-info']/text()")
            item['url'] =  url
            item['dirName'] = '.' 
            item['layerNum'] =tail_info[-2].get()
            item['createTime'] =tail_info[-1].get()
            item['author'] = tie.xpath(".//a[@class='p_author_name j_user_card']/text()").get() 
            item['content'] = tie.xpath(".//div[@class='d_post_content j_d_post_content ']/text()").get()
            item['imgList'] = tie.xpath(".//div[@class='d_post_content j_d_post_content ']/img[@class='BDE_Image']/@src").getall()
            yield item
        next_pages = response.xpath("//div[@class='l_thread_info']//li/a/@href").getall()
        for page in next_pages:
            if page is not None and page not in Tb2Spider.url_set:
                Tb2Spider.url_set.add(page)   
                page = response.urljoin(page)
                yield Request(page ) # add next page to crawl
    def parse3(self, response):
        allTie = response.xpath("//*[@id='j_p_postlist']/div")  
        item = TieItem()        
        item['dirName'] = '.' 

        # item['createTime'] =allTie[0].xpath(".//div[@class='post-tail-wrap']/span[@class='tail-info']/text()").getall()[-1]
        item['author'] = allTie.xpath(".//a[@class='p_author_name j_user_card']/text()").get() 
        item['url'] =  response.url
        imgList = []
        content = ''
        for tie in allTie:    
            author= tie.xpath(".//a[@class='p_author_name j_user_card']/text()").get() 
            newCon = tie.xpath(".//div[@class='d_post_content j_d_post_content ']/text()").get() 
            if  author == item['author'] :                
                content+= newCon
                imgList.extend( tie.xpath(".//div[@class='d_post_content j_d_post_content ']/img[@class='BDE_Image']/@src").getall())
        item['imgList'] = imgList
        item['content'] = content
        yield item
        next_pages = response.xpath("//div[@class='l_thread_info']//li/a/@href").getall()
        for page in next_pages:
            if page is not None and page not in Tb2Spider.url_set:
                Tb2Spider.url_set.add(page)   
                page = response.urljoin(page)
                yield Request(page ) # add next page to crawl