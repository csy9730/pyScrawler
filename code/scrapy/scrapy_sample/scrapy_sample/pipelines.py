# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo


class BudejieMongoPipeline(object):
    "将百思不得姐段子保存到MongoDB中"
    collection_name = 'jokes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'budejie')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


# import psycopg2


class BudejiePostgrePipeline(object):
    "将百思不得姐段子保存到PostgreSQL中"

    def __init__(self):
        self.connection = psycopg2.connect("dbname='test' user='postgres' password='12345678'")
        self.connection.autocommit = True

    def open_spider(self, spider):
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('insert into joke(author,content) values(%s,%s)', (item['username'], item['content']))
        return item


from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy_sample.items import ImageItem

class RawFilenameImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if not isinstance(item, ImageItem):
            return
        requests = super().get_media_requests(item, info)
        
        for req in requests:
            # req.headers.appendlist("referer", item['referer'])
            # req.headers["referer"]=item['referer']
            # req.headers[b'User-Agent'] = b'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' 
            req.meta["img_folder"] = item["img_folder"] or ''   
            # print(req.headers)              
        return requests

        # for image_url in item['image_urls']:
        #    yield Request(url=image_url,headers={'Referer':item['header_referer']})
    def file_path(self, request, response=None, info=None):        
        url = request.url   
        print(request.headers)
        # print( 'full/{1}{0}'.format( url.split('/')[-1], request.meta["img_folder"]) )
        return 'full/{1}{0}'.format( url.split('/')[-1],  request.meta["img_folder"])

        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        # return 'full/%s.jpg' % (image_guid)
    def item_completed2(self, results, item, info):
        pass
class RefererImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        for req in requests:
            req.headers.appendlist("referer", item['referer'])
        return requests


class CsdnBlogBackupPipeline(object):
    def process_item(self, item, spider):
        dirname = 'blogs'
        import os
        import codecs
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        print(r''+dirname+os.sep+item["title"]+".md")
        with codecs.open(f'{dirname}{os.sep}{item["title"]}.md', 'w', encoding='utf-8') as f:
            f.write(item['content'])
            f.close()
        return item
