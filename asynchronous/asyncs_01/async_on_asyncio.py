import aiohttp
import asyncio
import requests
from time import time


URL = 'https://loremflickr.com/320/240'


# synchronous

def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    f_name = response.url.split('/')[-1]
    with open(f_name, 'wb') as f:
        f.write(response.content)


def main_sync():
    start_time = time()
    for i in range(10):
        write_file(get_file(URL))
    print(time() - start_time)


# if __name__ == '__main__':
#     main_sync()   # 2.476003885269165


# asynchronous

def write_img(data):
    f_name = f'file-{int(time() * 1000)}.jpeg'
    with open(f_name, 'wb') as f:
        f.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_img(data)  # bad idea to mix asynchronous and synchronous code


async def main_async():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(URL, session))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t = time()
    asyncio.run(main_async())
    print(time() - t)
