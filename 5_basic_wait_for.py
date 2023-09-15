import asyncio


async def greet_t(timeout: int):
    await asyncio.sleep(timeout)
    return 'Функция выполнена'


async def main_t():
    long_task = asyncio.create_task(greet_t(5))

    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=2)
    except asyncio.TimeoutError:
        print("The long task cancelled")
        result = await long_task

    print(result)


asyncio.run(main_t())
