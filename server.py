from flask import Flask
from flask import request

from Task1 import (
    Karatsuba
)
from Task2 import (
    FirstRachinskogo,
    SecondRachinskogo,
    ThirdRachinskogo,
    Pascal
)
from Task3 import (
    Dodgson
)
from Task4 import (
    Strassen
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


@app.route('/first-rachinskogo')
def first_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return FirstRachinskogo.first_rachinskogo(number, simple)


@app.route('/second-rachinskogo')
def second_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return SecondRachinskogo.second_rachinskogo(number, simple)


@app.route('/third-rachinskogo')
def third_rachinskogo():
    number = int(request.values.get('number'))
    simple = int(request.values.get('simple'))

    return ThirdRachinskogo.third_rachinskogo(number, simple)


@app.route('/pascal')
def pascal():
    number = int(request.values.get('number'))
    divider = int(request.values.get('divider'))

    return Pascal.pascal(number, divider)


@app.route('/strassen')
def strassen():
    matrix_a = request.values.get('matrix_a')
    matrix_b = request.values.get('matrix_b')

    return Strassen.strassen_method(matrix_a, matrix_b)


if __name__ == "__main__":
    app.run()
