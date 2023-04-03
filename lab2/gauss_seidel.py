from prettytable import PrettyTable

from functions import gradient, norm, function
from functions import mint, derivatives



table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]

def gauss_seidel():
    n = 2
    eps = 0.01
    e = [[1, 0], [0, 1]]
    x = [0.5, 1]
    j = 0
    table.add_row([j, x.copy(), function(x), norm(gradient(x))])
    while True:
        k = 0
        print(x)
        while k <= n - 1:
            grad = gradient(x)
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