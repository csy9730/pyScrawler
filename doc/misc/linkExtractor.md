# linkExtractor



linkExtractor可以提取网页的超链接。源码如下，` from .lxmlhtml import LxmlLinkExtractor as LinkExtractor`

``` python

class LxmlLinkExtractor(FilteringLinkExtractor):

    def __init__(self, allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(),
                 tags=('a', 'area'), attrs=('href',), canonicalize=False,
                 unique=True, process_value=None, deny_extensions=None, restrict_css=(),
                 strip=True, restrict_text=None):
        tags, attrs = set(arg_to_iter(tags)), set(arg_to_iter(attrs))
        tag_func = lambda x: x in tags
        attr_func = lambda x: x in attrs
        lx = LxmlParserLinkExtractor(
            tag=tag_func,
            attr=attr_func,
            unique=unique,
            process=process_value,
            strip=strip,
            canonicalized=canonicalize
        )

        super(LxmlLinkExtractor, self).__init__(lx, allow=allow, deny=deny,
                                                allow_domains=allow_domains, deny_domains=deny_domains,
                                                restrict_xpaths=restrict_xpaths, restrict_css=restrict_css,
                                                canonicalize=canonicalize, deny_extensions=deny_extensions,
                                                restrict_text=restrict_text)

    def extract_links(self, response):
        base_url = get_base_url(response)
        if self.restrict_xpaths:
            docs = [subdoc
                    for x in self.restrict_xpaths
                    for subdoc in response.xpath(x)]#xpath 提取
        else:
            docs = [response.selector]
        all_links = []
        for doc in docs:
            links = self._extract_links(doc, response.url, response.encoding, base_url)
            all_links.extend(self._process_links(links))
        return unique_list(all_links)
```



allow：接收一个正则表达式或一个正则表达式列表，提取绝对url于正则表达式匹配的链接，如果该参数为空，默认全部提取。

deny：接收一个正则表达式或一个正则表达式列表，与allow相反，排除绝对url于正则表达式匹配的链接，换句话说，就是凡是跟正则表达式能匹配上的全部不提取。

restrict_xpaths：（str or list）我们在最开始做那个那个例子，接收一个xpath表达式或一个xpath表达式列表，提取xpath表达式选中区域下的链接。

restrict_css：（str or list）这参数和restrict_xpaths参数经常能用到

restrict_xpaths和restrict_css 是并列关系，都可以捕抓链接。如果两者都为空，则不生效，使用全部文本。

restric_text: re正则表达式捕抓连接。



\>tags：接收一个标签（字符串）或一个标签列表，提取指定标签内的链接，默认为tags=（‘a’，‘area’）

\>attrs：接收一个属性（字符串）或者一个属性列表，提取指定的属性内的链接，默认为attrs=（‘href’，），示例，按照这个中提取方法的话，这个页面上的某些标签的属性都会被提取出来，如下例所示，这个页面的a标签的href属性值都被提取到了。

**process_value** :可以改变url的值或返回None，默认为lambda x:x



``` python
def parse(self, response):
         link = LinkExtractor(tags='a',attrs='href')
         links = link.extract_links(response)
         print(type(links))
         for link in links:
             print(link)
```

## 

