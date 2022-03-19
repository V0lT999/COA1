def karatsuba_method(a, b):

    def _get_coefs(x, y):
        str_x = str(x)
        str_y = str(y)
        n = int(len(str_x) if not len(str_x) % 2 else len(str_x) + 1)
        x1 = int(x // 10**(n/2))
        x2 = int(x % 10**(n/2))
        y1 = int(y // 10**(n/2))
        y2 = int(y % 10**(n/2))

        return x1, x2, y1, y2, n

    def _return_step(x, y):

        x1, x2, y1, y2, n = _get_coefs(x, y)

        result = f"{x} * {y} = ({x1} * 10^{n/2} + {x2})({y1} * 10^{n/2} + {y2})" \
                 f" = {x1} * {y1} * 10^{n} + ({x1 + x2} * {y1 + y2} - {x1} * {y1}" \
                 f" - {x2} * {y2}) * 10^{n/2} + {x2} * {y2} = " \
                 f"{x1*y1*10**n} + {int(((x1 + x2) * (y1 + y2) - x1 * y1 - x2 * y2) * 10**(n/2))}" \
                 f" + {x2 * y2} = {x * y}"

        return result

    a1, a2, b1, b2, n = _get_coefs(a, b)

    return {
        'result': _return_step(a, b),
        '1': _return_step(a1 + a2, b1 + b2),
        '2': _return_step(a2, b2)
    }
