# # #!/usr/bin/env python3
# # # asyncq.py

# import asyncio
# import itertools as it
# import os
# import random
# import time

# async def makeitem(size: int = 5) -> str:
#     return os.urandom(size).hex()

# async def randsleep(caller=None) -> None:
#     i = random.randint(0, 10)
#     if caller:
#         print(f"{caller} sleeping for {i} seconds.")
#     await asyncio.sleep(i)

# async def produce(name: int, q: asyncio.Queue) -> None:
#     n = random.randint(0, 10)
#     for _ in it.repeat(None, n):  # Synchronous loop for each single producer
#         await randsleep(caller=f"Producer {name}")
#         i = await makeitem()
#         t = time.perf_counter()
#         await q.put((i, t))
#         print(f"Producer {name} added <{i}> to queue.")

# async def consume(name: int, q: asyncio.Queue) -> None:
#     while True:
#         await randsleep(caller=f"Consumer {name}")
#         i, t = await q.get()
#         now = time.perf_counter()
#         print(f"Consumer {name} got element <{i}>"
#               f" in {now-t:0.5f} seconds.")
#         q.task_done()

# async def main(nprod: int, ncon: int):
#     q = asyncio.Queue()
#     producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
#     consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
#     await asyncio.gather(*producers)
#     await q.join()  # Implicitly awaits consumers, too
#     for c in consumers:
#         c.cancel()

# if __name__ == "__main__":
#     asyncio.run(main(**ns.__dict__))
#     elapsed = time.perf_counter() - start
#     print(f"Program completed in {elapsed:0.5f} seconds.")


# """
# This gist shows how to run asyncio loop in a separate thread.
# It could be useful if you want to mix sync and async code together.
# Python 3.7+
# """
# # import asyncio
# # from datetime import datetime
# # from threading import Thread
# # from typing import Tuple, List, Iterable

# # import httpx

# # URLS = [
# #     "https://pypi.org",
# #     "https://python.org",
# #     "https://google.com",
# #     "https://amazon.com",
# #     "https://reddit.com",
# #     "https://stackoverflow.com",
# #     "https://ubuntu.com",
# #     "https://github.com",
# #     "https://microsoft.com",
# # ]


# # def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
# #     asyncio.set_event_loop(loop)
# #     loop.run_forever()


# # async def fetch(url: str) -> Tuple[str, int]:
# #     """Does HTTP get on url and returns url and status code"""
# #     async with httpx.AsyncClient() as session:
# #         response = await session.get(url)
# #         return url, response.status_code


# # async def fetch_all_urls(urls: Iterable[str]) -> List[Tuple[str, int]]:
# #     """Fetch all urls from the list of urls
# #     It is done concurrently and combined into a single coroutine"""
# #     tasks = [asyncio.create_task(fetch(url)) for url in urls]
# #     results = await asyncio.gather(*tasks)
# #     return results


# # def main() -> None:
# #     loop = asyncio.new_event_loop()
# #     t = Thread(target=start_background_loop, args=(loop,), daemon=True)
# #     t.start()

# #     start_time = datetime.now()

# #     task = asyncio.run_coroutine_threadsafe(fetch_all_urls(URLS), loop)
# #     for url, status_code in task.result():
# #         print(f"{url} -> {status_code}")

# #     exec_time = (datetime.now() - start_time).total_seconds()
# #     print(f"It took {exec_time:,.2f} seconds to run")
# #     loop.stop()


# # if __name__ == "__main__":
# #     main()


import asyncio, random
 
async def brother(yes=1):
    print(yes)
 
async def producer(queue):
    # produce a token and send it to a consumer
    await queue.put(brother)
 
async def consumer(queue):

    while True:
        brother = await queue.get()
        # process the token received from a producer
        await brother()
        queue.task_done()

async def main():
    queue = asyncio.Queue()
 
    print(queue)
    # fire up the both producers and consumers
    producers = asyncio.create_task(producer(queue))
    consumers = asyncio.create_task(consumer(queue))
 
    # with both producers and consumers running, wait for
    # the producers to finish
    await asyncio.gather(producers)
    # wait for the remaining tasks to be processed
    await queue.join()
 
    # cancel the consumers, which are now idle
    # for c in consumers:
    #     c.cancel()
 
asyncio.run(main())