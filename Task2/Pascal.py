def pascal(n, d):
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

    def _sum_step(step_number):
        step_result = []
        index = 0
        sum_step = 0
        while step_number > 0:
            sum_step += (step_number % 10) * power_residues[index]
            step_result.append(str(step_number % 10) + ' * ' + str(power_residues[index]))
            index += 1
            step_number = int(step_number / 10)

        result[f'{counter}'] = str.join(' + ', step_result) + " = " + str(sum_step)
        return sum_step

    while n > d and counter < 100:
        if n == _sum_step(n):
            break

        n = _sum_step(n)
        counter += 1

    if n == d or n == 0:
        result['result'] = True

    return result
