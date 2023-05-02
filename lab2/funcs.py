def function1(x):    # возвращает значение функции 1 в точке
    res = -x[0]**2 - x[1]**2 + x[0]*x[1] - x[0] + 2*x[1]
    return res

def function2(x):    # возвращает значение функции 2 в точке
    res = (x[0] - x[1])**2 + (x[1] -2)**2
    return res


def new_x(x, k, y):
    new_x = [x[0], x[1]]
    new_x[k] += y
    return new_x

def mint_new(a0, b0, eps, y, d):   # поиск минимального шага методом половинного деления
    lk = 0
    mk = 0
    delta = 0.5*eps
    x_ = 0
    ak = a0
    bk = b0
    k = 1

    lk = (ak + bk) / 2 - delta
    mk = (ak + bk) / 2 + delta

    k += 1
    
    if function2(new_x(y, d, lk)) > function2(new_x(y, d, mk)):
        ak = lk
    else:
        bk = mk

    while (bk - ak) >= 0.01:
        if k > 100:
            break
        lk = (ak + bk) / 2 - delta
        mk = (ak + bk) / 2 + delta

        k += 1

        if function2(new_x(y, d, lk)) > function2(new_x(y, d, mk)):
            ak = lk
        else:
            bk = mk
    x_ = (ak + bk) / 2
    return x_
