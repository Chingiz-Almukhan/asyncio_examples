import asyncio


class WriteToFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file_obj = open(self.filename, "w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()


#
# with WriteToFile("test.txt") as f:
#     f.write("Hello, world!")


import aiohttp


class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f"{url}: {html[:20]}"


async def main():
    res = asyncio.create_task(check("https://facebook.com"))
    res2 = asyncio.create_task(check("https://youtube.com"))
    res3 = asyncio.create_task(check("https://google.com"))

    print(await res)
    print(await res2)
    print(await res3)

asyncio.run(main())
