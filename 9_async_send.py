count = 1
async def f1():
    global count
    print(f'f1 {count}')
    count += 1
    try:
        f3(('f1', count)).send(None)
    except Exception as ex:
        pass
    count += 1
    print(f'f1 {count}')


async def f2():
    global count
    print(f'f2 {count}')
    count += 1
    try:
        f3(('f2', count)).send(None)
    except Exception as ex:
        pass
    count += 1
    print(f'f2 {count}')


async def f3(name):
    print(f'function {name}')


lst = [f1(), f2()]

while lst:
    try:
        func = lst.pop(0)
        func.send(None)
        lst.append(func)
    except Exception as ex:
        pass




