import asyncio


async def coro(msg):
    print(msg)
    await asyncio.sleep(1)
    print(msg)


async def main():
    # print(asyncio.all_tasks())
    print("--- main beginning")

    asyncio.create_task(coro("text"))

    await asyncio.sleep(0.5)

    print("--- main done")

asyncio.run(main())
