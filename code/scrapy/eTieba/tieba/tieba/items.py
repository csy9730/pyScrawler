# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    pointNum = scrapy.Field()
    href = scrapy.Field()

    replyAuthor = scrapy.Field()
    replyDate = scrapy.Field()
    createTime = scrapy.Field()

    layerNum = scrapy.Field()
    pageNum = scrapy.Field()
    tieba = scrapy.Field() 
class TieItem(scrapy.Item):
    # define the fields for your item here like:
    # title = scrapy.Field() # special
    url = scrapy.Field() #  unique 
    # tieba = scrapy.Field()
    dirName = scrapy.Field()

    author = scrapy.Field()
    replyNum = scrapy.Field()
    createTime = scrapy.Field()

    layerNum = scrapy.Field()
    pageNum = scrapy.Field()

    content = scrapy.Field()
    imgList = scrapy.Field()
    imgPathList = scrapy.Field()