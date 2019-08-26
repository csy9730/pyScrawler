# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem


class Mm131Spider(scrapy.Spider):
    name = 'mm131'

    start_urls = ['https://www.mm131.net/xinggan/3473.html',
                  #'https://www.mm131.net/xinggan/2746.html',
                  'https://www.mm131.net/xinggan/3331.html']

    def parse(self, response):
        total_page = int(response.css('span.page-ch::text').extract_first()[1:-1])
        current_page = int(response.css('span.page_now::text').extract_first())
        item = ImageItem()
        item['image_urls'] = response.css('div.content-pic img::attr(src)').extract()
        item['referer'] = response.url
        yield item
        if current_page < total_page:
            rp ='.' if response.url.rfind('_') == -1 else  '_'
            head, sep, tail = response.url.rpartition(rp)
            yield scrapy.Request(head + f'_{current_page+1}.html')
