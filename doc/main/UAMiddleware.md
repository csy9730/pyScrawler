#  UAMiddleware



UserAgentMiddleware源码

``` python

class UserAgentMiddleware(object):
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent='Scrapy'):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent)
```

可以看到：ua分别继承于setting的USER_AGENT，spider的'user_agent和request的b'User-Agent'。从USER_AGENT到 b'User-Agent'，适用范围越小，优先级越降低。

``` python
class CustomizeUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        """ 从 settings.py 中读取 预设的 UA 列表 """
        return cls(user_agent=crawler.settings.get('CUSTOMIZE_USER_AGENT_LIST'))

    def process_request(self, request, spider):
        """ 随机选择一个 UA 并设置到 Request 中 """
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent

```

UserAgentMiddleware在get_media_requests之后file_path之前生效

需要先在setting中登记，自定义蜘蛛中间件才能生效

``` python
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
   'scrapy_sample.middlewares.CustomizeUserAgentMiddleware': 222
 }
```



默认设置

``` python
{b'Accept': [b'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'], b'Accept-Language': [b'en'], b'User-Agent': [b'Scrapy/1.7.3 (+https://scrapy.org)'], b'Accept-Encoding': [b'gzip,deflate']}
```





