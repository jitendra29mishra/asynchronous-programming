import time

count = 1
def f1():
    global count
    print(f'f1 {count}')
    count += 1
    yield f3(('f1', count), 2)
    count += 1
    print(f'f1 {count}')


def f2():
    global count
    print(f'f2 {count}')
    count += 1
    yield f3(('f2', count), 1)
    count += 1
    print(f'f2 {count}')


def f3(name, n):
    time.sleep(n)
    print(f'function {name}')


lst = [f1(), f2()]

while lst:
    try:
        func = lst.pop(0)
        next(func)
        lst.append(func)
    except Exception as ex:
        print(ex)
