# 动态网页爬取



动态页面分为：　ajax请求和js异步渲染data（data存在js页面）。

如何获取动态网页的动态数据？

1. 直接渲染网页
2. 模拟请求，再解析返回数据（json，js，html）



直接渲染网页的方法包括：selenium，scrapy-splash。





##　模拟请求



人工debug获得api接口，人工debug方法包括：

1. 简单地人工总结拼凑参数生成请求url（api接口）
2. 对于js加密param的情况，python中运行js语句，生成请求url。





network查看initialor

​		



