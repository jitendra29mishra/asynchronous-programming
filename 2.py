import asyncio
import time

async def a_wait(x):
    # time.sleep(x)
    await asyncio.sleep(x)
    return 'wait'

async def f1():
    print('1')
    await a_wait(3)
    print('2')
    await a_wait(3)
    print('3')
    await a_wait(3)
    print('4')


f = f1()

try:
    f.send(None)
except Exception as ex:
    print()
