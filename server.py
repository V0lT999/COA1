from flask import Flask
from flask import request

import Task1.Karatsuba
from Task1 import *
import Task2.SecondRachinskogo
from Task2 import *
import Task2.FirstRachinskogo
from Task2 import *

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


@app.route('/second-rachinskogo')
def SecondRachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return Task2.SecondRachinskogo.second_rachinskogo(number, simple)


@app.route('/first-rachinskogo')
def first_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return Task2.FirstRachinskogo.first_rachinskogo(number, simple)


if __name__ == "__main__":
    app.run()
