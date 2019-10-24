#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 对于js异步加载网页的支持
Desc : 爬取京东网首页，下面内容基本都是异步加载的，我选取“猜你喜欢”这个异步加载内容来测试
"""
import logging
import re
import json
import base64
import scrapy


class JsSpider(scrapy.Spider):
    name = "jd"
    # allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/",
        # "https://manhua.dmzj.com/yueshenhasi/92686.shtml#@page=1",
    ]
    custom_setting= {
        #Splash服务器地址
        'SPLASH_URL':'http://localhost:8050'     ,                                                               
        #开启两个下载中间件，并调整HttpCompressionMiddlewares的次序                                      
        'DOWNLOADER_MIDDLEWARES ':{
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware':725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,                         
        },
        #设置去重过滤器
        'DUPEFILTER_CLASS':'scrapy_splash.SplashAwareDupeFilter',
        #用来支持cache_args（可选）
        'SPIDER_MIDDLEWARES':{
            'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
        },
        'DUPEFILTER_CLASS':'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE':'scrapy_splash.SplashAwareFSCacheStorage'   
    }
    def start_requests(self):
        from scrapy_splash import SplashRequest
        splash_args = {
            'wait': 4.5,
            # 'http_method': 'GET',
            # 'html': 1,
            # 'png': 1,
            # 'width': 600,
            # 'render_all': 1,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',args=splash_args)

    def parse_result(self, response):
        logging.info(u'----------使用splash爬取京东网首页异步加载内容-----------')
        #logging.info(response.text)
        with open('scr_jd.html','wb') as fp:
            fp.write(response.body)
        guessyou = response.xpath('//div[@id="guessyou"]/div[1]/h2/text()').extract_first()
        logging.info(u"find：%s" % guessyou)
        logging.info(u'---------------success----------------')


def main():
    body = u'发布于： 2016年04月08日'
    pat4 = re.compile(r'\d{4}年\d{2}月\d{2}日')
    if (re.search(pat4, body)):
        print(re.search(pat4, body).group())

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess 
    from scrapy.utils.project import get_project_settings

    process = CrawlerProcess(get_project_settings())
    process.crawl(JsSpider) 
    process.start() # the script will block here until the crawling is finished
    print("crawl finished")