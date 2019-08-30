# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from tieba.items import TieItem
from scrapy.exceptions import DropItem
from urllib.parse import urlparse
import os
import json

class TiebaPipeline(object):
    def process_item(self, item, spider):
        
        #with open("my_tieba.txt",'ab+') as fp:
        #    print( "item=",item['title'],item['author'])
        #    fp.write(item['title'].encode("GBK") + b','+item['author'].encode("GBK") + b','+b'\n')
        return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item, TieItem):
            for image_url in item['imgList']:
                file_path ='%s/%s' % (item["dirName"],os.path.basename(urlparse(image_url).path))
                yield scrapy.Request(image_url,meta={'file_path':file_path })
    def file_path(self, request, response=None, info=None):
        return request.meta['file_path']
    def item_completed(self, results, item, info):
        if isinstance(item, TieItem):
            if len(item['imgList'])==0:
                return item
            image_paths = [x['path'] for ok, x in results if ok]
            print( "img",image_paths)
            if not image_paths:
                item['imgPathList'] = ["DropItem"]
                return item
                raise DropItem("Item contains no images")
            item['imgPathList'] = image_paths
        return item

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, TieItem):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item