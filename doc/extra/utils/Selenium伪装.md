# Selenium伪装



## remote-debugging

首先cmd 运行命令chrome.exe --remote-debugging-port=9222 打开一个浏览器，然后py代码里chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")添加一个这个Options。其它的代码不变



## mitmproxy

**mitmproxy** is a free and open source interactive HTTPS proxy.

```text
    pip install mitmproxy
```



**基本使用方法：**

1. **给本机设置代理ip 127.0.0.1端口8001（为了让所有流量走mitmproxy）具体方法请百度。**

**2. 启动mitmproxy。**

**windows：**

```text
mitmdump -p 8001
```

**3. 打开chrome的开发者工具，找到目标网站是通过哪个js文件控制webdriver相应的，**

开始写干扰脚本(DriverPass.py)：

import re
from mitmproxy import ctx

def response(flow): 
    if '/js/yoda.' in flow.request.url:
        for webdriver_key in ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate', '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped', '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium', 'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw', 'driver-evaluate', 'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand', 'webdriver-evaluate-response', '__webdriverFunc', '__webdriver_script_fn', '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm', '__lastWatirPrompt', '$chrome_asyncScriptInfo', '$cdc_asdjflasutopfhvcZLmcfl_' ]:
            ctx.log.info('Remove "{}" from {}.'.format(
            webdriver_key, flow.request.url
            ))  
        flow.response.text = flow.response.text.replace('"{}"'.format(webdriver_key), '"NO-SUCH-ATTR"')  
    flow.response.text = flow.response.text.replace('t.webdriver', 'false')
    flow.response.text = flow.response.text.replace('ChromeDriver', '')
5. 退出刚才的mitmproxy状态，重新用命令行启动mitmproxy干扰脚本 监听8001端口的请求与响应。

mitmdump -s DriverPass.py -p 8001

6. 现在别管mitmproxy，启动webdriver 顺利获得cookies。
7. 

## misc



浏览器中的window.navigator.webdriver属性被JS暴露了出来，而被服务器端所识别，触发了服务器的反爬策略，导致爬取失败



1. Chrome从**v63版本**开始添加了这一属性，那么我们就可以使用低于v63版本的Chrome来实现即可(v62.0.3202.62版本测试通过，当然也不要忘了将chromedriver换成对应的版本)。
2. 使用google新推出的puppeteer，现在已经有对应的python版本pyppeteer，功能非常强大，绝对算得新一代爬虫利器，相信你去用了之后会爱上它的。API参考地址：



按键模拟+抓包

