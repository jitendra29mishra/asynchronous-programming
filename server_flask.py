import time
from flask import Flask


app = Flask(__name__)


@app.route("/foo/<num>")
def foo(num):
    time.sleep(1)
    return f"{num}" + ", ".join(["Hello world!"]*25)



app.run(host="127.0.0.1", port=8000)

