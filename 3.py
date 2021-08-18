import asyncio
"""
Call Async function from sync function.
"""

async def run():
    """
    Asynchronous function return string
    """
    await asyncio.sleep(3)
    return 'Hello World'


def test():
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(run())
    return ret



if  __name__ == '__main__':
    print(test())
