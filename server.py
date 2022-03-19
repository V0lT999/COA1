from flask import Flask
from flask import request

import Task1.Karatsuba
from Task1 import *

app = Flask(__name__)


@app.route('/')
def index():
    return app.make_response("OK")


@app.route('/karatsuba')
def karatsuba():
    a = int(request.values.get('a'))
    b = int(request.values.get('b'))

    if b > a:
        a, b = b, a

    return Task1.Karatsuba.karatsuba_method(a, b)


if __name__ == "__main__":
    app.run()
