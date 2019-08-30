# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem,TieItem
from scrapy.http import Request
from urllib.parse import urlparse
import os

class Tb3Spider(scrapy.Spider):
    name = 'tb3'
    allowed_domains = ['baidu.com']
   #  start_urls = ['http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0']
    url_set = set() 
    header = { #'accept-encoding': 'gzip, deflate, br', 
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user_agent':  'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def __init__(self,tieba ="python",page = 0,*args, **kwargs):
        super(Tb3Spider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s' % (tieba, page*50 ) ] 
        self.page = page
        self.tieba = tieba
    """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
    def start_requests(self):      

        return [Request(self.start_urls[0],headers=Tb3Spider.header,callback=self.parse)]

    def parse(self, response):
        print(response.request.headers,response.url)
        # print("response",response.text,len(response.text))
        allTie = response.xpath("//ul[@id='thread_list']//li[@class=' j_thread_list clearfix']")
        ii = 0

        # print(response.url.re("&pn=(\\d+)")[1])
        items = []
        for tie in allTie:
            item = TiebaItem()
            ii += 1
            item['pageNum'] = self.page
            item['layerNum'] = ii
            item['tieba'] = self.tieba
            item['title'] = tie.xpath("./div/div[2]/div[1]/div[1]/a/@title").extract()[0] 
            item['href'] = 'https://tieba.baidu.com' + tie.xpath("./div/div[2]/div[1]/div[1]/a/@href").extract()[0]
            item['author'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[0]
            item['pointNum'] = tie.xpath( ".//div[@class ='col2_left j_threadlist_li_left']/span[@class='threadlist_rep_num center_text']/text()").extract()[0]
            item['replyAuthor'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[1]
            item['createTime'] = tie.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract()[0]
            item['replyDate'] = tie.xpath(".//span[@class='threadlist_reply_date pull_right j_reply_data']/text()").re('[0-9:\-]+')[0]
            items.append(item)

        for item in items:    # yield item
            dirName = os.path.basename(urlparse(item["href"] ).path)
            # print("dirName=",dirName )
            yield Request(item['href'] ,headers=Tb3Spider.header,meta = {'item':item,'dirName':dirName},callback=self.parse_tie)
        next_pageExt = response.xpath("//*[@id='frs_list_pager']/a[@class='next pagination-item ']/@href")
        next_pages = next_pageExt.extract()
        for page in next_pages:
            if page is not None and page not in Tb3Spider.url_set:
                self.page = int( int(next_pageExt.re("&pn=(\\d+)")[0])/50)
                Tb3Spider.url_set.add(page)   
                page = response.urljoin(page)
                yield Request(page,headers=Tb3Spider.header,callback=self.parse)
    def parse_tie(self, response):
        allTie = response.xpath("//*[@id='j_p_postlist']/div")
        dirName = response.meta['dirName']
        print(response.url,dirName)    
        for tie in allTie:
            item = TieItem()
            tail_info=tie.xpath(".//div[@class='post-tail-wrap']/span[@class='tail-info']/text()")
            item['dirName']=dirName #            
            item['layerNum'] =tail_info[-2].get()
            item['createTime'] =tail_info[-1].get()
            item['author'] = tie.xpath("//a[@class='p_author_name j_user_card']/text()").get() 
            item['content'] = tie.xpath(".//div[@class='d_post_content j_d_post_content ']/text()").get()
            item['imgList'] = tie.xpath(".//div[@class='d_post_content j_d_post_content ']/img[@class='BDE_Image']/@src").getall()
            yield item
        next_pages = response.xpath("//div[@class='l_thread_info']//li/a/@href").getall()
        for page in next_pages:
            if page is not None and page not in Tb3Spider.url_set:
                # print( page)
                Tb3Spider.url_set.add(page)   
                page = response.urljoin(page)
                yield Request(page,callback=self.parse_tie,meta = {'dirName':dirName})# add next page to crawl