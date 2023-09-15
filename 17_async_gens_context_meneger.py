import asyncio

from redis import asyncio as aioredis

from contextlib import contextmanager, asynccontextmanager


@contextmanager
def custom_open(filename: str, mode: str = "w"):
    file_obj = open(filename, mode)  # до yield декоратор использует как метод enter, а то что после exit
    yield file_obj
    file_obj.close()


#
# with custom_open("file.txt") as file:
#     file.write("hello world")
#
@asynccontextmanager
async def redis_connection():
    try:
        redis = await aioredis.from_url('redis://localhost')
        yield redis
    finally:
        await redis.close()


async def main():
    async with redis_connection() as redis:
        await redis.set("course", "asyncio")


asyncio.run(main())
