from prettytable import PrettyTable

#from functions import *
#from func_test1 import *
from func_2 import *


table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "j", "yi", "di", "lmbd"]
table2 = PrettyTable()
table2.field_names = ["k", "x", "f(x)", "j", "yi", "di", "lmbd"]


# конец по норме
def gauss_seidel():
    n = 2
    eps = 0.01
    e = [[1, 0], [0, 1]]
    x = [10, 10]
    j = 0
    table.add_row([j, x.copy(), function(x), norm(gradient(x))])
    while True:
        k = 0 # по какой производной шагаем
        print(x)
        while k <= n - 1:
            grad = gradient(x)
            #print(f'grad = {grad}, norm = {norm(grad)}')
            if norm(grad) < eps:
                print(table)
                return
            else:
                t = mint(-10, 10, eps, x.copy()) # не до конца точно
                for i in range(n):
                    x[i] = x[i] - t * derivatives(x,k) * e[k][i]
                    #x[i] = x[i] - t * e[k][i]
                k = k + 1 
        j = j + 1
        table.add_row([j, x.copy(), function(x), norm(gradient(x))])


def comp(x1, x2, eps):
    if abs(x1[0] - x2[0]) < eps:
        if abs(x1[1] - x2[1]) < eps:
            return True
    return False


# конец по разности точек
def gauss_seidel2():
    n = 2
    eps = 0.1
    d = [[1, 0], [0, 1]]
    x = [5, 5]
    y = [5, 5]
    y_new = [0, 0]
    x_old = [0, 0]
    lmbd = [0, 0]
    j = 0
    table2.add_row([j, y.copy(), function(y), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"])
    cnt = 0
    while True:
        print(cnt)
        if cnt > 40:
            break
        cnt+=1
        k = 0 # по какой координате шагаем
        print(x)
        while k <= n - 1:
            lmbd[k] = mint_new(-10, 10, eps, x.copy(), y.copy(), k)
            #t = mint(-10, 10, eps, x.copy())
            for i in range(n):
                #x[i] = x[i] - t * derivatives(x,k) * e[k][i]
                y[i] = y[i] + lmbd[k] * d[k][i]
            k = k + 1 
        if comp(y, x_old, eps):
            table2.add_row([j+1, y.copy(), function(y), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"])
            print(table2)
            break
        x_old = y.copy()
        j = j + 1
        table2.add_row([j, y.copy(), function(y), "1\n2", f"{y[0]}\n{y[1]}", f"{d[0]}\n{d[1]}", f"{lmbd[0]}\n{lmbd[1]}"])


# без оптимизации
def gauss_seidel3():
    n = 2
    eps = 0.01
    e = [[1, 0], [0, 1]]
    x = [10, 10]
    x_old = [0,0]
    j = 0
    table2.add_row([j, x.copy(), function(x), norm(gradient(x))])
    while True:
        k = 0 # по какой производной шагаем
        print(x)
        while k <= n - 1:
            lmbd = 0.1
            for i in range(n):
                x[i] = x[i] - lmbd * derivatives(x,k) * e[k][i]
                #x[i] = x[i] + lmbd * e[k][i]
            k = k + 1 
        if comp(x, x_old, eps):
            print(table2)
            break
        x_old = x.copy()
        j = j + 1
        table2.add_row([j, x.copy(), function(x), norm(gradient(x))])