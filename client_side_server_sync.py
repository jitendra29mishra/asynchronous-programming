import socket
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()

n_tasks = 0


def get(path):
    global n_tasks
    n_tasks += 1
    s = socket.socket()

    s.connect(('localhost', 8000))

    request = f'GET {path} HTTP/1.0\r\n\r\n'
    s.send(request.encode())

    chunks = []
    while True:
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(path, ': ',  body.split("\n")[0])
            n_tasks -= 1
            return


start = time.time()
for i in range(8):
    get(f'/foo/{i}')
print('Time: {0:.2f}'.format(time.time() - start))
