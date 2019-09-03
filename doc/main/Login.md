# Login



先通过浏览器访问github的登录页面<https://github.com/login>， 然后使用浏览器调试工具来得到登录时需要提交什么东西:

这里使用chrome浏览器的调试工具，F12打开后选择Network，并将Preserve log和disable cache勾上。 故意输入错误的用户名和密码，得到它提交的form表单参数还有POST提交的URL。

去查看html源码会发现表单里面有个隐藏的`authenticity_token`值，这个是需要先获取然后跟用户名和密码一起提交的

![1567489644532](..\img\1567489644532.png)





1. login
2. post
3. after-login





## 使用request.session

``` python
import re
import requests

self.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'https://github.com/',
    'Host': 'github.com'
}
self.session = requests.Session()
response = self.session.get(self.login_url, headers=self.headers)

if response.status_code != 200:
	print('Get token fail')
	return None
match = re.search(
	r'name="authenticity_token" value="(.*?)"', response.text)
if not match:
	print('Get Token Fail')
	return None
return match.group(1)

# 登录入口
post_data = {
	'commit': 'Sign in',
	'utf8': '✓',
	'authenticity_token': self.get_token(),
	'login': self.email,
	'password': self.password
}
resp = self.session.post(
	self.post_url, data=post_data, headers=self.headers)
```



##  cookiejar



``` python

    start_urls = [
        'https://github.com/issues',

    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://github.com/",
    }

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://github.com/login",
                        meta={'cookiejar': 1}, callback=self.post_login)]
    # FormRequeset
    def post_login(self, response):
        # 先去拿隐藏的表单参数authenticity_token
        authenticity_token = response.xpath(
            '//input[@name="authenticity_token"]/@value').extract_first()
        logging.info('authenticity_token=' + authenticity_token)
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数，如果url跟Request页面的一样就省略掉
        return [FormRequest.from_response(response,
                                          url='https://github.com/session',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.post_headers,  # 注意此处的headers
                                          formdata={
                                              'utf8': '✓',
                                              'login': 'avcc',
                                              'password': '123456',
                                              'authenticity_token': authenticity_token
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                         )]

    def after_login(self, response):
        print('StatusCode:', response.status)
        if response.status != 200:
            print('Login Fail')
        for url in self.start_urls:
            # 因为我们上面定义了Rule，所以只需要简单的生成初始爬取Request即可
            yield Request(url, meta={'cookiejar': response.meta['cookiejar']})

    

    def _requests_to_follow(self, response):
        """重写加入cookiejar的更新"""
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = Request(url=link.url, callback=self._response_downloaded)
                # add cookiejar
                r.meta.update(rule=n, link_text=link.text, cookiejar=response.meta['cookiejar'])
                yield rule.process_request(r)
```



主意事项： FormRequest.from_response依赖form，会从response中搜索form，然后在表单上模拟单击提交。如果页面没有form，则会导致错误`No <form> element found in`，这种情况只能退而使用FormRequest，直接提交数据。



## misc

from scrapy.http import Request, FormRequest





## 模拟登录

##### 使用`scrapy.Formrequest.from_response()`进行登陆

##### 自己直接登陆网站，将登陆成功的`cookies`保存下来，供`Scrapy`直接携带

需要在`settings.py`中的`DOWNLOADER_MIDDLEWARES`**开启中间件scrapy.downloadermiddlewares.cookies.CookiesMiddleware**

如何通过验证码？