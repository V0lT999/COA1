import numpy as np


def strassen_method(matrix_a, matrix_b):

    def _get_matrix(matrix):
        x1 = np.array([[matrix[i][j] for j in range(n2)] for i in range(n2)])
        x2 = np.array([[matrix[i][j] for j in range(n2, n)] for i in range(n2)])
        x3 = np.array([[matrix[i][j] for j in range(n2)] for i in range(n2, n)])
        x4 = np.array([[matrix[i][j] for j in range(n2, n)] for i in range(n2, n)])

        return x1, x2, x3, x4

    ab = np.dot(matrix_a, matrix_b)

    n = len(matrix_a)
    n2 = n // 2

    if not n2 % 2:
        for i in range(n):
            matrix_a[i].append(0)
            matrix_b[i].append(0)
        row = [0 for i in range(n)]
        matrix_a.append(row)
        matrix_b.append(row)

    a1, a2, a3, a4 = _get_matrix(matrix_a)

    b1, b2, b3, b4 = _get_matrix(matrix_b)

    result = {
        'A11': str(a1),
        'A12': str(a2),
        'A21': str(a3),
        'A22': str(a4),
        'B11': str(b1),
        'B12': str(b2),
        'B21': str(b3),
        'B22': str(b4),
        'D0': ['(', str(a1), '+', str(a4), ')', '*', '(', str(b1), '+', str(b4), ')',
               '=', str(a1 + a4), '*', str(b1 + b4), '=', str((a1 + a4).dot(b1 + b4))],
        'D1': ['(', str(a2), '-', str(a4), ')', '*', '(', str(b3), '+', str(b4), ')',
               '=', str(a2 - a4), '*', str(b3 + b4), '=', str((a2 - a4).dot(b3 + b4))],
        'D2': ['(', str(a3), '-', str(a1), ')', '*', '(', str(b1), '+', str(b2), ')',
               '=', str(a3 - a1), '*', str(b1 + b2), '=', str((a3 - a1).dot(b1 + b2))],
        'D3': ['(', str(a1), '+', str(a2), ')', '*', str(b4),
               '=', str(a1 + a2), '*', str(b4), '=', str((a1 + a2).dot(b4))],
        'D4': [str(a1), '*', '(', str(b2), '-', str(b4), ')',
               '=', str(a1), '*', str(b2 - b4), '=', str(a1.dot(b2 - b4))],
        'D5': [str(a4), '*', '(', str(b3), '-', str(b1), ')',
               '=', str(a4), '*', str(b3 - b1), '=', str(a4.dot(b3 - b1))],
        'D6': ['(', str(a3), '+', str(a4), ')', '*', str(b1),
               '=', str(a3 + a4), '*', str(b1), '=', str((a3 + a4).dot(b1))],
        'result': str(ab)
    }

    return result
