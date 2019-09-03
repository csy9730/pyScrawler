#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
import re
import sys
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest, HtmlResponse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler(sys.stdout)])
post_data = {
    'name': 'abc@163.com',
    'password': '********',
    'remember':'false'
}

class GithubSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://www.douban.com/',
    ]

    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://accounts.douban.com/passport/login",
    }

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",
                        headers=self.post_headers,  # 注意此处的headers
                        meta={'cookiejar': 1}, callback=self.post_login)]

    # FormRequeset
    def post_login(self, response):
        # authenticity_token = response.xpath(
        #     '//input[@name="authenticity_token"]/@value').extract_first()
        captcha_image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        if captcha_image_url is None:
            print("登录时无验证码")
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数，如果url跟Request页面的一样就省略掉
        # 登录入口

        return [FormRequest(url='https://accounts.douban.com/j/mobile/login/basic',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.post_headers,  # 注意此处的headers
                                          formdata=post_data,
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]
        return [Request('https://accounts.douban.com/j/mobile/login/basic',
                                     method='POST',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.post_headers,  # 注意此处的headers
                                          data=post_data,
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        print('StatusCode:', response.status)
        if response.status != 200:
            print('Login Fail')
        for url in self.start_urls:
            yield Request(url, headers=self.post_headers,  meta={'cookiejar': response.meta['cookiejar']},callback=self.parse_item)
    def parse_item(self,response):
        print('StatusCode:', response.status)
        if response.status != 200:
            print('Login Fail')
            return
        print( response.text)
        pc = response.xpath("//*[@id='db-global-nav']//li[@class='nav-user-account']//a/span/text()").get()
        print( pc)


if __name__ == '__main__':
    import sys
    if len(sys.argv)>=2:post_data["password"] = sys.argv[2]
    if len(sys.argv)>=1:post_data["name"] = sys.argv[1]
    print( post_data)

    from twisted.internet import reactor
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.log import configure_logging
    configure_logging()
    runner = CrawlerRunner()
    runner.crawl(GithubSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run() # the script will block here until all crawling jobs are finished
    print("spider finished")