from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import socket
import time

selector = DefaultSelector()

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

    callback = lambda: connected(s, request)

    selector.register(s.fileno(), EVENT_WRITE, data=callback)
    selector.select()


def connected(s, request):
    selector.unregister(s.fileno())
    s.send(request.encode())

    chunks = []
    callback = lambda: readable(s, chunks)
    selector.register(s.fileno(), EVENT_READ, data=callback)


def readable(s, chunks):
    global n_tasks
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        callback = lambda: readable(s, chunks)
        selector.register(s.fileno(), EVENT_READ, data=callback)
    else:
        body = (b''.join(chunks)).decode()
        print(body.split("\n")[0])
        n_tasks -= 1


start = time.time()
for i in range(50):
    get('/foo')

while n_tasks:
    events = selector.select()
    for event, mask in events:
        cb = event.data
        cb()

calc = time.time() - start
print(f'took {calc:.1f} sec')
