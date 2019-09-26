import asyncio
from pyppeteer import launch


async def main():
    # headless参数设为False，则变成有头模式
    # Pyppeteer支持字典和关键字传参，Puppeteer只支持字典传参
    
    # 指定引擎路径
    # exepath = r'C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458\chrome-win32/chrome.exe'
    # browser = await launch({'executablePath': exepath, 'headless': False, 'slowMo': 30})
    url = 'https://www.toutiao.com/'
    browser = await launch({
        # headless=False,
        'dumpio': True,
        'headless':False,
        'args': [
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
        ],
    })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')


    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    # 是否启用JS，enabled设为False，则无渲染效果
    # await page.setJavaScriptEnabled(enabled=True)
    # 超时间见 1000 毫秒
    await page.goto(url)    
    print("page.goto")
    
    """"""
    # res = await page.goto( url , options={'timeout': 9000})
    # resp_headers = res.headers  # 响应头
    # resp_status = res.status  # 响应状态
    
    # 等待
    await asyncio.sleep(2)
    # 第二种方法，在while循环里强行查询某元素进行等待
    # while not await page.querySelector('.t'):
    #    pass

    # 滚动到页面底部
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

    await asyncio.sleep(2)
    # 截图 保存图片
    await page.screenshot({'path': 'scr_toutiao.png'})

    # 打印页面cookies
    print(await page.cookies())

    """  打印页面文本 """
    # 获取所有 html 内容
    res = await page.content()
    print( res )

    # 在网页上执行js 脚本
    dimensions = await page.evaluate(pageFunction='''() => {
            return {
                width: document.documentElement.clientWidth,  // 页面宽度
                height: document.documentElement.clientHeight,  // 页面高度
                deviceScaleFactor: window.devicePixelRatio,  // 像素比 1.0000000149011612
            }
        }''', force_expr=False)  # force_expr=False  执行的是函数
    print(dimensions)

    #  只获取文本  执行 js 脚本  force_expr  为 True 则执行的是表达式
    content = await page.evaluate(pageFunction='document.body.textContent', force_expr=True)
    print(content)

    # 打印当前页标题
    print(await page.title())

    # 抓取新闻内容  可以使用 xpath 表达式
    """
    # Pyppeteer 三种解析方式
    Page.querySelector()  # 选择器
    Page.querySelectorAll()
    Page.xpath()  # xpath  表达式
    # 简写方式为：
    Page.J(), Page.JJ(), and Page.Jx()
    """
    element = await page.querySelector(".feed-infinite-wrapper > ul>li")  # 纸抓取一个
    print(element)
    # 获取所有文本内容  执行 js
    content = await page.evaluate('(element) => element.textContent', element)
    print(content)

    # elements = await page.xpath('//div[@class="title-box"]/a')
    elements = await page.querySelectorAll(".title-box a")
    for item in elements:
        print(await item.getProperty('textContent'))
        # <pyppeteer.execution_context.JSHandle object at 0x000002220E7FE518>

        # 获取文本
        title_str = await (await item.getProperty('textContent')).jsonValue()

        # 获取链接
        title_link = await (await item.getProperty('href')).jsonValue()
        print(title_str)
        print(title_link)

    # 关闭浏览器
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())