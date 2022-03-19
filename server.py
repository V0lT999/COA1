from flask import Flask
from flask import request

from Task1 import (
    Karatsuba
)
from Task3 import (
    Dodgson
)

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

    return Karatsuba.karatsuba_method(a, b)


@app.route('/dodgson')
def dogson():
    matrix = request.values.get('matrix')

    return Dodgson.dodgson_method(matrix)


if __name__ == "__main__":
    app.run()
