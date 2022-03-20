import numpy as np


def get_matrix(request):
    matrix = request.values.get('matrix').replace('[','').replace(']','').split(',')
    matrix = [int(i) for i in matrix]
    size = int(request.values.get('size'))
    matrix = np.asarray(matrix)
    matrix = matrix.reshape(size, size)
    matrix = matrix.tolist()

    return matrix


def get_two_matrix(request):
    matrix_a = request.values.get('matrix_a').replace('[','').replace(']','').split(',')
    matrix_a = [int(i) for i in matrix_a]
    size_a = int(request.values.get('size_a'))
    matrix_a = np.asarray(matrix_a)
    matrix_a = matrix_a.reshape(size_a, size_a)
    matrix_a = matrix_a.tolist()

    matrix_b = request.values.get('matrix_b').replace('[', '').replace(']', '').split(',')
    matrix_b = [int(i) for i in matrix_b]
    size_b = int(request.values.get('size_b'))
    matrix_b = np.asarray(matrix_b)
    matrix_b = matrix_b.reshape(size_b, size_b)
    matrix_b = matrix_b.tolist()

    return matrix_a, matrix_b