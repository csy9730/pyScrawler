# -*- coding: utf-8 -*-
import scrapy


class DomainSpider(scrapy.Spider):
    name = 'domain'
    allowed_domains = ['domain.com']
    start_urls = ['http://domain.com/']

    def parse(self, response):
        print("begin parse")
        pass
