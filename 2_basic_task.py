import asyncio


# simple пример с задачей
async def coro():
    return 1


async def main_with_task():
    task = asyncio.create_task(coro())
    await task
    print(dir(task))
    print(task.done())

asyncio.run(main_with_task())
