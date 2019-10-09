# Request



一开始要导入 Requests 模块：

```
>>> import requests
```

然后，尝试获取某个网页。本例子中，我们来获取 Github 的公共时间线：

```
>>> r = requests.get('https://api.github.com/events')
```

现在，我们有一个名为 `r` 的 [`Response`](http://cn.python-requests.org/zh_CN/latest/api.html#requests.Response) 对象。我们可以从这个对象中获取所有我们想要的信息。

Requests 简便的 API 意味着所有 HTTP 请求类型都是显而易见的。例如，你可以这样发送一个 HTTP POST 请求：

```
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```

漂亮，对吧？那么其他 HTTP 请求类型：PUT，DELETE，HEAD 以及 OPTIONS 又是如何的呢？都是一样的简单：

```
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')
```

都很不错吧，但这也仅是 Requests 的冰山一角呢。

 `r.text`和 `r.content`，content对应bytes类型？text对应有编码的str类型，

``` python
byt = response.body #  type = bytes
text = response.text  #  type =str
```

```python
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
```

## 定制请求头

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

