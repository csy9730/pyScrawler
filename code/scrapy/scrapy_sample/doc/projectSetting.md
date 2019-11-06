# projectSetting

[TOC]

## 简介
配置包含： project，preferences，machine,spider.
preferences配置包含 skin，窗口及控件的位置和大小布局，插件相关，快捷键相关。（由用户设置，偏慢变化）
machine：保存project history，（内置，无需用户操心，快速变化）
project配置包含：spider输入输出配置

spider配置包含：spider的默认配置


## cmdline配置
输入一个url，在一个文件夹内得到一个或多个文件。
* 输入配置：url，pg，pg_range,word
* 输出配置：sql，xls，json，fold_name,JOBDIR,
* 过程控制： 早退出条件。

首先要思考到底哪些参数是必需的。

``` python
    import argparse
    parser = argparse.ArgumentParser(prog='scrapy')
    parser.add_argument('--argument','-a', default=[],action='append', help='argument setting ')
    parser.add_argument('--set','-s', default=[],action='append', help='setting')
    parser.add_argument('--spider','-d',default='meizitu0',action='store', help='spider')
    parser.add_argument('--output','-o', action='append', help='output help')
    parser.add_argument('--start_urls','-u', action='append', help='start urls ')
    parser.add_argument('--name', action='store', help='spider name')
    parser.add_argument('--allowed_domains', action='append', help='domain')
    parser.add_argument('--loadconfig','-l', action='store', help='load config file')
```



以下参数都使用同一个spider入口，
* --argument 指定自定义参数
* --allowed_domains --name --start_urls 指定spider常用参数
* --custom_setting 指定自定义参数custom_setting

--set参数更新全局settings.py
* 通过JOBDIR可以实现增量
* --output 指定输出方式，通过管道ITEM_PIPELINES实现。
* 通过IMAGE_STORE指定图片输出文件夹。

以下配置属于settings.py，与项目关系不大，可以去除
早退出条件：CLOSESPIDER
log记录：LOG_LEVEL

使用方式：

```bash
crawl -o abc.json  -c werw=werwr -s werwer=tertert
```


## misc
**Q**:命令行能否传递json字典，
**A**: 注意字符串"和 回车键的转义。


* 命令行会转义" 编程',使用"""装饰字符串
* 使用python 内置cmdline传递，自带参数分割
* 使用jsonpath，一一指定叶节点值。

使用先字典后命令行(列表)在转字典的方法，确认转换无误。

扁平化， 把json的结构转船扁平化的key&value。
配合curd 实现json任意尺度编辑，


命令行的表达能力有限，需要自行扩展转义规则：
* 使用url规则
* 使用yaml规则
* 使用json规则


命令行可以表示简单一阶字典`{"a":"ww","ab":"wb"}`。通过append实现value可以取值列表。
通过=或":"赋值操作实现二阶字典。`{"a":{"aa":"ww","ab":"wb"},"b":"bv"}`
* 无名单字典表示：`dct={"a":"ww","ab":"wb"}`   `--argument dct:a=ww&ab=wb`
* 有名单字典表示：start_params ={"word":"moon","pn":0,"pg_range":2} `--start_params    word=moon&pn=0&pg_range=2`
* 字典列表： `start_params = [{"word":"moon","pn":0,"pg_range":2},]`



```python
dct ={
        "ITEM_PIPELINES":{
            'scrapy_sample.pipelines.RefererImagePipeline': 1,
             'scrapy_sample.pipelines.ImagePipeline': 555,
        }
}
dct2 = {"a":{"aa":"ww","ab":"wb"},"b":"bv"}
a=2&b=bv&c=ccc
# ITEM_PIPELINES='scrapy_sample.pipelines.RefererImagePipeline'=1
```

通过；分隔实现二阶列表。
`{"a":{ "wer":{"aa":"ww","ab":"wb"},"aa":"cc"},"b":"bv"}`



## Json配置文件

``` json
{
    "alias":"meizitu",
    "spider": "meizitu0",
    "spider_class":"sss",
    "output": [
        "scr_abc.jl",
        "wwre.xls"
    ],
    "type": "news",
    "start_urls": [
        "www.baidu.com",
    ],
    "argument": {
        "START_DICT": [{
            "url":"www.abc.com",
            "word":"moon",
            "pn":90
        },
        {
            "url":"www.abc.com",
            "word":"sun",
            "pn":90
        }]
    },
    "set": {
        "IMAGES_STORE": "images",
        "JOBDIR": "scr_job",
        "CLOSESPIDER_ITEMCOUNT": 2,
        "CLOSESPIDER_TIMEOUT": 555
    },
    "rule":[
        {
            "allow":"/\\d+/\\d+",
            "restrict_xpaths":"//div[@class='pagenavi']",
            "callback":"parse_article",
            "follow":true
        },
    ],
    "item":{
        "class": "ImageItem",
        "loader":"ItemLoader",
        "attrs": {
            "title":{
                "method": "xpath",
                "args": "//h1[@id='chan_newsTitle']/text()" ,
                "re": "(\\d+-\\d+-\\d+\\s\\d+:\\d+:\\d+)",
                "process":"TakeFirst",
            },
        }
    }
}
```

## 副本



提供命令行接口，setting, dict接口,api接口供pyqt使用。
命令行接口： 程序导入命令参数并执行 
dict接口: 函数通过字典导入设置
setting接口：通过文本文件导入设置
api接口： 导出相关格式 csv,json,xml,jsonline =>xls,sqlite, pickle
gui界面设计：

配置文件基于变化频率，分为 

- 基于project的缺省内存配置 （缺省生效）
- 当前内存的缓存配置 （核心）
- UI界面的可编辑配置  （UI触发生效）
- 文本框缓存配置        （UI触发生效）
- 命令行配置和临时json配置文件（命令行调用生效）
- 保存的project配置文件，   （文件打开生效）
- custom_spider配置文件    （文件打开生效）
- 基于spider内置配置    （默认生效）