def third_rachinskogo(n, p):
    counter = 1
    b = p % 10
    if b == 1:
        q = int((p * 9 + 1) / 10)
    elif b == 9:
        q = int((p + 1) / 10)
    else:
        q = int((p * b + 1) / 10)

    q = p - q

    a = int(p / 10)
    result = {'result': False}

    current_number = n
    while n > p and counter < 100:
        k = n % 10
        m = int(n / 10)

        n = m - k * q
        result[f'{counter}'] = f"{m} - {k}*{q} = {n}"
        if (n >= current_number):
            break
            # По условию - нужно использовать другой метод, если n не уменьшается
        counter += 1
        current_number = n

    if n == p or n == 0:
        result['result'] = True

    return result