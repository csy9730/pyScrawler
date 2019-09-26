import asyncio
import pyppeteer
from collections import namedtuple

Response = namedtuple("rs", "title url html cookies headers history status")


async def get_html(url):
    browser = await pyppeteer.launch(headless=True, args=['--no-sandbox'])
    page = await  browser.newPage()
    res = await page.goto(url) # , options={'timeout': 3000}
    data = await page.content()
    title = await page.title()
    resp_cookies = await page.cookies()  # cookie
    resp_headers = res.headers  # 响应头
    resp_status = res.status  # 响应状态
    print(data)
    print(title)
    print(resp_headers)
    print(resp_status)
    return title


if __name__ == '__main__':
    url_list = ["https://www.toutiao.com/",
                "http://jandan.net/ooxx/page-8#comments",
                "https://www.12306.cn/index/"
               ]
    task = [get_html(url) for url in url_list]

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*task))
    for res in results:
        print(res)

headers = {'date': 'Sun, 28 Apr 2019 06:50:20 GMT',
           'server': 'Cmcc',
           'x-frame-options': 'SAMEORIGIN\nSAMEORIGIN',
           'last-modified': 'Fri, 26 Apr 2019 09:58:09 GMT',
           'accept-ranges': 'bytes',
           'cache-control': 'max-age=43200',
           'expires': 'Sun, 28 Apr 2019 18:50:20 GMT',
           'vary': 'Accept-Encoding,User-Agent',
           'content-encoding': 'gzip',
           'content-length': '19823',
           'content-type': 'text/html',
           'connection': 'Keep-alive',
           'via': '1.1 ID-0314217270751344 uproxy-17'}