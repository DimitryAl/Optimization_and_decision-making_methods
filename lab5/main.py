import numpy as np
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
import math
from prettytable import PrettyTable

def coordinate_descent(F, x0, lbd_lhs, lbd_rhs, eps = 1e-3, max_iter=30):
    x = x0.copy()
    f = F(x)
    iter = 0
    prev_x = x.copy()

    while iter < max_iter:
        for i in range(len(x)):
            def f_i(alpha):
                x_new = x.copy()
                x_new[i] = alpha
                return F(x_new)
            res, *args = find_min_golden_ration(f_i, 1e-8, x[i] + lbd_lhs, x[i] + lbd_rhs)
            prev_x = x.copy()
            x[i] = res

        if np.linalg.norm(x - prev_x) < eps:
            break

        f = F(x)
        iter += 1

    return x, f, iter

def find_min_golden_ration(func, l, a_init, b_init, exes=None, is_max=False):
    F = (1 + math.sqrt(5)) / 2
    f = (3 - math.sqrt(5)) / 2
    a, b = a_init, b_init
    sign = -1 if is_max else 1
    lbd = a + (b - a) * f
    muy = b - (b - a) * f
    func_1_val = sign * func(lbd)
    func_2_val = sign * func(muy)
    func_calc_times = 2
    while (l <= abs(b - a)):
        func_calc_times += 1
        if (func_1_val > func_2_val):
            a = lbd
            lbd = muy
            muy = b - (b - a) * f
            func_1_val = func_2_val
            func_2_val = sign * func(muy)
        else:
            b = muy
            muy = lbd
            lbd = a + (b - a) * f
            func_2_val = func_1_val
            func_1_val = sign * func(lbd)

    return a, b, b - a, (a + b) / 2, func((a + b) / 2), func_calc_times

def f_1(x):
    return x[0]**2 + x[1]**2

def f_2(x):
    return (x[0] + 3 * x[1] + 3) / (2 * x[0] + x[1] + 6)

def g1(x):
    return -x[1] + 1

def g2(x):
    return 2 * x[0] + x[1] - 2

def g1_2(x):
    return 2 * x[0] + x[1] - 12

def g2_2(x):
    return -x[0] + 2 * x[1] - 4

def g3_2(x):
    return -x[0]

def g3_3(x):
    return -x[1]

def g0_1(x):
    return 0.2 * x[0] + x[1] - 2

def g0_2(x):
    return -x[1] + 1

def line_print():
    print()

def penalty_function_method(objective, constraints, x0, muy=10.0, beta=1.0, eps=1e-3, max_iter=10):

    def obj(x):
        penalty = sum([max(0, c(x)) for c in constraints])
        return objective(x) + muy * penalty
    
    table = PrettyTable()
    table.field_names = ["K", "mu", "X(k+1)=X(mu_k)", "F(Xk+1)", "alpha(X(mu_k))", "tetha(mu_k)", "mu_k_alpha"]

    for i in range(max_iter):
        res = coordinate_descent(obj, x0, -1, 1)
        penalty_func = sum([max(0, c(res[0])) for c in constraints])
        #print("{:2d} | {:>f} | {:>f}; {:>f} | {:>f} | {:>f} | {:>f} | {:>f}".format(i + 1, muy, res[0][0], res[0][1], objective(res[0]), penalty_func, obj(res[0]), penalty_func * muy))
        table.add_row(["{:.2f}".format(i+1), muy, "{:.10}".format(res[0][0])+";"+"{:.10}".format(res[0][1]), objective(res[0]), penalty_func, obj(res[0]), penalty_func * muy], divider=True)
        x0 = res[0]
        muy *= beta

        if np.sum([max(0, c(x0)) for c in constraints]) < eps:
            table.float_format= ".6"
            return x0, table
    
    table.float_format= ".6"
    return x0, table


if __name__ == '__main__':
    x0 = np.array([-10.0, -10.0])
    constraints = [g1, g2]

    res, table = penalty_function_method(f_1, constraints, x0)
    print(table.get_string())
    print("Оптимальный результат: ", res)