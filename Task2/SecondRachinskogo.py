def second_rachinskogo(n, p):

    b = p % 10
    if b == 1:
        b = 9
    elif b == 9:
        b = 1

    q = int((p * b + 1) / 10)

    result = {'result': False, '1': f"q = (p * b + 1) / 10 = ({p} * {b} + 1) / 10 = {q}"}

    counter = 2
    current_number = n
    while n > p and counter < 100:
        k = n % 10
        m = int(n / 10)

        n = m + k * q
        result[f'{counter}'] = f"m = {m} k = {k}, {m} + {k}*{q} = {n}"
        if n >= current_number:
            break
            # По условию - нужно использовать другой метод, если n не уменьшается
        counter += 1
        current_number = n

    if n == p or n == 0:
        result['result'] = True

    result['count'] = len(result.keys()) - 1

    return result
