# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from .utils import removeDirtyChar
from scrapy.loader.processors import Join, MapCompose, TakeFirst,Compose

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field() 
    images = scrapy.Field() # record output sha1
    img_folder = scrapy.Field(
        output_processor=Compose( TakeFirst (),removeDirtyChar,lambda x:x+'/' ))

    title = scrapy.Field(
        output_processor=Compose( TakeFirst (),removeDirtyChar ))
    referer = scrapy.Field(output_processor= TakeFirst() )
    datetime = scrapy.Field( output_processor=Compose( TakeFirst (),removeDirtyChar,str.strip ))

class BookItem(scrapy.Item):
    title  = scrapy.Field()
    author = scrapy.Field()
    descrption =  scrapy.Field()
    tag = scrapy.Field()
    click_num = scrapy.Field()
    datetime = scrapy.Field()
    misc = scrapy.Field()

class BudejieItem(scrapy.Item):
    username = scrapy.Field()
    content = scrapy.Field()


class CsdnBlogItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class BlogListItem(scrapy.Item):
    title = scrapy.Field()
    referer = scrapy.Field()
    href = scrapy.Field()
    description = scrapy.Field()
    datetime = scrapy.Field()
    read_num = scrapy.Field()
    reply_num = scrapy.Field()

class BodyItem(scrapy.Item):
    referer = scrapy.Field()
    body = scrapy.Field()
    image_urls = scrapy.Field() 
    title = scrapy.Field()