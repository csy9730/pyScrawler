# pyqtCrawler



[TOC]



pyqtCrawler包括：

* 输入输出配置，
* 过程可视化&可交互控制。
* 爬虫软件
* 多进程管理器

核心应用在于Crawler，功能包括：视频下载器，数据采集器，网页内容监视器，工具接口集成

可视化包括：图片浏览器，小说阅读器，表格管理



UI部分

应用部分

- [ ] 添加下载进程的可视化设计

### 配置
``` python
    def _configRead(self):
    def _configWrite(self,dct):
    def saveConfig(self,project_name='setting.scrproj'):
        pass
    def loadConfig(self,project_name =  'setting.scrproj'):
        pass
    def showConfigAtEdit(self):
        self.txtConfig.setText( json.dumps( self.config,indent=4,ensure_ascii=False))
    def importConfigFromtEdit(self):
        pass
```
## UI
UI布局使用H型布局，左边栏，右边栏，中上主框体，中下交互命令行。
仿vscode布局页面，仿vscode的peacock的调色模块。
状态栏添加按钮，点击可以显示或隐藏split的widget。 


下拉抽屉菜单，可以持久显示，移动界面不消失。

- [ ] REPL工具 prompt

### pyinstaller
* 添加scrapy目录的VERSION文件
* 避免import错误，显式import 模块
* 避免spider not found 错误

主程序不能使用scrapy.exe,也不能使用cmdline调用，
只能使用CrawlerProcess或CrawlerRunner调用核心主程序。
CrawlerRunner可以通过name字符串或spiderClass调用spiderClass
CrawlerProcess继承于CrawlerRunner。

**Q**:KeyError: 'Spider not found: 
**A**: 这种错误通常由于spiderName错误导致，也可能由于当前目录没有spider.py文件引起。更好的方式是显式把spiderClass传入参数，无需搜索工作目录。

**Q**:ModuleNotFoundError: No module named 'sip'
**A**:重新安装PyQt5

## misc

for img in imgs:
    body.replace( img,)
title = response.css('title').get()
body= response.xpath('body').get()


