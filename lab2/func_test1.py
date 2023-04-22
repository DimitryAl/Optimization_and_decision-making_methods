import math


def function(x):    # возвращает значение функции в точке
    res = -x[0]**2 - x[1]**2 + x[0]*x[1] - x[0] + 2*x[1]
    return res


def gradient(x):    # возвращает грандент функции в точке
    g1 = -2*x[0] + x[1] - 1
    g2 = -2*x[1] + x[0] + 2
    return [g1, g2]


def norm(p):    # возвращает значение нормы вектора
    n = 0
    for i in range(len(p)):
        #n += p[i]**2
        n += math.pow(p[i], 2)
    n = math.sqrt(n)
    return n


def g(x, alpha):
    '''  '''
    new_x = [0, 0]
    grad = gradient(x)
    for i in range(len(x)):
        new_x[i] = x[i] - alpha * grad[i]
    res = function(new_x)
    return res


def mint(a0, b0, eps, x):   # поиск минимального шага методом половинного деления
    # http://optimizaciya-sapr.narod.ru/bez_mnogomer/naiskpok2.html
    lk = 0
    mk = 0
    delta = 0.5*eps
    x_ = 0
    ak = a0
    bk = b0
    k = 1

    lk = (ak + bk - delta) / 2
    mk = (ak + bk + delta) / 2
    # lk = (ak + bk) / 2 - delta
    # mk = (ak + bk) / 2 + delta
    k += 1
    if g(x, lk) <= g(x, mk):
        bk = mk
    else:
        ak = lk

    while (bk - ak) >= eps:
        lk = (ak + bk - delta) / 2
        mk = (ak + bk + delta) / 2
        # lk = (ak + bk) / 2 - delta
        # mk = (ak + bk) / 2 + delta
        k += 1
        if g(x, lk) <= g(x, mk):
            bk = mk
        else:
            ak = lk
    x_ = (ak + bk) / 2
    return x_

def der1(x):    # Возвращает значение производной по x1
    return -2*x[0] + x[1] - 1


def der2(x):    # Возвращает значение производной по x2
    return -2*x[1] + x[0] + 2


def derivatives(x, k):
    derivative = {0: der1(x), 1: der2(x)}
    der = derivative[k]
    return der