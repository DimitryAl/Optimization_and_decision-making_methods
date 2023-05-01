from funcs import function1, function2
from gauss_seidel import gauss_seidel_opt, gauss_seidel_disk

# print("Введите начальную точку:", sep = '')
# x1, x2 = float(input('x1 = ')), float(input("x2 = "))
# eps = float(input('Введите eps: '))

x1 = 5
x2 = 5
eps = 0.01

gauss_seidel_opt(function2, [x1, x2], eps)
gauss_seidel_disk(function2, [x1, x2], eps)