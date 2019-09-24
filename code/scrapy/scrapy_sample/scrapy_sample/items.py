# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    img_folder = scrapy.Field()
    referer = scrapy.Field()
    title = scrapy.Field()
    datetime = scrapy.Field()

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
