import time
import socket
from datetime import datetime as dt

HOST = "localhost"
PORT = 8000


def get_today():
    return dt.today().strftime("%a, %d %b %Y %T")


def format_resp(data):
    ret = f"HTTP/1.0 200 OK\nDate: {get_today()}\nContent-Length: {len(data)}\nContent-type: text/plain; charset=utf-8"
    ret += f"\n\n\n{data}"
    return ret.encode()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, address = s.accept()
        with conn:
            print("Connected by", address)
            chunks = []
            while True:
                data = conn.recv(1024)
                print('-> ', data)
                if not data:
                    break
                time.sleep(1)
                conn.send(format_resp(data))
                break
