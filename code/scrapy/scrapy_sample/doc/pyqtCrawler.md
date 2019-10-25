# pyqtCrawler

视频下载器，数据采集器，网页内容监视器，工具接口集成，
* 输入输出配置，
* 过程可视化&可交互控制。
* 爬虫软件
* 多项目管理器
## crawler
* 图片爬虫： 
  * baidu_img, 
  * meizitu,mzitu,mm131,
漫画爬虫：dmzj,sfacg
文档爬虫: blog,
小说：biquge，
BBS爬虫： tieba，
新闻爬虫：
shop： 
    jingdong，
    taobao
music：
    netease, spider163-master
    baidumusic
video：biblbili
    * VIP 视频破解无名网站：http://www.administrator5.com/WMXZ.WANG/index.html
Rss:
movie: 
    * doubantop250,
    * maoyanboard
    * https://github.com/iawia002/annie
12306
知乎登录
豆瓣登录
微博登陆


### 配置
层级： index-> list->(book/album)->article 
开始url： 指定url？如何判断当前页面parse函数
抓取策略： 几级深度？深度优先vs广度优先
结束策略： item_count, time_expire

**Q**:结构化搜索？
**A**:scrapy是扁平化解构，常规网站是多级结构。rule 是扁平化，没有结构，不好用.扁平化结构，不关心网站结构层次，所有内容都经过队列，队列后进先出，丢失了先后顺序，结构信息。常规网站有着鲜明的结构层次，入口页面包含多个列表页，列表页含有多个分页，列表页包含内容页，按照这个层次化结构抓取，上级页面包含了下级页面的部分信息。
采用分页计算权重方式，总列表页，列表页，文章页，三者对应关系为[1,5, 100],则可以令权重为[105,21,1],每次从三者中选取最低权重的url开始遍历。


**Q**: 如何设置翻页设置？添加翻页数
        通过翻页，限制页面数量。
        列表页翻页是否增加深度？
命令行配置： 
`spider -c abc`
**Q**: 如何配置pythonobject，例如item，middleware，pipeline等等

## UI
UI布局使用H型布局，左边栏，右边栏，中上主框体，中下交互命令行。
仿vscode布局页面，仿vscode的peacock的调色模块。
[] REPL工具 prompt
[] 状态栏添加按钮，点击可以显示或隐藏split的widget。
[]  baiduimage &dmzj 的动态生成start_urls 
[] 下拉抽屉菜单，可以持久显示，移动界面不消失。
[] jupyter中调试request。

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


### todo
[] https://www.51xs.org/info/1.html
[]  http://www.girl13.com  
[] 如何集成request和scrapy和selenium于一个框架
[] 添加类postman内容
[] 查询参数拼接时是否有序？
[]  添加浏览器支持：webkit，v8，本地浏览器。
[+] 合并文件夹 23us,doubanMovieTop250
[+]  添加tableWIdgetWIdget,spider_info.json
[+] combobox读取 spider_info
[]  添加下载进程的可视化设计
[+]  # LOG_LEVEL = 'INFO'
[+]  定时刷新 dirmodel
[]  ss: 网络矿工  https://zhuanlan.zhihu.com/p/33868523
[+] add depth bfs,dfs
[+] add QFileDialog
[] add recent ,preference,recent folder path,gui position
[] qss
[] ctrl+C 暂停信号
[] add custom spider to gui: linkExtract & rule & callback
[+] scrapy custom spider
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


