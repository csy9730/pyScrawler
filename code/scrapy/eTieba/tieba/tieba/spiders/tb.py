# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem

class TbSpider(scrapy.Spider):
	name = 'tb'
	allowed_domains = ['baidu.com']
	start_urls = ['http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0',]
# 'http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search&red_tag=a1178616250'
	def parse(self, response):
		allTie = response.xpath("//ul[@id='thread_list']/li[@class=' j_thread_list clearfix']")
		ii = 0
		for tie in allTie:
			item = TiebaItem()
			ii+=1
			item['layerNum'] = ii
			item['title'] =  tie.xpath("./div/div[2]/div[1]/div[1]/a/@title").extract()[0]
			item['href'] = 'http://tieba.baidu.com/'+tie.xpath("./div/div[2]/div[1]/div[1]/a/@href").extract()[0]
			item['author'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[0]
			item['pointNum'] = tie.xpath(".//div[@class ='col2_left j_threadlist_li_left']/span[@class='threadlist_rep_num center_text']/text()").extract()[0]
			item['replyAuthor'] = tie.xpath(".//div[@class='threadlist_author pull_right']//span[contains(@class,'tb_icon_author')]/@title").extract()[1]
			item['createTime'] = tie.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract()[0]
			item['replyDate'] = tie.xpath(".//span[@class='threadlist_reply_date pull_right j_reply_data']/text()").re('[0-9:\-]+')[0]
			yield item
            # title = tie.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']/a/@title").extract()
            # href = tie.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']/a/@href").extract()[0]		
			# title.encode('UTF-8').decode('UTF-8')
			# author = pic.xpath("./div/div[2]/div[1]/div[2]/span[1]/span[1]/a/text()").extract()
			# author = pic.xpath(	"./div/div[2]/div[1]/div[2]/span[1]/span[1]/a/text()|./div/div[2]/div[1]/div[2]/span[1]/span[2]/a/text()").extract()[0]
			# pointNum = pic.xpath("./div/div[1]/span/text()").extract()[0]
			# replyDate=pic.xpath(".//span[@title='最后回复时间']/text()")	
