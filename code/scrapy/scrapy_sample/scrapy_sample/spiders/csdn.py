import scrapy

from scrapy_sample.items import BlogListItem

class CsdnBlogSpider(scrapy.Spider):
    """我的CSDN所有文章和链接的爬虫"""
    name = 'csdn_blog'
    start_urls = ['http://blog.csdn.net/u011054333/article/list/1']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'http://blog.csdn.net'

    def parse(self, response):
        import urllib.parse
        articles = response.css('div.article-list div.article-item-box')
        for article in articles:
            title = ''.join( article.css('h4 a::text').getall()).strip()
            href = self.base_url + article.css('h4 a::attr(href)').get()  
            description =  article.css('p.content a::text').get().strip()
            datetime =  article.css('div.info-box span.date::text').get().strip()
            num =  article.css('div.info-box span.read-num span.num::text').getall() or [-1,-1]
            read_num =  num[0]
            reply_num =  num[1]
            yield  BlogListItem(title=title, href=href,referer = response.url ,description=description, 
                            datetime=datetime,read_num=read_num,reply_num=reply_num)

        pages = response.css('div#pageBox')
        next_page_url = pages.css('a').re_first('<a href=\"(.*)\">下一页')
        if next_page_url is not None:
            yield scrapy.Request(urllib.parse.urljoin(self.base_url, next_page_url))
