#  Cookie原理

------

> HTTP是无状态的面向连接的协议, 为了保持连接状态, 引入了Cookie机制

Cookie是http消息头中的一种属性，包括：

- Cookie名字（Name）Cookie的值（Value）
- Cookie的过期时间（Expires/Max-Age）
- Cookie作用路径（Path）
- Cookie所在域名（Domain），使用Cookie进行安全连接（Secure）。
  前两个参数是Cookie应用的必要条件，另外，还包括Cookie大小（Size，不同浏览器对Cookie个数及大小限制是有差异的）。



Chrome 中可以通过document.cookie显示cookie

``` python
from selenium import webdriver
cookies = driver.get_cookies()
```





**不需要知道登录url和表单字段以及其他参数，不需要了解登录的过程和细节。由于不是采用登录url, 用户名+密码的方式。配合工具使用，快速方便。**



scrapy的cookiedemo

```python
for i, url in enumerate(urls):
    yield scrapy.Request("http://www.example.com", meta={'cookiejar': i},
        callback=self.parse_page)

def parse_page(self, response):
    # do some processing
    return scrapy.Request("http://www.example.com/otherpage",
        meta={'cookiejar': response.meta['cookiejar']},
        callback=self.parse_other_page)
```