# CrawlSpider



``` bash
  scrapy startproject crawlspider
  scrapy genspider -t crawl Crawlspider domain.com
```

会自动生成以下模板代码：

``` python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlspiderSpider(CrawlSpider):
    name = 'Crawlspider'
    allowed_domains = ['domain.com']
    start_urls = ['http://domain.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
```

CrawlSpider和spider的区别在于：CrawlSpider增加了rule和linkExtractors，可以不写默认的parse函数。



## Rule

通过设置多条规则rule，可以实现横向移动和纵向移动。

横向移动：一个索引页到另一个索引页。纵向移动，一个索引页到源页抽取Item。

多条规则搭配，可以实现多层规则、多级树状规则。

以下是一个多层解析网站的demo：

``` 
# https://www.abc.so/  				# 主页
# https://www.abc.so/list/3_1.html		# 书本列表
# http://www.abc.so/xiaoshuo/414.html	# 单本书封面，调用parse_book_message生成bookItem
# https://www.abc.so/files/article/html/0/414/index.html	# 单本书章节列表
# https://www.abc.so/files/article/html/0/414/5361947.html  # 书单章，调用parse_chapter_content生成chapterItem
# 
rules=(
    Rule(LinkExtractor(allow=("list/\d*_\d*.html"),restrict_xpaths=".//div[@class='main m_menu']//li")),
    Rule(LinkExtractor(allow=("xiaoshuo/\d*\.html"),restrict_xpaths=".//dl[@id='content']//dd"),callback="parse_book_message",follow=True),
    Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?.index.html"),restrict_xpaths=".//*[@id='content']//dd//div")),
    Rule(LinkExtractor(allow=("files/article/html/\d*?/\d*?/\d*?.html"),restrict_xpaths=(".//*[@id='at']//tr//td")),callback="parse_chapter_content",follow=False),
  )
```

显而易见，网站共有五级页面，对应的url有明显地多级目录结构。

`Rule(LinkExtractor(allow=("list/\d*_\d*.html"),restrict_xpaths=".//div[@class='main m_menu']//li"))`表示：从页面（一级页面）的xpath解析出二级页面的超链接，交给其他Rule处理。其中三级页面和五级页面调用对应的解析函数`parse_book_message`和`parse_chapter_content`。

`start_urls`可以携带一级到五级页面，`rule`可以基于页面调用不同`Rule`解析。

注意： rule只对页面的链接生效，不会提供对start_urls的默认parse函数处理，需要添加`Rule(LinkExtractor(allow=start_urls), callback='parse_item', follow=False),`

网页解析默认使用广度优先机制，先处理一级页面再处理二级页面、三级页面。单页面抓取url按照先进后出顺序。

## 问题

Rule机制对网页筛选不够灵活，难以利用当前页面的item信息筛选链接，难以传递meta值，还得结合使用parse函数。

``` python
class CrawlSpider(Spider):

    rules = ()

    def __init__(self, *a, **kw):
        super(CrawlSpider, self).__init__(*a, **kw)
        self._compile_rules()
    def parse(self, response):
        return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    def parse_start_url(self, response):
        return []
```

rule的allow，可以拒绝不匹配的url。
``` python
allow_res = [x if isinstance(x, _re_type) else re.compile(x)
                          for x in arg_to_iter(allow)]
_matches = lambda url, regexs: any(r.search(url) for r in regexs)
if _matches(link.url, self.allow_res):
  return

# 基于字符串返回 成员函数（parse）
def get_method(method):
      if callable(method):
          return method
      elif isinstance(method, six.string_types):
          return getattr(self, method, None)
```  

