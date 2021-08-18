import socket
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()


class Future:
    def __init__(self):
        self.callback = []

    def resolve(self):
        for cb in self.callback:
            cb()


class Task:
    def __init__(self, gen):
        self.gen = gen
        self.step()

    def step(self):
        try:
            f = next(self.gen)
        except StopIteration:
            return
        f.callback.append(self.step)


n_tasks = 0


def get(path):
    global n_tasks
    n_tasks += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 8000))
    except BlockingIOError:
        pass

    request = f'GET {path} HTTP/1.0\r\n\r\n'

    f = Future()
    selector.register(s.fileno(), EVENT_WRITE, data=f)
    yield f

    selector.unregister(s.fileno())
    s.send(request.encode())

    chunks = []
    while True:
        f = Future()
        selector.register(s.fileno(), EVENT_READ, data=f)
        yield f
        selector.unregister(s.fileno())
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print('Url: ', path, '\r',  body)
            # print('Url: ', path, '\r',  body.split('\n')[0])
            n_tasks -= 1
            return


start = time.time()
Task(get('/foo/1'))
Task(get('/foo/2'))

while n_tasks:
    events = selector.select()
    for event, mask in events:
        fut = event.data
        fut.resolve()
print('Time: {0:.2f}'.format(time.time() - start))
