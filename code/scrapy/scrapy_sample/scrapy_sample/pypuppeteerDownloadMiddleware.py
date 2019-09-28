from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import pyppeteer
import asyncio
import os
from scrapy.http import HtmlResponse

pyppeteer.DEBUG = False 

class FundscrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self) :
        print("Init downloaderMiddleware use pypputeer.")
        os.environ['PYPPETEER_CHROMIUM_REVISION'] ='588429'
        # pyppeteer.DEBUG = False
        print(os.environ.get('PYPPETEER_CHROMIUM_REVISION'))
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(self.getbrowser())
        loop.run_until_complete(task)

        #self.browser = task.result()
        print(self.browser)
        print(self.page)
        # self.page = await browser.newPage()
    async def getbrowser(self):
        self.browser = await pyppeteer.launch()
        self.page = await self.browser.newPage()
        # return await pyppeteer.launch()
    async def getnewpage(self): 
        return  await self.browser.newPage()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(self.usePypuppeteer(request))
        loop.run_until_complete(task)
        # return task.result()
        return HtmlResponse(url=request.url, body=task.result(), encoding="utf-8",request=request)

    async def usePypuppeteer(self, request):
        print(request.url)
        # page = await self.browser.newPage()
        await self.page.goto(request.url)
        content = await self.page.content()
        return content 

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)