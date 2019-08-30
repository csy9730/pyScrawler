# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

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
