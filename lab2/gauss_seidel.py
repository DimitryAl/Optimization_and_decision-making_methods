from prettytable import PrettyTable
from funcs import *


def comp(x1:list[float], x2:list[float], eps:float) -> bool:
    ''' '''
    if abs(x1[0] - x2[0]) < eps:
        if abs(x1[1] - x2[1]) < eps:
            return True
    return False


def norm(x, y, eps):
    temp = ((y[0]-x[0])**2+(y[1]-x[1])**2)**(1/2)
    if temp < eps:
        return True
    else:
        return False

def gauss_seidel_opt(func, y:list[float], eps:float):
    ''' Метод Гаусса-Зейделя с одномерной оптимизацией '''
    print("Метод Гаусса-Зейделя с одномерной оптимизацией")
    n = 2
    d = [[1, 0], [0, 1]]
    y_old = y.copy()
    lmbd = [1, 1]
    j = 0
    table2 = PrettyTable()
    table2.field_names = ["k", "x", "f(x)", "j", "yi", "di", "lmbd"]
    table2.add_row([j, y.copy(), func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
    cnt = 0
    while True:
        if cnt >= 50:
            print(table2)
            break
        cnt+=1
        k = 0 # по какой координате шагаем
        while k <= n - 1:
            lmbd[k] = mint_new(func, -10, 10, eps, y.copy(), k)
            for i in range(n):
                y[i] = y[i] + lmbd[k] * d[k][i]
            k = k + 1 
        if comp(y, y_old, eps):
            table2.add_row([j+1, y_old, func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
            print(table2)
            break
        j = j + 1
        table2.add_row([j, y_old, func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
        y_old = y.copy()
    print(f"Найденный минимум: ({y[0]}, {y[1]})")
    print(f"Значение функции в минимуме: {func(y)}")
    return y, table2.get_string(), cnt


def lmbd_check(lmbd, y, d, k, func):
    temp = y.copy()
    cnt = 0
    while True:
        temp[k] = y[k] + lmbd * d[k][k]
        if func(temp) < func(y):
            return lmbd
        temp[k] = y[k] - lmbd * d[k][k]
        if func(temp) < func(y):
            return -lmbd
        lmbd /= 2
        cnt += 1
        if cnt > 20:
            break
    return 1
    

def gauss_seidel_disk(func, y:list[float], eps:float):
    ''' Метод Гаусса-Зейделя с дискретным шагом '''
    print("Метод Гаусса-Зейделя с дискретным шагом")
    n = 2
    d = [[1, 0], [0, 1]]
    y_old = y.copy()
    lmbd = [2, 2]
    j = 0
    table = PrettyTable()
    table.field_names = ["k", "x", "f(x)", "j", "yi", "di", "lmbd"]
    table.add_row([j, y.copy(), func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
    cnt = 0
    while True:
        #lmbd = [0.1, 0.1]
        if cnt >= 50:
            print(table)
            break
        cnt+=1
        lmbd[0] = lmbd_check(lmbd[0], y, d, 0, func)
        y[0] = y[0] + lmbd[0] * d[0][0]
        lmbd[1] = lmbd_check(lmbd[1], y, d, 1, func)
        y[1] = y[1] + lmbd[1] * d[1][1]
        #if norm(y, y_old, eps):
        if comp(y, y_old, eps):
            table.add_row([j+1, y_old, func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
            print(table)
            break
        j = j + 1
        table.add_row([j, y_old, func(y_old), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"], divider=True)
        y_old = y.copy()
    print(f"Найденный минимум: ({y[0]}, {y[1]})")
    print(f"Значение функции в минимуме: {func(y)}")
    return y, table.get_string(), cnt