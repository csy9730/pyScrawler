# -*- coding: utf-8 -*-
##########################################################################
# author
#     chaosju
# description:
#     Define your item pipelines here
#     save or process  your spider's data 
# attention:
#     Don't forget to add your pipeline to the ITEM_PIPELINES setting in setting file
# help document:
#     See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
########################################################################
import re
from twisted.enterprise import adbapi
from scrapy.http import Request
from CpsecSpiders.items import CpsecspidersItem
import CpsecSpiders.settings  as settings
from scrapy.exceptions import DropItem
# from CpsecSpiders.CpsecSpiderUtil import  spiderutil as sp


import MySQLdb
import MySQLdb.cursors
class CpsecspidersPipeline(object):
    ''''''
    def __init__(self):
        #connect to mysql DB
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            # cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True)
    def process_item(self, item, spider):
        """
        if  spider.name == '360search' or spider.name == 'baidu' or spider.name == 'sogou':
            query = self.dbpool.runInteraction(self._conditional_insert, item)
            return item
        elif  spider.name == 'ifengSpider':
            query = self.dbpool.runInteraction(self._conditional_insert_ifeng, item)
            return item
        elif spider.name == 'chinanews':
            query = self.dbipool.runInteraction(self._conditional_insert_chinanews, item)
            return item
        else:
        """    
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        for i in range(len(item['article_name'])):
            tx.execute("select * from article_info as t where t.id = %s", (item['article_id'][i], ))
            result = tx.fetchone()
            #lens = sp.isContains(item['article_name'][i])

            #if not result and lens != -1:
            #数据不存在，则插入
            if not result:
                print( type(item['article_id'][i] ),item['article_id'][i])
                # sql = 'insert into article_info(id,article_name,article_time,article_url,crawl_time,praise_num,comment_num,article_from,article_author) values (%s, "%s", "%s', '%s, %s, %s, %s, %s, %s)'  % (item['article_id'][i],item['article_name'][i],item['article_time'][i],item['article_url'][i],item['crawl_time'][i],item['click_num'][i],item['reply_num'][i],item['article_from'][i],item['article_author'][i])
                # print(sql)
                
                sql = 'insert into article_info(id,article_name) values (%d, "%s")'%(item['article_id'][i],item['article_name'][i])
                print(sql)
                tx.execute(\
                  'insert into article_info(id,article_name) values (%d, "%s")'%(item['article_id'][i],item['article_name'][i]))
                
                # tx.execute(\
                #   'insert into article_info(id,article_name,article_time,article_url,crawl_time,praise_num,comment_num,article_from,article_author) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'%(item['article_id'][i],item['article_name'][i],item['article_time'][i],item['article_url'][i],item['crawl_time'][i],item['click_num'][i],item['reply_num'][i],item['article_from'][i],item['article_author'][i]))
                #tx.execute(\
                #  'insert into article_content(id,article_content) values (%d, "%s")'%( item['article_id'][i],item['article_content'][i]))