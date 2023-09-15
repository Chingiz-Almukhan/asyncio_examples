import asyncio


async def greet_t(timeout: int):
    await asyncio.sleep(timeout)
    return 'Hello World'


async def main_t():
    long_task = asyncio.create_task(greet_t(60))

    seconds = 0

    while not long_task.done():

        await asyncio.sleep(1)
        seconds += 1

        if seconds == 5:
            long_task.cancel()

        print("Time passed: ", seconds)
    try:
        await long_task
    except asyncio.CancelledError:
        print("The long task cancelled")


asyncio.run(main_t())
