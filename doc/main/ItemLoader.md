# ItemLoader

itemLoader???????????????????
## demo

???scrapy?????demo
```python
from scrapy.loader import ItemLoader
from myproject.items import Product
 
def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]',re='(\d+.?\d+)')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()
```

## Selector

???Selector?add_xpath?add_css?add_value???????????Selector?getall()
``` python
	
loader = ItemLoader(item=Item())
header_loader = loader.nested_xpath('//header')
header_loader.add_xpath('social', 'a[@class = "social"]/@href')
header_loader.add_xpath('email', 'a[@class = "email"]/@href')
loader.load_item()
```

## Input and Output processors
???????????,processors?????????????????ItemLoader?Item?
????Input processors??list???list?Output processors??list????????Join?TakeFirst?

* `Identity` ????
* `TakeFirst` ??????????????????
* `Join` ?????????????' '
* `Compose` ????????????????????
* `MapCompose` ????`Compose`????????????????????.
* ???????????????????????????????????????????????????????????* ?????????????
* `SelectJmes` ??json???????????
* 



#### Identity
``` python
from scrapy.loader.processors import Identity
proc = Identity()
lst = ['', 'one', 'two', 'three']
result = proc( lst )
# result = ['', 'one', 'two', 'three']
print(f"result = {result}")
```
#### TakeFirst

#### compose

#### MapCompose

``` python
from scrapy.loader.processors import Identity
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Join
from scrapy.loader.processors import Compose
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import SelectJmes
proc = TakeFirst()
lst = ['', 'one', 'two', 'three']
result = proc( lst )
# result = 'one'
print(f"result = {result}")
proc2 = Compose(lambda v: v[0], str.upper)
proc2(['hello', 'world'])  # 'HELLO'
proc3 = MapCompose(lambda v: v[0], str.upper)
proc3(['hello', 'world'])  # ['H', 'W']
```
#### SelectJmes
?????JSON path????????jmespath(https://github.com/jmespath/jmespath.py)????????????

>>> from scrapy.loader.processors import SelectJmes, Compose, MapCompose
>>> proc = SelectJmes("foo") #for direct use on lists and dictionaries
>>> proc({'foo': 'bar'})
'bar'
>>> proc({'foo': {'bar': 'baz'}})
{'bar': 'baz'}

## ItemLoader
???ItemLoader ???
``` python
class ItemLoader(object):
    default_item_class = Item
    default_input_processor = Identity()
    default_output_processor = Identity()
    default_selector_class = Selector
```
### ItemLoader.processor
???processor??ItemLoader?demo
``` python
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose(str.title)
    name_out = Join()

    price_in = MapCompose(str.strip)
```
input processors ?_in???????output processors ?_out ???????????ItemLoader.default_input_processor ?ItemLoader.default_output_processor ???????? input/output processors?

### Item.processor

???processor??Item?demo
``` python
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value
class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )
    title = scrapy.Field(
        input_processor=MapCompose(TakeFirst),
    )

from scrapy.loader import ItemLoader
il = ItemLoader(item=Product())
il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
il.add_value('price', [u'&euro;', u'<span>1000</span>'])
il.add_value('title', ['abcdefg','hijk','lmn'])
il.load_item()
# {'name': u'Welcome to my website', 'price': u'1000'}

``` 