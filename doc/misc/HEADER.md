# HEADER



## header

### 查看

```
def parse(self, response):
    print(response.request.headers)

```



![1566551927137](./img/1566551927137.png)



### 模拟浏览器头

1. 单次模拟

``` python
user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' 
headers = {'User_agent': user_agent}
r=requests.get(url,headers=headers)
```

2. 固定头

``` python
DEFAULT_REQUEST_HEADERS = {
    'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'https://www.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
}
```

3. 在middlewares.py 中使用随机浏览器头

启用USER_AGENT_LIST

``` python

```



## 浏览器头

以下是google浏览器的request头部

``` 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3

Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _ga=GA1.2.1822517096.1567062426; _gid=GA1.2.536599681.1567062426;Hm_lvt_f89e0235da0841927341497d774e7b15=1567062427;Hm_lpvt_f89e0235da0841927341497d774e7b15=1567062427

Host: www.ruanyifeng.com
If-Modified-Since: Wed, 28 Aug 2019 02:45:49 GMT
If-None-Match: "ff07-5912462fe9f80-gzip"
Referer: https://cn.bing.com/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
```

