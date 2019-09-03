# middleware



## DownloaderMiddleware
DownloaderMiddleware主要处理请求Request发出去和结果Response返回的一些回调，

比如说你要加UserAgent，使用代理，修改refferer，添加cookie，或者请求异常超时处理啥的

主要有几个方法：

``` python
process_request(request, spider)
# 当每个request通过下载中间件时，该方法被调用，这里可以修改UA，代理，Refferer

process_response(request, response, spider) # 这里可以看返回是否是200加入重试机制

process_exception(request, exception, spider) # 这里可以处理超时
```





## SpiderMiddleware

SpiderMiddleware主要处理解析Item的相关逻辑修正，比如数据不完整要添加默认，增加其他额外信息等

``` python
process_spider_input(response, spider)# 当response通过spider中间件时，该方法被调用，处理该response。

rocess_spider_output(response, result, spider)
# 当Spider处理response返回result时，该方法被调用。

process_spider_exception(response, exception, spider)
# 当spider或(其他spider中间件的) process_spider_input() 跑出异常时， 该方法被调用。

```

