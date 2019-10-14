# projectSetting


配置文件基于变化频率，分为 
* spider默认配置
* project配置文件，
* 命令行配置
* 当前内存缓存配置。


[]  baiduimage &dmzj 的动态生成start_urls 
[] 


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



set对应 setting，argument对应自定义参数。
表达能力有限，需要自行扩展：

命令行可以表示简单一阶字典`{"a":"ww","ab":"wb"}`。通过append实现value可以取值列表。

通过=或":"赋值操作实现二阶字典。`{"a":{"aa":"ww","ab":"wb"},"b":"bv"}`

通过；分隔实现二阶列表。
`{"a":{ "wer":{"aa":"ww","ab":"wb"},"aa":"cc"},"b":"bv"}`

**Q**:命令行能否传递json字典，
**A**: 注意字符串"和 回车键的转义。
* 命令行会转义" 编程',使用"""装饰字符串
* 使用python 内置cmdline传递，自带参数分割
* 使用jsonpath，一一指定叶节点值。

[+] 使用先字典后命令行(列表)在转字典，确认转换无误。

扁平化， 把json的结构转船扁平化的key&value。
配合curd 实现json任意尺度编辑，


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




