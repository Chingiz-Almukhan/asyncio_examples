import asyncio


async def coro_norm():
    return "Hello world"


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def main():
    try:
        async with asyncio.TaskGroup() as tg:

            res = tg.create_task(coro_norm())
            res2 = tg.create_task(coro_value_error())
            res3 = tg.create_task(coro_type_error())

        results = [res.result(), res2.result(), res3.result()]

    except* ValueError as e:
        print(f'{e=}')
    except* TypeError as e:
        print(f'{e=}')
    else:
        print(f'{results=}')


asyncio.run(main())
