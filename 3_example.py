import asyncio


# Решение проблемы из первого примера

async def one_t():
    return 1


async def greet_t(timeout: int):
    await asyncio.sleep(timeout)
    return 'Hello World'


async def main_t():
    res1 = asyncio.create_task(one_t())  # возвращает экземпляр класса Task
    res2 = asyncio.create_task(greet_t(2))
    res3 = asyncio.create_task(greet_t(3))
    res4 = asyncio.create_task(greet_t(20))
    res5 = asyncio.create_task(greet_t(3))
    res6 = asyncio.create_task(greet_t(2))

    print(await res1)
    print(await res2, "res 2")
    print(await res3, "res 3")
    print(await res4, "res 4")
    print(await res5, "res 5")
    print(await res6, "res 6")


asyncio.run(main_t())
