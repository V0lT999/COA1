def lucas(n, d):
    power_residues = []
    result = {'result': False}

    number = n
    s = 1
    while number > 0:
        power_residues.append(s % d)
        number = int(number / 10)
        s *= 10

    result['1'] = ''
    for i, item in enumerate(power_residues):
        result['1'] += f"r{i} = {item} "

    counter = 2

    while n > d and counter < 100:
        b = n % 100
        a = n // 100
        n = power_residues[2] * a + b
        result[str(counter)] = f"a = {a} b = {b} r2 = {power_residues[2]}, {power_residues[2]} * {a} + {b} = {n}"
        if len(str(n)) <= len(str(d)):
            break
        counter += 1

    if n == d or n == 0:
        result['result'] = True

    result['count'] = len(result.keys()) - 1

    return result
