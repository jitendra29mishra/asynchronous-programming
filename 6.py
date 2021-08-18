import asyncio
import datetime
import time

async def f1():
    print(f'f1 enter - {datetime.datetime.today()}')
    print(f'f1 await statement start - {datetime.datetime.today()}')
    await asyncio.sleep(5)
    print(f'f1 await statement end - {datetime.datetime.today()}')


async def f2():
    print(f'f2 enter - {datetime.datetime.today()}')
    print(f'f2 await statement start - {datetime.datetime.today()}')
    await asyncio.sleep(5)
    print(f'f2 await statement end - {datetime.datetime.today()}')

async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())

    print(f"started at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

    await task1
    await task2

    print(f"finished at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

asyncio.run(main())
