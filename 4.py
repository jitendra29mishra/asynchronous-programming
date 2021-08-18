import asyncio

async def main():
    print('Hello ....')
    await asyncio.sleep(3)
    print('....World')

    return 'I\'m return from async function call main'

print(asyncio.run(main()))
