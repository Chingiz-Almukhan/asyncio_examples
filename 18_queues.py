import asyncio
from random import randint


# first in first out
class C:
    white = "\033[0m"
    blue = "\033[94m"
    green = "\033[92m"


c = C()


async def producer(queue, name: int):
    timeout = randint(1, 5)
    await queue.put(timeout)
    print(f"{c.blue}Producer {name} put {timeout} to the queue, {queue}{c.white}")


async def consumer(queue, name: int):
    while True:
        timeout = await queue.get()
        await asyncio.sleep(timeout)
        print(f"{c.green}Consumer {name} ate {timeout}, {queue}{c.white}")
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=3)
    producers = []
    for i in range(12):
        task = asyncio.create_task(producer(queue, name=i))
        producers.append(task)

    consumers = [asyncio.create_task(consumer(queue, name=i)) for i in range(4)]

    await asyncio.gather(*producers)
    await queue.join()

    for c in consumers:
        c.cancel()


asyncio.run(main())
