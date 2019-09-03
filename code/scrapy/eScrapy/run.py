import scrapy 
from domain import DomainSpider

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess 
    from scrapy.utils.project import get_project_settings

    process = CrawlerProcess(get_project_settings())
    process.crawl(DomainSpider) 
    process.start() # the script will block here until the crawling is finished
    print("crawl finished")

