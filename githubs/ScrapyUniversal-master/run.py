import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    print(custom_settings)

    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    print(spider)
    return

    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()
