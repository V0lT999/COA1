def fourier_method(a: list, b: list):
    len_a = len(a)
    a = [0 for i in range(len(b)-1)] + a[::-1] + [0 for i in range(len(b)-1)]
    num = 0
    product = []
    result = {}
    for i in range(len_a+len(b)-1):
        sum = num
        for j in range(len(b)):
            sum += a[i+j] * b[j]
        product.append(str(sum % 10))
        num = sum // 10
        result[str(i+1)] = ''.join(product[::-1])
        if num > 0:
            result[str(i+1)] = ''.join([f'({num})', result[str(i+1)]])

    if num > 0:
        product.append(str(num))
    result['result'] = ''.join(product[::-1])
    result['count'] = str(len_a+len(b)-1)
    return result
