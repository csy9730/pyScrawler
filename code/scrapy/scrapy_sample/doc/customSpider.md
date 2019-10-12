# customSpider


所有配置：
* spiderClass
* itemClass
* itemLoaderClass
* rule+linkextractor: re,xpath,
* callback : re,callback()
* start_urls: 静态分配+字典生成，动态生成？？？
* 


``` python
allowed_domains = "allowed_domains"
name = "name"
domain = "domain"

start_urls = [ dct[  ].format(**dct]  for dct in urlDictLst ]

ks = ["follow","callback"]
for dct in ruleLst:
	d = { k:v  for k,v in dct.items() if k not in  ks }
	d2 = { k:v  for k,v in dct.items() if k  in  ks2 }
	rule = Rule(LinkExtractor(**d), **d2 )


    routes = [  {"allow":"/\\d+$","callback":"parse_article"} ,
                    {"allow":"/page/\\d+/","callback":"parse_nop"} ,
        ]        
    for r in routes:
        r.update(allow_res=re.compile(r["allow"]))

	def parse_start_url(self, response):          
		for ar in self.routes:
			if ar["allow_res"].search(response.url):
				return getattr(self,  ar["callback"] ) (response) 
		return self.parse_article(response)
```