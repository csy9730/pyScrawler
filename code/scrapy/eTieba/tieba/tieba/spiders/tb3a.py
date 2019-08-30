# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem
from scrapy.http import Request
import urllib.parse  as  urlparse

class Tb3aSpider(scrapy.Spider):
    name = 'tb3a'
    allowed_domains = ['baidu.com']
   #  start_urls = ['http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0']
    url_set = set() 
    header = { #'accept-encoding': 'gzip, deflate, br', 
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user_agent':  'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
    def __init__(self,tieba ="python",page = 0,*args, **kwargs):
        super(Tb3aSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s' % (tieba, page*50 ) ] 
        self.page = page
        self.tieba = tieba
    """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
    def start_requests(self):      

        return [Request(self.start_urls[0],headers=Tb3aSpider.header,callback=self.parse)]

    def parse(self, response):
        print(response.request.headers,response.url)
        # print("response",response.text,len(response.text))
        allTie = response.xpath("//ul[@id='thread_list']//li[@class=' j_thread_list clearfix']")
        ii = 0

        # print(response.url.re("&pn=(\\d+)")[1])
        for tie in allTie:
            item = TiebaItem()
            ii += 1
            print("i=",ii )
            item['pageNum'] = self.page
            item['layerNum'] = ii
            item['tieba'] = self.tieba
            item['title'] = tie.xpath("./div/div[2]/div[1]/div[1]/a/@title").extract()[0] 
            item['href'] = 'http://tieba.baidu.com/' + tie.xpath("./div/div[2]/div[1]/div[1]/a/@href").extract()[0]
            item['author'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[0]
            item['pointNum'] = tie.xpath( ".//div[@class ='col2_left j_threadlist_li_left']/span[@class='threadlist_rep_num center_text']/text()").extract()[0]
            item['replyAuthor'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[1]
            item['createTime'] = tie.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract()[0]
            item['replyDate'] = tie.xpath(".//span[@class='threadlist_reply_date pull_right j_reply_data']/text()").re('[0-9:\-]+')[0]
            yield item
        next_pageExt = response.xpath("//*[@id='frs_list_pager']/a[@class='next pagination-item ']/@href")
        next_pages = next_pageExt.extract()
        for page in next_pages:
            if page is not None and page not in Tb3aSpider.url_set:
                # print( page)
                self.page = int( int(next_pageExt.re("&pn=(\\d+)")[0])/50)
                Tb3aSpider.url_set.add(page)   
                page = response.urljoin(page)
                yield Request(page,headers=Tb3aSpider.headers, callback=self.parse) # add next page to crawl
