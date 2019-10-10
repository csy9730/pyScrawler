# customSpider



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

# spider
# item
# item loader
```