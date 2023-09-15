import asyncio
from random import randint


async def waiter(condition, pk):
    async with condition:
        print(f"Waiter {pk} is awaiting")
        await condition.wait()

        num = randint(1, 5)
        print(f"Waiter with {pk} generated {num}")


async def starter(condition):
    print("Starting sleeping for 5 secs")
    await asyncio.sleep(5)

    async with condition:
        # condition.notify_all()
        condition.notify(3)


async def main():
    condition = asyncio.Condition()
    waiters = [
        asyncio.create_task(
            waiter(condition, pk=i)
        )
        for i in range(5)
    ]
    asyncio.create_task(starter(condition))

    await asyncio.gather(*waiters)


asyncio.run(main())
