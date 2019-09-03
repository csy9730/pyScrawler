# start_requests



## start_urls

start_url可以指定起始网址列表，

### 文件导入起始网址

```python
start_urls=[ i.strip() for i in open('todo.urls.txt').readlines()]
```



### 命令行注入参数

通过命令行注入参数来指定起始url，

`scrapy crawl myspider -a category=electronics`

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    def __init__(self, category=None, *args, **kwargs):
    super(MySpider, self).__init__(*args, **kwargs)
    self.start_urls = ['http://www.example.com/categories/%s' % category]
    # ...
```



## start_requests（）

start_requests()方法可以代替start_urls，发出第一个网络访问请求