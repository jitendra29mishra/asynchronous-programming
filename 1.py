import asyncio

async def main():
    print('Hello ....')
    await asyncio.sleep(3)
    print('....World')
    return "Return value"

ret = asyncio.run(main())

print("==>> ", ret)
