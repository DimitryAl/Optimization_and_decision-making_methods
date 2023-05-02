from funcs import function1, function2
from gauss_seidel import gauss_seidel_opt, gauss_seidel_disk

print("Введите начальную точку:", sep = '')
x1, x2 = float(input('x1 = ')), float(input("x2 = "))
eps = float(input('Введите eps: '))

# x1 = 10
# x2 = 5
# eps = 0.01

x_opt, table_opt = gauss_seidel_opt(function2, [x1, x2], eps)
x_disk, table_disk = gauss_seidel_disk(function2, [x1, x2], eps)

f = open('table_opt2.txt', 'w')
f.write(table_opt)
f.write(f"\n{x_opt[0]}, {x_opt[1]}\n")
f.write(str(function2(x_opt)))
f.close()
f = open('table_disk2.txt', 'w')
f.write(table_disk)
f.write(f"\n{x_disk[0]}, {x_disk[1]}\n")
f.write(str(function2(x_disk)))
f.close()

x_opt, table_opt = gauss_seidel_opt(function1, [x1, x2], eps)
x_disk, table_disk = gauss_seidel_disk(function1, [x1, x2], eps)

f = open('table_opt1.txt', 'w')
f.write(table_opt)
f.write(f"\n{x_opt[0]}, {x_opt[1]}\n")
f.write(str(function1(x_opt)))
f.close()
f = open('table_disk1.txt', 'w')
f.write(table_disk)
f.write(f"\n{x_disk[0]}, {x_disk[1]}\n")
f.write(str(function1(x_disk)))
f.close()