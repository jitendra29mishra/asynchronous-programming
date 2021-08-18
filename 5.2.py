import asyncio
import datetime 

async def say_after(delay, what):
    for i in range(10):
        await asyncio.sleep(delay)
        print(f"{what} - {datetime.datetime.now().strftime('%H:%M:%S.%f')}")


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))

    print(f"started at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

    await task1
    await task2
    # for i in asyncio.Task.all_tasks():
    #     print(i)
    print(f"finished at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

asyncio.run(main())

