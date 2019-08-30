# Item



``` python
class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
    referer = scrapy.Field()
    title = scrapy.Field()
    datetime = scrapy.Field()
```



## misc

常见抓取属性



- type：文本的类型，这里就是 article 了

- title：文章的标题

- pageUrl：文章链接

- date：文章的发布时间，其格式为 RFC 1123

- author：作者

- authorUrl：作者的链接

- humanLanguage：语言类型，如英文还是中文等

  

- text：文章的纯文本内容，如果是分段内容，那么其中会以换行符来分隔

- html：提取结果的 HTML 内容

- images：文章中包含的图片
- videos：文章中包含的视频
- numPages：如果文章是多页的，这个参数会控制最大的翻页拼接数目
- nextPages：如果文章是多页的，这个参数可以指定文章后续链接

- discussion：评论内容，和 Disscussion API 返回结果一样



- estimatedDate：如果日期时间不太明确，会返回一个预估的时间，如果文章超过两天或者没有发布日期，那么这个字段就不会返回

- siteName：站点名称

- publisherRegion：文章发布地区

- publisherCountry：文章发布国家

  

- resolvedPageUrl：如果文章是从 pageUrl 重定向过来的，则返回此内容

- tags：文章的标签或者文章包含的实体，根据自然语言处理技术和 DBpedia 计算生成，是一个列表，里面又包含了子字段：

- label：标签名

- count：标签出现的次数

- score：标签置信度

- rdfTypes：如果实体可以由多个资源表示，那么则返回相关的 URL

- uri：Diffbot Knowledge Graph 中的实体链接

- breadcrumb：面包屑导航信息

  



- quotes：引用信息
- sentiment：文章的情感值，-1 到 1 之间
- links：所有超链接的顶级链接
- querystring：请求的参数列表