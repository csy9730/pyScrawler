#  ImagesPipeline





Scrapy提供了专门处理下载的Pipeline，包括文件下载和图片下载。下载文件和图片的原理与抓取页面的原理一样，因此下载过程支持异步和多线程，下载十分高效。下面我们来看看具体的实现过程。 

官方文档地址为：https://doc.scrapy.org/en/latest/topics/media-pipeline.html。

首先定义存储文件的路径，需要定义一个`IMAGES_STORE`变量，在settings.py中添加如下代码：

```javascript
IMAGES_STORE = './images'
```

在这里我们将路径定义为当前路径下的images子文件夹，即下载的图片都会保存到本项目的images文件夹中。

内置的`ImagesPipeline`会默认读取Item的`image_urls`字段，并认为该字段是一个列表形式，它会遍历Item的`image_urls`字段，然后取出每个URL进行图片下载。

但是现在生成的Item的图片链接字段并不是`image_urls`字段表示的，也不是列表形式，而是单个的URL。所以为了实现下载，我们需要重新定义下载的部分逻辑，即要自定义`ImagePipeline`，继承内置的`ImagesPipeline`，重写几个方法。

我们定义`ImagePipeline`，如下所示：

```javascript
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])
```

在这里我们实现了`ImagePipeline`，继承Scrapy内置的`ImagesPipeline`，重写下面几个方法。

- `get_media_requests()`。它的第一个参数`item`是爬取生成的Item对象。我们将它的`url`字段取出来，然后直接生成Request对象。此Request加入到调度队列，等待被调度，执行下载。
- `file_path()`。它的第一个参数`request`就是当前下载对应的Request对象。这个方法用来返回保存的文件名，直接将图片链接的最后一部分当作文件名即可。它利用`split()`函数分割链接并提取最后一部分，返回结果。这样此图片下载之后保存的名称就是该函数返回的文件名。
- `item_completed()`，它是当单个Item完成下载时的处理方法。因为并不是每张图片都会下载成功，所以我们需要分析下载结果并剔除下载失败的图片。如果某张图片下载失败，那么我们就不需保存此Item到数据库。该方法的第一个参数`results`就是该Item对应的下载结果，它是一个列表形式，列表每一个元素是一个元组，其中包含了下载成功或失败的信息。这里我们遍历下载结果找出所有成功的下载列表。如果列表为空，那么该Item对应的图片下载失败，随即抛出异常DropItem，该Item忽略。否则返回该Item，说明此Item有效。

## FilesPipeline

``` python
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from douban.items import doubanTextItem,doubanItem
import json
class doubanPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,doubanTextItem):   #判断item是否为doubanTextItem类型
            name = item['title'] + '.txt'
            with open(name, 'a', encoding='utf-8') as f:
                text = "".join(item['text'])
                f.write(text)
        return item                         #返回item
class doubanFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item, doubanItem):        #判断item是否为doubanItem类型
            for image_url in item['file_urls']:
                if 'http' in image_url:
                    name = item['name']
                    yield scrapy.Request(url=image_url, meta={'name': name})
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        file_name = image_guid.split('.')[0] + '.jpg'
        name = request.meta['name']
        if len(name):
            file_name=name+'/'+file_name
        return 'full/%s' % (file_name)
    def item_completed(self, results, item, info):
        if isinstance(item, doubanItem):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            # item['image_paths'] = image_paths
            return item
```

