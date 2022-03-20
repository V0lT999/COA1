from pprint import pprint

import numpy as np


def calc_det_2_by_2(matrix: np.ndarray):
    assert matrix.shape[0] == matrix.shape[1] == 2
    return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]


def change_columns(matrix_: np.ndarray):
    for i, elem in enumerate(matrix_[0, :]):
        if elem != 0:
            tmp = matrix_[:, i].copy()
            matrix_[:, i] = matrix_[:, 0]
            matrix_[:, 0] = tmp
            return


def chio_cond_method(matrix: list, result: dict, req_lvl: int, multiplayer: int = 1):
    matrix_ = np.array(matrix) if type(matrix) is list else matrix
    assert matrix_.shape[0] == matrix_.shape[1]
    if matrix_.shape[0] == 2:
        result['result'] = multiplayer * calc_det_2_by_2(matrix_)
        return result
    det_matrix = []
    n = matrix_.shape[0]
    if matrix_[0, 0] == 0:
        change_columns(matrix_)
        multiplayer *= -1

    # cant happend
    if matrix_[0, 0] == 0:
        # det have zero row
        result['result'] = 0
        return result

    for i in range(n - 1):
        row = []
        for j in range(n - 1):
            row.append(np.array([[matrix_[0, 0], matrix_[0, j + 1]], [matrix_[i + 1, 0], matrix_[i + 1, j + 1]]]))
        det_matrix.append(row)
    det_result = np.zeros(shape=(n - 1, n - 1))
    for i in range(det_result.shape[0]):
        for j in range(det_result.shape[0]):
            det_result[i, j] = calc_det_2_by_2(det_matrix[i][j])

    multiplayer = multiplayer * 1 / (matrix_[0, 0] ** (n - 2))
    # print(det_result)
    # str_det = np.array2string(, precision=1, separator=',', suppress_small=True)
    str_det = np.array_str(np.array(det_matrix), precision=1, suppress_small=True)
    result[str(req_lvl)] = f"1 / {matrix_[0, 0]} ** {(n - 2)} * {str_det}"
    return chio_cond_method(det_result, result, req_lvl + 1, multiplayer)


def main_chio_cond_method(matrix: list):
    res = chio_cond_method(matrix, {}, 1)
    res['count'] = len(res.keys()) - 1
    pprint(res)
    return res


def tests():
    for i in range(100000):
        matrix = np.round(np.random.rand(4, 4) * 100)
        matrix[0, 0] = 0
        matrix[1, 1] = 0
        matrix_list = matrix.tolist()
        result_ = main_chio_cond_method(matrix_list)
        result = result_['result']
        result_2 = np.round(np.linalg.det(matrix))
        print(result)
        print(result_2)
        assert round(result_2) == round(result), f"Should be {result}, but {result_2}"
        # print(result_3)


if __name__ == '__main__':
    matrix = [[0, 1, 3, 2], [3, 2, 4, 2], [0, 1, 2, 0], [1, 3, 2, 1]]
    # chio_cond_method(matrix, {}, 1)
    main_chio_cond_method(matrix)
    # tests()
