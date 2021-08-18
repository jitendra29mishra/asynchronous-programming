import queue
import threading
import requests

_req_ch = queue.Queue()
_resp_ch = queue.Queue()





def network(host, port, endpoint, req):
    resp = requests.request("POST", url=f"http://{host}:{port}/{endpoint}", data=req)
    _resp_ch.put(resp.json())

def transfer



