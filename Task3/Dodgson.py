def dodgson_method(matrix):

    def _get_new_matrix(mtrx, deviders):
        n = len(mtrx)

        new_matrix = []

        for i in range(n - 1):
            row = []
            for j in range(n - 1):
                row.append(
                    (mtrx[i][j] * mtrx[i + 1][j + 1] - mtrx[i][j + 1] * mtrx[i + 1][j])
                    // deviders[i][j]
                )
            new_matrix.append(row)

        return new_matrix

    def _need_to_mix():
        new_matrix = [matrix[(i + 1) % len(matrix)] for i in range(len(matrix))]

        return new_matrix

    def process(mtrx) -> dict:
        result = {
            '1': mtrx,
        }

        counter = 2
        new_matrix = mtrx.copy()
        prev_matrix = mtrx.copy()

        while counter:
            n = len(prev_matrix)
            deviders = []

            if counter == 2:
                deviders = [[1 for j in range(n - 1)] for i in range(n - 1)]
            else:
                for i in range(1, n - 1):
                    row = []
                    for j in range(1, n - 1):
                        if prev_matrix[i][j] == 0:
                            return process(_need_to_mix())
                        row.append(prev_matrix[i][j])
                    deviders.append(row)

            prev_matrix = new_matrix
            new_matrix = _get_new_matrix(new_matrix, deviders)

            if len(new_matrix) == 1:
                result['result'] = new_matrix
                return result
            result[str(counter)] = new_matrix
            counter += 1

    result = process(matrix)

    result['count'] = len(result.keys()) - 1

    return result
