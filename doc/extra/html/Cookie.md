#  Cookie原理

------

> HTTP是无状态的面向连接的协议, 为了保持连接状态, 引入了Cookie机制

Cookie是http消息头中的一种属性，包括：

- Cookie名字（Name）Cookie的值（Value）
- Cookie的过期时间（Expires/Max-Age）
- Cookie作用路径（Path）
- Cookie所在域名（Domain），使用Cookie进行安全连接（Secure）。
  前两个参数是Cookie应用的必要条件，另外，还包括Cookie大小（Size，不同浏览器对Cookie个数及大小限制是有差异的）。

数据如下所示（json格式)：

```json
[
    {
        "domain": "www.baidu.com",
        "expiry": 2513673649,
        "httpOnly": false,
        "name": "ORIGIN",
        "path": "/",
        "secure": false,
        "value": "2"
    },
    {
        "domain": "www.baidu.com",
        "expiry": 2513673649,
        "httpOnly": false,
        "name": "sug",
        "path": "/",
        "secure": false,
        "value": "3"
    }
]
```



## 获取cookies

如果只想查看页面Cookie。那么和简单，在你的要查看的cookie的页面上。直接在地址栏前面的文档薄上点击，如图所示：



就会出现Chrome维护的所有的cookie。

![1568700016300](..\img\1568700016300.png)

然后 选择一个cookie名称后点击就可以查看cookie的详细内容,字符串如下：

``` 
"BIDUPSID=834591DE5266799C7BA5496FA7CBC646; PSTM=1555569460; H_WISE_SIDS=132886_125704_127759_131452_132775_132507_128064_132126_132686_120221_133017_132909_133041_131247_132439_130763_132394_132378_132325_132213_131518_132260_118886_118873_131401_118843_118818_118802_131650_131577_132840_131534_131529_133158_132604_129565_107315_132590_132782_130122_131874_132770_131196_133352_132565_133478_133302_132890_129651_132557_132542_133290_131905_128892_132293_132551_132498_133387_129646_131423_133211_133414_132904_110085_127969_133153_123290_131748_127315_133194_127416_131549_133343; BD_UPN=12314753; BDSFRCVID=r1FOJeC62AlH653wDpNguRPdGeQWX96TH6aomj7OUDHhgpYZNembEG0PHM8g0KubT4X3ogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0P3J; BD_HOME=1; BD_CK_SAM=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; COOKIE_SESSION=1380194_1_6_7_9_20_0_2_4_6_3_0_1380213_0_26_0_1568197414_1566799864_1568197388%7C9%238885898_1_1566799853%7C2; PSINO=6; H_PS_PSSID=1420_21082_18560_29523_29518_29721_29567_29221_22159; delPer=0; BAIDUID=834591DE5266799C7BA5496FA7CBC848:FG=1; H_BDCLCKID_SF=tJkfoC05tKD3f-tk2tRVb4DOqlOybTnU5e79aJ5nJDoKhxO8MlLBh-LR3-cGQnoqamOHVnTOQpP-HqIR5pD--U-YD-TD5lOlQjndKl0MLn5Wbb0xynoDbUKpBUnMBMPe52OnaIbg3fAKftnOM46JehL3346-35543bRTohFLtD0aMK_ljT03KP4E52Ty2t70aDTbW-38HJrqfKvRjMrcy4LdhtAqLJbyLeQfQb590h6IVhOYhfRvD--g3-7Q2n505jTrVxO_MT6RsMQ_bf--QfbQ0hOhqP-jW5TaKfbxLJ7JOpkxbUnxy5KUQRPH-Rv92DQMVU52QqcqEIQHQT3mDUThDG0tJ6kjJnusL-35HJoHjJbGq4bohjnDbb39BtQmQnTxohbEL-QbSlOdyfcIhxF9bPRiBn3NQNnTBJOmLD5aOCtmLROBLpKN0bJX0x-jLTnRLq6D-45DOCoE04nJyUnQbPnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3TJMIEtJ-joC-btDL3JJRzbCT_htub5xLX5-RLf5uDKq7F5l8-hlj1y5DhDn-vK-TM-ljT5gv-bx39fCQxOKQphPc8jU4AQ-73KbOkyeo-WRoN3KJmOhC9bT3v5tD7jbAe2-biWb7M2MbdJpbP_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDcjqR8ZD68be55P; ZD_ENTRY=bing; sug=3; sugstore=0; ORIGIN=2; bdime=0"
```







Chrome 中可以通过devtool的document.cookie显示cookie



selenium通过以下

``` python
from selenium import webdriver
cookies = driver.get_cookies()

get_cookies() # 读取所有cookie
get_cookie(name) # 读取指定cookie
add_cookie(dict) # 添加cookie
delete_all_cookies() # 删除所有cookie
delete_cookie(name) # 删除指定cookie
```



## 登录



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



