import asyncio
import aiohttp

url = 'http://httpbin.org/post'
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

data = {
    'data': 'person data',
}

# 定义异步函数 main()
async def main():
    # 获取 session 对象
    async with aiohttp.ClientSession() as session:
        # post 方式请求 httbin
        async with session.post(url=url, headers=headers, data=data) as response:
            print(response.status)
            print(await response.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())