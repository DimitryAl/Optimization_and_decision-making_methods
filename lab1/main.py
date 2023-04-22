from methods import *


def func1(x: float) -> float:
    global func1_cnt
    func1_cnt += 1
    return x**3/3 - 2*x**2 + 3*x + 5/3


def func2(x: float) -> float:
    global func2_cnt
    func2_cnt += 1
    return (x**2 - 2*x - 3) / (x**4 - 5*x**2 + 4)



# a, b = float(input('a: ')), float(input('b: '))
# eps = float(input('Введите eps: '))
# l = float(input('Введите l: '))
a = 2
b = 4
eps = 0.01
l = 0.1
func1_cnt = 0
func2_cnt = 0
# функция 1
#x_dich, res_dich, cnt_dich = Dichotomic_search(func1, a, b, eps, l, 'min')
#res_dich = Dichotomic_search(func2, a, b, eps, l, '')
##res_gold = Golden_search(func1, a, b, l, 'max')
res_fib = Fibonacci_search(func1, a, b, eps, l, '')
with open('dich_min_1.txt', 'w') as f_d,\
     open('gold_min_1.txt', 'w') as f_g,\
     open('fib_min_1.txt', 'w')  as f_b:

    #f_d.write(f'a = {a}, b = {b}, eps = {eps}, l = {l}\nx* = {res_dich[0]}; y* = {func1(res_dich[0])}\n'+res_dich[1] + f'\nfunction calls: {res_dich[2]}\n')
    ##f_g.write(f'a = {a}, b = {b}, l = {l}\nx* = {res_gold[0]}; y* = {func1(res_gold[0])}\n'+res_gold[1] + f'\nfunction calls: {res_gold[2]}\n')
    f_b.write(f'a = {a}, b = {b}, eps = {eps}, l = {l}\nx* = {res_fib[0]}; y* = {func1(res_fib[0])}\n'+res_fib[1] + f'\nfunction calls: {res_fib[2]}\n')
print(func1_cnt-1)
print(func2_cnt)

a = 0
b = 2
eps = 0.01
l = 0.1
func1_cnt = 0
func2_cnt = 0
# функция 2
#res_dich = Dichotomic_search(func2, a, b, eps, l, '')
##res_gold = Golden_search(func2, a, b, l, '')
res_fib = Fibonacci_search(func2, a, b, eps, l, '')
with open('dich_min_2.txt', 'w') as f_d,\
     open('gold_min_2.txt', 'w') as f_g,\
     open('fib_min_2.txt', 'w')  as f_b:

    #f_d.write(f'a = {a}, b = {b}, eps = {eps}, l = {l}\nx* = {res_dich[0]}; y* = {func1(res_dich[0])}\n'+res_dich[1] + f'\nfunction calls: {res_dich[2]}\n')
    ##f_g.write(f'a = {a}, b = {b}, eps = {eps}, l = {l}\nx* = {res_gold[0]}; y* = {func1(res_gold[0])}\n'+res_gold[1] + f'\nfunction calls: {res_gold[2]}\n')
    f_b.write(f'a = {a}, b = {b}, l = {l}\nx* = {res_fib[0]}; y* = {func1(res_fib[0])}\n'+res_fib[1] + f'\nfunction calls: {res_fib[2]}\n')

print(func1_cnt-1)
print(func2_cnt)

