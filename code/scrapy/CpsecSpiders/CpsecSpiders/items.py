# s*- coding: utf-8 -*-
########################################################################
# author:
#    chaosju 
#
# decription:
#     Define here the models for your scraped items
#
# help documentation:
#     http://doc.scrapy.org/en/latest/topics/items.html
#######################################################################
from scrapy.item import Item, Field

class CpsecspidersItem(Item):
    article_url = Field()
    article_id = Field()  # SQL ID == hash(url)

    article_name = Field() # title
    article_content = Field()
    article_time = Field() 
    article_author =Field()
    article_from = Field()
    click_num = Field()
    reply_num = Field()
    
    crawl_time = Field()

