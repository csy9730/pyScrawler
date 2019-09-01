# scrapy

[TOC]

## 简介

scrapy是python的网络爬虫库。

## 安装

``` bash
pip3 install lxml
pip3 install scrapy
```



## DEMO

### 新建项目

安装scrapy

```
scrapy startproject tutorial # 生成项目文件目录
```

tutorial是项目名。将会生成以下目录结构

```
tutorial/
    scrapy.cfg
    tutorial/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            spider1.py
        	spider2.py
```

- scrapy.cfg: 项目的配置文件

- tutorial/: 该项目的python模块。之后您将在此加入代码。

- tutorial/items.py: 项目中的item文件.

- tutorial/pipelines.py: 项目中的pipelines文件.

- tutorial/settings.py: 项目的设置文件.

- tutorial/spiders/: 放置spider代码的目录.

  

  items.py 相当于字典

  spider包括xpath解析。

  middlewares.py：定义Downloader Middlewares(下载器中间件)和Spider Middlewares(蜘蛛中间件)的实现

### 设计数据结构

定义item，item和字典功能类似。

### 爬虫创建

``` bash
scrapy genspider scrawlerName targetUrl
```

该命令会创建以下文件·scrawlerName.py

``` python
# -*- coding: utf-8 -*-
import scrapy

class Meizitu0Spider(scrapy.Spider):
    name = 'scrawlerName'
    allowed_domains = ['abcabc.com']
    start_urls = ['https://www.abc.com/']

    def parse(self, response):
        pass

```

创建一个Spider，继承于 scrapy.Spider 类， 且定义以下属性:

- name：是爬虫的名字，该名字必须是唯一的。
- allowed_domains：是允许爬取的域名，比如一些网站有相关链接，域名就和本网站不同，这些就会忽略。
- atart_urls：是Spider爬取的网站，定义初始的请求url，可以多个。
- parse方法：是Spider的一个方法，在请求start_url后，之后的方法，这个方法是对网页的解析，与提取自己想要的东西。

### Selectors解析

请求网页后返回response，也就是你需要解析的网页。selector可以提供丰富的解析手段。

Selector有四个基本的方法

- [`xpath()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.xpath): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表 。
- [`css()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.css): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表.
- [`extract()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.extract): 序列化该节点为unicode字符串并返回list。
- [`re()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.re): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表。

### 运行

命令行中运行

``` bash
scrapy crawl scrawlerName
scrapy crawl scrawlerName -o maoyan.csv # 文件导出
scrapy crawl scrawlerName -o maoyan.json
```

python中运行start.py

``` python
from scrapy import cmdline
cmd = 'scrapy crawl scrawlerName' 
cmdline.execute( cmd.split())
```

