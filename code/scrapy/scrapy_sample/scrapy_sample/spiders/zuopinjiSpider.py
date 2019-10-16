# -*- coding: utf-8 -*-


from scrapy import Request, Spider
from pyquery import PyQuery as pq
from scrapy_sample.items import ZuopinjiItem


class ZuopinjSpider(Spider):
    name = 'zuopinj'
    allowed_domains = ['zuopinj.com']
    index_url = 'http://zuopinj.com/writer/'

    def start_requests(self):
        yield Request(self.index_url, self.parse_author)

    # 获取该站全部作家的主页链接
    def parse_author(self, response):
        items = response.xpath('//div[@class="item"]/ul/li/a/@href').extract()
        for item in items:
            yield Request(item, self.parse_one_page)

    # 获取每本书的书名和链接
    def parse_one_page(self, response):
        content = response.text
        doc = pq(content)
        author_name = doc('.head .logo a').text()
        # 解析两种不同的作家主页，一种可以翻页，另一种不行
        if doc('.content .box').text() is "":
            content = doc('.main-books .tab-detail.on')
            items = content('.zp-book-item').items()
            for item in items:
                book_name = item('a h2').text()
                book_url = item('a').attr('href')
                yield Request(book_url, self.parse_chapters, meta={'book_name': book_name, 'author_name': author_name})

            # 获取下一页的书名和链接
            items_pages = doc('.main-top .main-books .tab-detail.on .zp_pages a').items()
            next_urls = []
            for item in items_pages:
                cur_page = item.attr('href')
                if cur_page not in next_urls:
                    next_urls.append(cur_page)
            for url_page in next_urls:
                yield Request(url_page, self.parse_one_page)
        else:
            items = doc('.content .box .books.section-cols .bk h3 a').items()
            for item in items:
                book_name = item.text()
                book_url = item.attr('href')
                yield Request(book_url, self.parse_chapters, meta={'book_name': book_name, 'author_name': author_name})

    # 获取某本书的章节名和链接
    def parse_chapters(self, response):
        content = response.text
        doc = pq(content)
        chapter_urls = doc('.content .section .book_list ul li a').items()
        book_name = response.meta['book_name']
        author_name = response.meta['author_name']
        for item in chapter_urls:
            chapter_name = item.text()
            chapter_url = item.attr('href')
            yield Request(chapter_url, self.parse_content, meta={'chapter_name': chapter_name,
                                                                 'book_name': book_name,
                                                                 'author_name': author_name})

    # 获取章节内容
    def parse_content(self, response):
        content = response.text
        doc = pq(content)
        text = doc('.content .ncon .nc_l .contentbox p').text()
        content = text.replace('\n', '\n    ')
        content = '    ' + content
        item = ZuopinjiItem()
        item['book_name'] = response.meta['book_name']
        item['author_name'] = response.meta['author_name']
        item['chapter_name'] = response.meta['chapter_name']
        item['chapter_content'] = content
        yield item