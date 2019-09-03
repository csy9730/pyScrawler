# misc



## 邮件

```python
MailSender
```

## logger

默认配置

``` python
LOG_ENABLED = true
LOG_ENCODING = "utf-8"
LOG_LEVEL = logging.INFO
LOG_FILE = "log/spider.log"
LOG_STDOUT = True
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
```



``` python
import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'
    start_urls = ['http://scrapinghub.com']

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
```

