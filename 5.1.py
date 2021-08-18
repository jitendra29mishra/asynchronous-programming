import asyncio
import datetime 

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"{what} - {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
    return what * 3


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

    await task1
    await task2
    for i in asyncio.all_tasks():
        print(i)
    print(f"finished at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

asyncio.run(main())

