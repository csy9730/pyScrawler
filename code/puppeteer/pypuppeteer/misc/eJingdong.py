import requests
from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio

import json_lines
import json
from functools import reduce
fExt= lambda x,y:[*x,*y]

def jsonlineWrite(pfn,lst,enc="utf-8",**entries):
    with open( pfn,'a+',encoding=enc) as fp:
        for item in lst:
            fp.write(json.dumps(item,**entries)+'\n')

def jsonlineShow(pfn,enc="utf-8"):
    lst =[]
    with open(pfn, 'r',encoding=enc) as f:
        for item in json_lines.reader(f):
            lst.append(item)
    return lst

def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main(url):
    # browser = await launch({'headless': False, 'args': ['--no-sandbox'], })
    browser = await launch({
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
    width, height = screen_size()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto(url,options={'timeout': 90000})
    print(url)
    # await asyncio.sleep(2)
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
    await asyncio.sleep(1)  

    # content = await page.content()
    li_list = await page.xpath('//*[@id="J_goodsList"]/ul/li')

    # print(li_list)
    item_list = []
    for li in li_list:
        a = await li.xpath('.//div[@class="p-img"]/a')
        detail_url = await (await a[0].getProperty("href")).jsonValue()
        promo_words = await (await a[0].getProperty("title")).jsonValue()
        a_ = await li.xpath('.//div[@class="p-commit"]/strong/a')
        p_commit = await (await a_[0].getProperty("textContent")).jsonValue()
        # i = await li.xpath('./div/div[3]/strong/i')
        i = await li.xpath('//div[@class="tab-content-item"]//div[@class="p-price"]//strong/i')
        price = await (await i[0].getProperty("textContent")).jsonValue()
        # em = await li.xpath('./div/div[4]/a/em')
        em = await li.querySelectorAll('div.p-name a em')

        title = await (await em[0].getProperty("textContent")).jsonValue()
        item = {
            "title": title.replace(u'\xa0',u' '),
            "detail_url": detail_url.replace(u'\xa0',u' '),
            "promo_words": promo_words.replace(u'\xa0',u' '),
            'p_commit': p_commit.replace(u'\xa0',u' '),
            'price': price.replace(u'\xa0',u' ')
        }
        item_list.append(item)
        # print(item)
        # break
    # print(content)

    await page_close(browser)
    return item_list


async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close()


msg = "手机"
msg = "显卡"
url = "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&cid2=653&cid3=655&page={}"
url = "https://search.jd.com/search?keyword={}&enc=utf-8&qrst=1&stop=1&vt=2&wq={}&cid2=677&page={}"
# "page=5&s=121&click=0"
task_list = []
url_list = [  url.format(msg, msg,  i * 2 + 1) for i in range(0,2) ]
print(url_list)
for ur in url_list:
    task_list.append(main( ur ))

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*task_list))
print(results, len(results),type(results))
jsonlineWrite("scr_jingdong3.jl",reduce(fExt,results),ensure_ascii=False)



# soup = BeautifulSoup(content, 'lxml')
# div = soup.find('div', id='J_goodsList')
# for i, li in enumerate(div.find_all('li', class_='gl-item')):
#     if li.select('.p-img a'):
#         print(li.select('.p-img a')[0]['href'], i)
#         print(li.select('.p-price i')[0].get_text(), i)
#         print(li.select('.p-name em')[0].text, i)
#     else:
#         print("#" * 200)
#         print(li)