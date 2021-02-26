from math import tan, pi
import random


def my_tan_fractions(n, eps):
    mic = 10 ** (-12)
    f = mic
    c = f
    d = 0
    j = 1
    while True:
        if j == 1:
            a = n
        else:
            a = -(n ** 2)
        b = 2 * j - 1
        d = b + a * d
        if d == 0:
            d = mic
        c = b + a / c
        if c == 0:
            c = mic
        d = 1 / d
        delta = c * d
        f *= delta
        j += 1
        if abs(delta - 1) < eps:
            break
    return f


def my_tan_poly(n):
    if n < 0:
        return -my_tan_poly(-n)
    if pi / 4 <= n < pi / 2:
        return 1 / my_tan_poly(pi / 2 - n)
    c1 = 0.33333333333333333
    c2 = 0.133333333333333333
    c3 = 0.053968253968254
    c4 = 0.0218694885361552
    return n + c1 * n ** 3 + c2 * n ** 5 + c3 * n ** 7 + c4 * n ** 9


def calc_tan_10000_runs():
    print("task 3")
    _eps = 10 ** (-16)

    fraction_err = 0
    poly_err = 0
    runs = 10_000
    for _ in range(runs):
        x = random.uniform(-pi / 2, pi / 2)
        fraction_err += abs(tan(x) - my_tan_fractions(x, _eps))
        poly_err += abs(tan(x) - my_tan_poly(x))
    return {'fracError': fraction_err, 'poliErr': poly_err, 'runs': runs}
    print(f'Eroarea medie prin metoda ractiilor continue: {fraction_err / runs}')
    print(f'Eroarea medie prin metoda polinoamelor: {poly_err / runs}')


def calc_tan_simple():
    print("task 3")
    _eps = 10 ** (-16)
    x = random.uniform(-pi / 2, pi / 2)
    return {'number': x, 'fracError': abs(tan(x) - my_tan_fractions(x, _eps)), 'poliErr': abs(tan(x) - my_tan_poly(x))}
