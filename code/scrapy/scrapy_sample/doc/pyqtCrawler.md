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

ModuleNotFoundError: No module named 'sip'

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

### log
rule 是扁平化，没有结构，不好用
有时需要有结构化设计
### todo
[]  baiduimage &dmzj 的动态生成start_urls 
[]  http://www.girl13.com  https://github.com/chenjiandongx/mmjpg  http://www.mmjpg.com
[]  添加下载进程的可视化设计
[+]  定时刷新 dirmodel
[]  ss: 网络矿工  https://zhuanlan.zhihu.com/p/33868523
[+] add depth bfs,dfs
[+] add QFileDialog
[] add recent ,preference,recent folder path,gui position
[] qss
[] ctrl+C 暂停信号
[] add custom spider to gui: linkExtract & rule & callback
[+] add file treeWidget
[+] set output file path
[+] how to set pipeline & fileformat(csv,json,xls...)
[+] spider添加 属性： 分类tag，name，base_url,
[+] project-setting & scrapy-setting 
[] wizard & project-setting
[] scrapy markdown
[] scrapy rss 
[+] readthedocs
[] scrapy 通用爬虫,broadcrawler
[] scrapy custom spider
[] coolscrapy
[-] docker & splash
[] smtp
[] add headless chrome options
[] email 保存&接收&发送
[] ss: celery
[] ss:rpc 框架
[] ss:事件循环


## misc

for img in imgs:
    body.replace( img,)
title = response.css('title').get()
body= response.xpath('body').get()

字符串转合法路径：
re.sub('[^\w\-_\. ]', '_', 'some\\*-file._n\\\\ame')
Out[27]: 'some__-file._n__ame'

\xa0表示不间断空白符。在Python中，使用re.sub方法不能将其去除，但有以下两种方法可行：

1.使用translate方法，示例：
>>> inputstring = u'\n               Door:\xa0Novum    \t'
>>> move = dict.fromkeys((ord(c) for c in u"\xa0\n\t"))
>>> output = inputstring.translate(move)
>>> output
             Door:Novum     
2.利用split()方法，示例:
>>> s = 'T-shirt\xa0\xa0短袖圆领衫,体恤衫\xa0'
>>> out = "".join(s.split())
>>> out
'T-shirt短袖圆领衫,体恤衫'
参考：python中去掉字符串中的\xa0、\t、\n