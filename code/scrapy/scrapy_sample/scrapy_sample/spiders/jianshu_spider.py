#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor

class Jianshu(scrapy.Spider):
    name = "jianshu_spider"
    allowed_domains = ["jianshu.com"]

    def __init__(self, *args, **kwargs):
        super(Jianshu, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.jianshu.com/']

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths='//ul[@class="note-list"]/li')
        links = link.extract_links(response)
        if links:
            for link_one in links:
                print (link_one)