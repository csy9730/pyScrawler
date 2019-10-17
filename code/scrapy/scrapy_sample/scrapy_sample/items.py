# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from .utils import removeDirtyChar
from scrapy.loader.processors import Join, MapCompose, TakeFirst,Compose
from w3lib.html import remove_tags


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
    referer = scrapy.Field(output_processor=TakeFirst())#章节url    
    novel = scrapy.Field(output_processor=TakeFirst())#小说名称
    chapter = scrapy.Field(output_processor=TakeFirst())#章节名称
    text = scrapy.Field(
        output_processor=Compose( Join(separator=''),removeDirtyChar ))
    #内容
    bookId = scrapy.Field()#小说id
    _id = scrapy.Field()#章节id

class NovelItem(scrapy.Item):
    _id = scrapy.Field(output_processor=TakeFirst()) #小说id，用于定位章节信息，章节唯一
    novel = scrapy.Field(output_processor=TakeFirst()) #小说名称
    author = scrapy.Field(output_processor=TakeFirst())#小说作者
    tags = scrapy.Field(output_processor=Join(','))#小说类型
    status = scrapy.Field(output_processor=Compose(TakeFirst(),removeDirtyChar))#小说状态，连载或者完结
    updateTime = scrapy.Field(output_processor=TakeFirst())#最后更新时间
    wordCount = scrapy.Field(output_processor=TakeFirst()) #总字数
    cover = scrapy.Field(output_processor=TakeFirst())#封面图片
    referer = scrapy.Field(output_processor=TakeFirst())#小说url
    introduction = scrapy.Field(output_processor= Compose(Join(),removeDirtyChar))#小说简介
    latestChapter = scrapy.Field(output_processor=TakeFirst())#小说简介
    novel_AllClick = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#总点击
    novel_MonthClick = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#月点击
    novel_WeekClick = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#周点击
    novel_AllComm = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#总推荐
    novel_MonthComm = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#月推荐
    novel_WeekComm = scrapy.Field(output_processor=Compose(TakeFirst(),str.strip,int))#周推荐  
   
class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
class ZuopinjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_name = scrapy.Field()
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_content = scrapy.Field()

class NewsItem(Item):
    title = Field()
    text = Field()
    datetime = Field()
    source = Field()
    url = Field()
    website = Field()
