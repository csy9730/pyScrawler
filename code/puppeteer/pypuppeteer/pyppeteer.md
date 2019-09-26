# pyppeteer

`pip install pyppeteer`

``` python
    # 模拟输入 账号密码  {'delay': rand_int()} 为输入时间
    await page.type('#TPL_username_1', "sadfasdfasdf")
    await page.type('#TPL_password_1', "123456789", )
    
    await page.waitFor(1000)
    await page.click("#J_SubmitStatic")
    ```

   f'Protocol Error ({method}): Session closed. Most likely the '

``` python
# 抓取新闻内容  可以使用 xpath 表达式
# Pyppeteer 三种解析方式
Page.querySelector()  # 选择器
Page.querySelectorAll()
Page.xpath()  # xpath  表达式
# 简写方式为：
Page.J(), Page.JJ(), and Page.Jx()
``` 
## 问题
pyppeteer.errors.NetworkError: Protocol Error (Runtime.evaluate): Session closed. Most likely the page has been closed.

pyppeteer.errors.TimeoutError: Navigation Timeout Exceeded: 30000 ms exceeded.