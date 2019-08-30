# scrapy shell



## 基础命令

``` bash
scrapy startproject tutorial # 生成项目文件目录
scrapy genspider scrawlerName targetUrl
scrapy crawl scrawlerName
scrapy crawl scrawlerName -o maoyan.csv # 文件导出
scrapy crawl scrawlerName -o maoyan.json
# ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')

```



``` bash
scrapy crawl -h
--logfile=FILE          log file. if omitted stderr will be used
--loglevel=LEVEL, -L LEVEL
                        log level (default: DEBUG)
--nolog                 disable logging completely
```

## 交互模式

scrapy shell可以调用ipython 开启交互模式

例如执行`scrapy shell http://blog.csdn.net/`

然后可以交互中执行：

``` bash
response.xpath(' ').extract()
```

可以在交互模式尝试编写xpath并测试。



## 中止策略

CLOSESPIDER_TIMEOUT（秒）：在指定时间过后，就终止爬虫程序. 

CLOSESPIDER_ITEMCOUNT：抓取了指定数目的Item之后，就终止爬虫程序. 

CLOSESPIDER_PAGECOUNT：在收到了指定数目的响应之后，就终止爬虫程序. 

CLOSESPIDER_ERRORCOUNT：在发生了指定数目的错误之后，就终止爬虫程序.最大爬取深度



## telnet

Telnet Console