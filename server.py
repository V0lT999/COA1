from flask import Flask
from flask import request

import Task1.Karatsuba
from Task1 import *
import Task2.FirstRachinskogo
from Task2 import *
import Task2.SecondRachinskogo
from Task2 import *
import Task2.ThirdRachinskogo
from Task2 import *
import Task2.Pascal
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


@app.route('/first-rachinskogo')
def first_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return Task2.FirstRachinskogo.first_rachinskogo(number, simple)


@app.route('/second-rachinskogo')
def second_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return Task2.SecondRachinskogo.second_rachinskogo(number, simple)


@app.route('/third-rachinskogo')
def third_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return Task2.ThirdRachinskogo.third_rachinskogo(number, simple)


@app.route('/pascal')
def pascal():
    number = int(request.values.get('number'))
    divider = int(request.values.get('divider'))

    return Task2.Pascal.pascal(number, divider)


if __name__ == "__main__":
    app.run()
