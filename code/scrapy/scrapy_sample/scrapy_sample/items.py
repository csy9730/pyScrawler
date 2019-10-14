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


class ChapterItem(scrapy.Item):
    chapter_Url = scrapy.Field()#章节url
    _id = scrapy.Field()#章节id
    novel_Name = scrapy.Field()#小说名称
    chapter_Name = scrapy.Field()#章节名称
    chapter_Content = scrapy.Field()#内容
    novel_ID = scrapy.Field()#小说id
    is_Error = scrapy.Field()#是否异常
 
class BookItem(scrapy.Item):
    _id = scrapy.Field() #小说id，用于定位章节信息，章节唯一
    novel_Name = scrapy.Field() #小说名称
    novel_Writer = scrapy.Field()#小说作者
    novel_Type = scrapy.Field()#小说类型
    novel_Status = scrapy.Field()#小说状态，连载或者完结
    novel_UpdateTime = scrapy.Field()#最后更新时间
    novel_Words = scrapy.Field() #总字数
    novel_ImageUrl = scrapy.Field()#封面图片
    novel_AllClick = scrapy.Field()#总点击
    novel_MonthClick = scrapy.Field()#月点击
    novel_WeekClick = scrapy.Field()#周点击
    novel_AllComm = scrapy.Field()#总推荐
    novel_MonthComm = scrapy.Field()#月推荐
    novel_WeekComm = scrapy.Field()#周推荐
    novel_Url = scrapy.Field()#小说url
    novel_Introduction = scrapy.Field()#小说简介

class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()