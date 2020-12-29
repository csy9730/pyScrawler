#  processors


``` python
from scrapy.loader.processors import Identity
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Join
from scrapy.loader.processors import Compose
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import SelectJmes
from w3lib.html import remove_tags
proc = TakeFirst()
lst = ['', 'one', 'two', 'three']
result = proc( lst )
# result = 'one'
print(f"result = {result}")
proc2 = Compose(lambda v: v[0], str.upper)
proc2(['hello', 'world'])  # 'HELLO'
proc3 = MapCompose(lambda v: v[0], str.upper)
proc3(['hello', 'world'])  # ['H', 'W']
proc4 = Compose( TakeFirst(),lambda x:x+'/')
proc4( lst)  # 'one/'

proc5 = SelectJmes("foo") #for direct use on lists and dictionaries
proc5({'foo': 'bar'}) # 'bar'
proc5({'foo': {'bar': 'baz'}}) # {'bar': 'baz'}
remove_tags(u'<strong>website</strong>') # website
```

**Q**:` Compose(TakeFirst)` 会导致` ·`TypeError: object() takes no parameters`
**A**: 必须使用`Compose(TakeFirst() )`