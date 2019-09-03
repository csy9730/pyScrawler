import scrapy

class MySpider1(scrapy.Spider):
    # Your first spider definition
    name = 'domain'
    allowed_domains = ['domain.com']
    start_urls = ['http://domain.com/']

    def parse(self, response):
        print("begin parse domain")
        pass

class MySpider2(scrapy.Spider):
    # Your second spider definition
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("begin parse baidu")
        pass
if __name__ == '__main__':
    from twisted.internet import reactor
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.log import configure_logging
    configure_logging()
    runner = CrawlerRunner()
    runner.crawl(MySpider1)
    runner.crawl(MySpider2)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run() # the script will block here until all crawling jobs are finished
    print("spider finished")