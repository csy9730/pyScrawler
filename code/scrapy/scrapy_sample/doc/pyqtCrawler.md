# pyqtCrawler

## crawler
图片爬虫： baidu_img, meizitu,mzitu,mm131,
漫画爬虫：dmzj
文档爬虫: blog,
BBS爬虫：
新闻爬虫：
shop： jingdong，taobao
music：netease
video：biblbili
Rss:

### 配置
层级： index-> list->(book/album)->article 
开始url： 指定url？如何判断当前页面parse函数
抓取策略： 几级深度？深度优先vs广度优先
结束策略： item_count, time_expire
**Q**: 如何设置翻页设置？
        列表页翻页是否增加深度？
命令行配置： 
`spider -c abc`
**Q**: 如何配置pythonobject，例如item，middleware，pipeline等等

## pyinstaller
* 添加scrapy目录的VERSION文件
* 避免import错误，显式import 模块
* 避免spider not found 错误


主程序不能使用scrapy.exe,也不能使用cmdline调用，
只能使用CrawlerProcess或CrawlerRunner调用核心主程序。
CrawlerRunner可以通过name字符串或spiderClass调用spiderClass
CrawlerProcess继承于CrawlerRunner。

**Q**:KeyError: 'Spider not found: 
**A**: 这种错误通常由于spiderName错误导致，也可能由于当前目录没有spider.py文件引起。更好的方式是显式把spiderClass传入参数，无需搜索工作目录。

## argparse
``` bash
crawl -o abc.json  -c werw=werwr -s werwer=tertert
```
## misc
提供命令行接口，setting, dict接口,api接口供pyqt使用。
命令行接口： 程序导入命令参数并执行 
dict接口: 函数通过字典导入设置
setting接口：通过文本文件导入设置
api接口： 导出相关格式 csv,json,xml,jsonline =>xls,sqlite, pickle
gui界面设计：

### todo
[] coolscrapy
[] docker & splash
[]  smtp
[] rss

[] project-setting & scrapy-setting
[] wizard & project-setting
[] add headless chrome options

``` python
for img in imgs:
    body.replace( img,)
title = response.css('title').get()
body= response.xpath('body').get()
byt = response.body #  type = bytes
text = response.text  #  type =str
```
[] scrapy markdown
[] scrapy rss 
[] scrapy 通用爬虫,broadcrawler
[] scrapy custom spider
[] email 保存&接收&发送
[] readthedocs
[] ss: celery
[] ss:rpc 框架
[] ss:事件循环
 

## misc

File (code: 302): Error downloading file from <GET referred in None 
item['referer'] = response.url

HTTP Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器籍此可以获得一些信息用于处理。比如从我主页上链接到一个朋友那里，他的服务器就能够从HTTP Referer中统计出每天有多少用户点击我主页上的链接访问他的网站。

200 表示正常访问

302 状态，
只能启用 重定向: `MEDIA_ALLOW_REDIRECTS = True`或`REDIRECT_ENABLED = True`

522 Connection Timed Out
Cloudflare could not negotiate a TCP handshake with the origin server.

DEBUG: Retrying <GET https://www.abc.com> (failed 1 times): TCP connection timed out: 10060: 由于 

字符串转合法路径：
re.sub('[^\w\-_\. ]', '_', 'some\\*-file._n\\\\ame')
Out[27]: 'some__-file._n__ame'
