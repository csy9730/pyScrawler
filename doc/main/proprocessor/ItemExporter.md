# ItemExporter

BaseItemExporter
``` python
class scrapy.exporters.BaseItemExporter(fields_to_export=None, export_empty_fields=False, encoding='utf-8', indent=0, dont_fail=False):
    def start_exporting():
        pass
    # 响应导出过程的开始和结束，执行相应动作。
    def finish_exporting():
        pass
    def export_item(item):
        pass
    def serialize_field(self, field, name, value):
        # 每个属性对应的序列化的方法
        pass
    def fields_to_export():
        # 返回 需要导出的属性列表，或者返回None代表全部属性。
        pass

```
XmlItemExporter
``` python
classs crapy.exporters.XmlItemExporter(file, item_element='item', root_element='items', **kwargs):
    pass
# Exports items in XML format to the specified file object.
```
CsvItemExporter

PickleItemExporter

PprintItemExporter

JsonItemExporter

JsonLinesItemExporter

MarshalItemExporter
# Feed exports

