import threading
import asyncio

import datetime
import time


async def foo(sleep_time):
    print('foo - Current thread name: ', threading.currentThread().name)

    print(f'Start Await foo: {datetime.datetime.today()}')
    await asyncio.sleep(sleep_time)
    print(f'End Await foo: {datetime.datetime.today()}')


async def f1():
    print('f1 - Current thread name: ', threading.currentThread().name)

    print(f'Start Await f1: {datetime.datetime.today()}')
    await asyncio.sleep(5)
    print(f'End Await f1: {datetime.datetime.today()}')

async def f2():
    print('f2 - Current thread name: ', threading.currentThread().name)

    print(f'Start Await f2: {datetime.datetime.today()}')
    await asyncio.sleep(5)
    print(f'End Await f2: {datetime.datetime.today()}')


async def main():
    print('aync main - Current thread name: ', threading.currentThread().name)

    tk1 = asyncio.create_task(f1())
    tk2 = asyncio.create_task(f2())

    await tk1
    await tk2

def t():
    print('t - Current thread name: ', threading.currentThread().name)
    asyncio.run(main())

print(f'Create Thread: {datetime.datetime.today()}')
t = threading.Thread(target=t, name='Thread Async Testing', daemon=True)
print(f'Thread start: {datetime.datetime.today()}')
t.start()
print(f'Thread join: {datetime.datetime.today()}')
t.join()
