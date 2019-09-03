# Rule



## 源码

``` python


class Rule(object):

    def __init__(self, link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None):
        self.link_extractor = link_extractor
        self.callback = callback
        self.cb_kwargs = cb_kwargs or {}
        self.process_links = process_links
        self.process_request = process_request or _identity
        self.process_request_argcount = None
        self.follow = follow if follow is not None else not callback

    def _compile(self, spider):
        self.callback = _get_method(self.callback, spider)
        self.process_links = _get_method(self.process_links, spider)
        self.process_request = _get_method(self.process_request, spider)
        self.process_request_argcount = len(get_func_args(self.process_request))
        if self.process_request_argcount == 1:
            msg = 'Rule.process_request should accept two arguments (request, response), accepting only one is deprecated'
            warnings.warn(msg, category=ScrapyDeprecationWarning, stacklevel=2)

    def _process_request(self, request, response):
        """
        Wrapper around the request processing function to maintain backward
        compatibility with functions that do not take a Response object
        """
        args = [request] if self.process_request_argcount == 1 else [request, response]
        return self.process_request(*args)
```



* link_extractor
* callback
* follow

link_extractor 是一个Link Extractor对象。 是从response中提取链接的方式。在下面详细解释
follow是一个布尔值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback 为None，follow 默认设置为True，否则默认为False。 
当follow为True时，爬虫会从获取的response中取出符合规则的url，再次进行爬取，如果这次爬取的response中还存在符合规则的url，则再次爬取，无限循环，直到不存在符合规则的url。 
当follow为False是，爬虫只从start_urls 的response中取出符合规则的url，并请求。

callback和follow可以都为空，此时follow默认为True。该rule可以用于解析目录页、导航页，当前页面没有item生成，只是把解析的链接交给其他rule处理。



