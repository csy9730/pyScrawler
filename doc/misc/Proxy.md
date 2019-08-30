# Proxy



## 1

**在settings配置文件中新增IP池:**

```python
IPPOOL=[  
    {"ipaddr":"61.129.70.131:8080"},  
    {"ipaddr":"61.152.81.193:9100"},  
    {"ipaddr":"120.204.85.29:3128"},  
    {"ipaddr":"219.228.126.86:8123"},  
    {"ipaddr":"61.152.81.193:9100"},  
    {"ipaddr":"218.82.33.225:53853"},  
    {"ipaddr":"223.167.190.17:42789"}  
]
```



**在settings中设置DOWNLOADER_MIDDLEWARES**

```
DOWNLOADER_MIDDLEWARES = {
#    'youx.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'youx.middlewares.MyproxiesSpiderMiddleware': 125
} 
```



```python
import random  
from scrapy import signals  
from youx.settings import IPPOOL  

class MyproxiesSpiderMiddleware(object):  
	def __init__(self,ip=''):  
      self.ip=ip  

  def process_request(self, request, spider):  
      thisip=random.choice(IPPOOL)  
      print("this is ip:"+thisip["ipaddr"])  
      request.meta["proxy"]="http://"+thisip["ipaddr"] 
```