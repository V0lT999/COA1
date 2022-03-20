
# Сокращенное умножение
def abbreviated_multiplication(a, b):
    work_a = str(a).rjust(len(str(b)), '0')
    work_b = str(b).rjust(len(str(a)), '0')

    res_list = [work_a, work_b]

    calc_list = _full_rows_calculation(work_a, work_b)
    calc_list.append(__total(calc_list, len(work_a)))
    res_list.extend(calc_list)

    return __format_res(res_list)

def _full_rows_calculation(a, b):
    res_list = []
    for iter in range(len(a)):
        res_list.append(__single_row_calculation(a, b, iter))
    return res_list

def __single_row_calculation(a, b, iter):
    res = ""
    for i in range(len(a) - iter):
        res += str(int(a[i]) * int(b[i + iter]) + bool(iter) * int(a[i + iter]) * int(b[i])).rjust(2, '0')
    return res

def __total(list_row, number_len):
    multi_res = 0
    max_row_len = 2 * number_len
    for row in list_row:
        multi_res += int(row.ljust(max_row_len, '0'))
        max_row_len -= 1
    return str(multi_res)

def __format_res(res):
    result = {}
    max_len = len(max(res, key=len))
    for i, row in enumerate(res, start=1):
        result[i] = f"{row.center(max_len, ' ')}"
    return result