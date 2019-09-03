# Selector



scrapy的selector支持xpath，css和re。

### xpath

避免使用数组索引
@class 少用
@id 
使用功能描述作为特征
目标特征 img ,href,

//*[contains(@class,"ltr") and contain(@class,"skin-vector")]//h1//text()

//div[starts-with(@class,'reflist')]//a/@href

## CSS



## RE

## extract

So, the main difference is that output of .get() and .getall() methods is more predictable: .get() always returns a single result, .getall() always returns a list of all extracted results. With .extract() method it was not always obvious if a result is a list or not; to get a single result either .extract() or .extract_first() should be called.

## misc







对于多变属性，使用或连接捕抓，在从列表选一个。
对于网页编码，GBK编码都不够用，存在特殊表情字符，难以转存





