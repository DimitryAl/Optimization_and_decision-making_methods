from methods import *

def func1(x: float) -> float:
    return 3*x - x**3 -1

def func2(x:float) -> float:
    return -3*x**2 + 7*x + 2

Dichotomic_search(func1, -3, 0, 0.01, 0.1)
Golden_search(func1, -3, 0, 0.01, 0.1)