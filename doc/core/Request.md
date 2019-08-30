# Request





## Response.follow

Spider.Resquest的作用，Response.follow也有同样的功能，不过多了一些小区别。

一、Response.follow可以使用相对地址 
这是第一点不同，Resquest需要你提供完整的url才可以进行请求。

二、Response.follow可以使用选择器

for href in response.css('li.next a::attr(href)'):
    yield response.follow(href, callback=self.parse)
1
2
如果你不想使用url，可以使用css选择器，不过必须要使用其中包含url参数的选择器

三、Response.follow可以使用标签

for a in response.css('li.next a'):
    yield response.follow(a, callback=self.parse)
1
2
如果你连带url参数选择器都不想使用，可以直接使用带url的标签传递，response.follow会自动使用其中的url



## urllib

python2使用urllib2
python3使用urllib
import urllib.request as urllib2

1. 通过python自带的urllib模块，不需要安装，直接from urllib import request，直接使用request对象做Http请求的发送。
2. 通过第三方的requests模块，需要pip install安装（推荐，因为API人性化）

1.  Requests 使用的是 urllib3，继承了urllib2的所有特性

