import asyncio


class E:
    def show(self):
        return "Hello world"


class A:
    def __init__(self) -> None:
        self.a = 10

    def __ainit__(self, y) -> None:
        self.y = y

    async def func(self, x):
        return self.a + x

    async def funcclass(self):
        return E()

if True:
    def f(x):
        a = A()
        try:
            # a.func(x).send(None)
            a.funcclass().send(None) 
        except StopIteration as ex:
            return ex
        print('stop')

    aa = f(9)
    # print(aa.args)
    # print(aa.value)
    print(aa.value.show())
else:
    async def f(x):
        a = A()
        b = await a.func(x)
        print(b)
    asyncio.run(f(8))




# try:
#     print(b.send(None))
# except StopIteration as si:
#     print('Error: ', str(si))
# except StopAsyncIteration as sai:
#     print('Error: ', str(sai))

