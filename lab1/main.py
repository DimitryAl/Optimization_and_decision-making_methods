from methods import *


def func1(x: float) -> float:
    return x**3/3 - 2*x**2 + 3*x + 5/3


def func2(x: float) -> float:
    return (x**2 - 2*x - 3) / (x**4 - 5*x**2 + 4)



a, b = float(input('a: ')), float(input('b: '))
eps = float(input('Введите eps: '))
l = float(input('Введите l: '))


# функция 1
x_dich, res_dich = Dichotomic_search(func1, a, b, eps, l)
x_gold, res_gold = Golden_search(func1, a, b, l)
x_fib, res_fib = Fibonacci_search(func1, a, b, eps, l)
with open('dich_min_1.txt', 'w') as f_d,\
     open('gold_min_1.txt', 'w') as f_g,\
     open('fib_min_1.txt', 'w')  as f_b:

    f_d.write(f'x* = {x_dich}\n'+res_dich)
    f_g.write(f'x* = {x_gold}\n'+res_gold)
    f_b.write(f'x* = {x_fib}\n'+res_fib)

# функция 2
x_dich, res_dich = Dichotomic_search(func2, a, b, eps, l)
x_gold, res_gold = Golden_search(func2, a, b, l)
x_fib, res_fib = Fibonacci_search(func2, a, b, eps, l)
with open('dich_min_2.txt', 'w') as f_d,\
     open('gold_min_2.txt', 'w') as f_g,\
     open('fib_min_2.txt', 'w')  as f_b:

    f_d.write(f'x* = {x_dich}\n'+res_dich)
    f_g.write(f'x* = {x_gold}\n'+res_gold)
    f_b.write(f'x* = {x_fib}\n'+res_fib)