import asyncio

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


class CustomException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


async def server_return_error():
    await asyncio.sleep(2)
    raise CustomException("Failed to connect")


async def main():
    # coros = [
    #     check("https://facebook.com"),
    #     check("https://youtube.com"),
    #     check("https://google.com"),
    #     # check("https://geafeaeafaefoogle.com")
    # ]

    # results = await asyncio.gather(*coros,
    #                                # server_return_error(),
    #                                return_exceptions=False
    #                                )  # return_exceptions=True для возвращения корутин и ошибок
    #
    # for res in results:
    #     print(res)

    # for coro in asyncio.as_completed(coros): # резы возвращается по мере работы
    #     res = await coro
    #     print(res)
    group1 = asyncio.gather(
        check("https://facebook.com"),
        check("https://twitter.com"),
    )
    group2 = asyncio.gather(
        check("https://google.com"),
        check("https://twitch.com"),
    )

    groups = asyncio.gather(group1, group2)

    res = await groups

    for r in res:
        print(r)


asyncio.run(main())
