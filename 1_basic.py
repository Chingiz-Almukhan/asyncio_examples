import asyncio


# не асинхронный так как ждем выполнение каждой корутины
async def one():
    return 1


async def greet():
    await asyncio.sleep(2)
    return 'Hello World'


async def main():
    res1 = await one()  # корутина
    res2 = await greet()

    print(res1)
    print(res2)