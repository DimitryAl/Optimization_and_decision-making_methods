from funcs import function1, function2
from gauss_seidel import gauss_seidel_opt, gauss_seidel_disk


def file_write(f, func, eps, table, x, cnt):
    f.write(f"Константа различимости: {eps}\n")
    f.write(table)
    f.write(f"\nОптимальное значение аргумента x = ({x[0]}, {x[1]})\n")
    f.write("Минимум функции = " + str(func(x)))
    f.write(f"\nКоличество итераций = {cnt}")

# print("Введите начальную точку:", sep = '')
# x1, x2 = float(input('x1 = ')), float(input("x2 = "))
# eps = float(input('Введите eps: '))

x1 = 3
x2 = 2
eps = 0.1

x_opt, table_opt, cnt_opt = gauss_seidel_opt(function2, [x1, x2], eps)
x_disk, table_disk, cnt_disk = gauss_seidel_disk(function2, [x1, x2], eps)

f = open('table_opt2.txt', 'w')
file_write(f, function2, eps, table_opt, x_opt, cnt_opt)
f.close()

f = open('table_disk2.txt', 'w')
file_write(f, function2, eps, table_disk, x_disk, cnt_disk)

f.close()

x_opt, table_opt, cnt_opt = gauss_seidel_opt(function1, [x1, x2], eps)
x_disk, table_disk, cnt_disk = gauss_seidel_disk(function1, [x1, x2], eps)

f = open('table_opt1.txt', 'w')
file_write(f, function1, eps, table_opt, x_opt, cnt_opt)
f.close()

f = open('table_disk1.txt', 'w')
file_write(f, function1, eps, table_disk, x_disk, cnt_disk)

f.close()