from flask import Flask
from flask import request
from flask_cors import CORS

from Task1 import (
    Karatsuba
)
from Task2 import (
    FirstRachinskogo,
    SecondRachinskogo,
    ThirdRachinskogo,
    Pascal,
    Lucas
)
from Task3 import (
    Dodgson,
    Chio_Cond
)
from Task4 import (
    Strassen
)
from utils import get_matrix, get_two_matrix

app = Flask(__name__)
CORS(app)


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


@app.route('/dodgson', methods=['POST', 'GET'])
def dogson():
    matrix = get_matrix(request)

    return Dodgson.dodgson_method(matrix)


@app.route('/chio_cond', methods=['POST', 'GET'])
def chio_cond():
    matrix = get_matrix(request)
    return Chio_Cond.main_chio_cond_method(matrix)


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


@app.route('/lucas')
def lucas():
    number = int(request.values.get('number'))
    divider = int(request.values.get('divider'))

    return Lucas.lucas(number, divider)


@app.route('/strassen', methods=['POST', 'GET'])
def strassen():
    matrix_a, matrix_b = get_two_matrix(request)
    return Strassen.strassen_method(matrix_a, matrix_b)


if __name__ == "__main__":
    app.run()
