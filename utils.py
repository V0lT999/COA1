import numpy as np


def get_matrix(request):
    matrix = request.values.get('matrix').split(',')
    matrix = [int(i) for i in matrix]
    size = int(request.values.get('size'))
    matrix = np.asarray(matrix)
    matrix = matrix.reshape(size, size)
    matrix = matrix.tolist()

    return matrix