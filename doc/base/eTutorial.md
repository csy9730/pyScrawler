# scrapy

[TOC]

## ���

scrapy��python����������⡣

## ��װ

``` bash
pip3 install lxml
pip3 install scrapy
```



## DEMO

### �½���Ŀ

��װscrapy

```
scrapy startproject tutorial # ������Ŀ�ļ�Ŀ¼
```

tutorial����Ŀ����������������Ŀ¼�ṹ

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

- scrapy.cfg: ��Ŀ�������ļ�

- tutorial/: ����Ŀ��pythonģ�顣֮�������ڴ˼�����롣

- tutorial/items.py: ��Ŀ�е�item�ļ�.

- tutorial/pipelines.py: ��Ŀ�е�pipelines�ļ�.

- tutorial/settings.py: ��Ŀ�������ļ�.

- tutorial/spiders/: ����spider�����Ŀ¼.

  

  items.py �൱���ֵ�

  spider����xpath������

  middlewares.py������Downloader Middlewares(�������м��)��Spider Middlewares(֩���м��)��ʵ��

### ������ݽṹ

����item��item���ֵ书�����ơ�

### ���洴��

``` bash
scrapy genspider scrawlerName targetUrl
```

������ᴴ�������ļ���scrawlerName.py

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

����һ��Spider���̳��� scrapy.Spider �࣬ �Ҷ�����������:

- name������������֣������ֱ�����Ψһ�ġ�
- allowed_domains����������ȡ������������һЩ��վ��������ӣ������ͺͱ���վ��ͬ����Щ�ͻ���ԡ�
- atart_urls����Spider��ȡ����վ�������ʼ������url�����Զ����
- parse��������Spider��һ��������������start_url��֮��ķ�������������Ƕ���ҳ�Ľ���������ȡ�Լ���Ҫ�Ķ�����

### Selectors����

������ҳ�󷵻�response��Ҳ��������Ҫ��������ҳ��selector�����ṩ�ḻ�Ľ����ֶΡ�

Selector���ĸ������ķ���

- [`xpath()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.xpath): ����xpath���ʽ�����ظñ��ʽ����Ӧ�����нڵ��selector list�б� ��
- [`css()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.css): ����CSS���ʽ�����ظñ��ʽ����Ӧ�����нڵ��selector list�б�.
- [`extract()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.extract): ���л��ýڵ�Ϊunicode�ַ���������list��
- [`re()`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html#scrapy.selector.Selector.re): ���ݴ����������ʽ�����ݽ�����ȡ������unicode�ַ���list�б�

### ����

������������

``` bash
scrapy crawl scrawlerName
scrapy crawl scrawlerName -o maoyan.csv # �ļ�����
scrapy crawl scrawlerName -o maoyan.json
```

python������start.py

``` python
from scrapy import cmdline
cmd = 'scrapy crawl scrawlerName' 
cmdline.execute( cmd.split())
```

