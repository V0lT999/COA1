def first_rachinskogo(n, p):
    b = p % 10
    a = int(p / 10)
    result = {'result': False, '1': f"a = {a} b = {b}"}

    counter = 2
    while n > p and counter < 100:
        k = n % 10
        m = int(n / 10)

        n = m * b - k * a
        result[f'{counter}'] = f"m = {m} k = {k}, {m}*{b} - {k}*{a} = {n}"
        counter += 1

    if n == p or n == 0:
        result['result'] = True

    result['count'] = len(result.keys()) - 1

    return result
