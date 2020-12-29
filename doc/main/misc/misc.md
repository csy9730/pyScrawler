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



response.text str格式
response.body bytes格式



对于动态网页使用ajax技术，两种办法

1. 寻找js的api的数据
2. 渲染网页，可以使用phatphomjs、splash渲染网页。



ValueError: Missing scheme in request url:

url缺乏https或http协议