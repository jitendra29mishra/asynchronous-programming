import asyncio

count = 1
async def f1():
    global count
    print(f'f1 start {count}')
    count += 1
    await f3(('f1', count), 2)
    count += 1
    print(f'f1 End {count}')


async def f2():
    global count
    print(f'f2 start {count}')
    count += 1
    await f3(('f2', count), 1)
    count += 1
    print(f'f2 End {count}')


async def f3(name, n):
    await asyncio.sleep(n)
    print(f'function {name}')


async def main():
    await asyncio.gather(f1(), f2())

asyncio.run(main())


