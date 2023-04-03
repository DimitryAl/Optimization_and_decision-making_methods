from prettytable import PrettyTable


def Rosenbrock_method(func, a: float, b: float, eps: float, l: float) -> tuple[float, str]:
    """Rosenbrock method"""

    result = PrettyTable()
    result.field_names = ["k", "X(k)\nF(X(k))", "j",
                          "y(j)\nF(y(i))", "Δ(j)",
                          "d(j)", "y(j) + Δ(j)d(j)\nF(y(j) + Δ(j)d(j))"
                          ]
        
    #https://www.cyberforum.ru/pascalabc/thread284906.html

    return result.get_string()
