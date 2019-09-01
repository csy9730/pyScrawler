import scrapy 
from scrapy.crawler import CrawlerProcess 
from scrapy.utils.project import get_project_settings
from domain import DomainSpider
process = CrawlerProcess(get_project_settings())
process.crawl(DomainSpider) 
process.start() # the script will block here until the crawling is finished
print("crawl finished")

