import asyncio

import aioredis


async def main():
    redis = aioredis.from_url("redis://localhost")
    await redis.publish("channel:1", "brbrbrb")


if __name__ == "__main__":
    asyncio.run(main())