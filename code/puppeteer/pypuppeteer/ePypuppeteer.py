import asyncio
from pyppeteer import launch
import os,sys
pth = 'D:/Project/myLib/tool_misc/js/puppeteer/node_modules/_puppeteer@1.20.0@puppeteer/.local-chromium/win64-686378/chrome-win'
sys.path.append(pth)
os.environ['PATH'] +=(';'+pth)
os.environ['PYPPETEER_HOME'] =pth
async def main():
    browser = await launch({       
       # r'C:\Users\csy_acer_win8\AppData\Roaming\npm\node_modules\puppeteer\.local-chromium\win64-686378\chrome-win',
        "headless":False,
    })
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'scr_example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())