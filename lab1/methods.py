from prettytable import PrettyTable


def Dichotomic_search(func, a: float, b: float, eps: float, l: float) -> tuple[float, str]:
    """Dichotomic search method"""

    result = PrettyTable()
    result.field_names = ["k", "a(k)", "b(k)",
                          "lmbd(k)", "mu(k)",
                          "F(lmbd(k))", "F(mu(k))"
                          ]

    k = 1
    while b - a > l:

        lmbd = ((a + b) / 2) - eps
        mu = ((a + b) / 2) + eps

        func_lmbd = func(lmbd)
        func_mu = func(mu)

        result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

        if func_lmbd > func_mu:
            a = lmbd
        else:
            b = mu

        k += 1

    result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    return (a + b)/2, result.get_string()


def Golden_search(func, a: float, b: float, l: float) -> tuple[float, str]:
    """Golden-section search method"""

    result = PrettyTable()
    result.field_names = ["k", "a(k)", "b(k)",
                          "lmbd(k)", "mu(k)",
                          "F(lmbd(k))", "F(mu(k))"
                          ]

    alpha = (5 ** 0.5 + 1) / 2
    k = 1
    lmbd = a + (b - a)/(alpha + 1)
    mu = b - (b-a)/(alpha + 1)
    func_lmbd = func(lmbd)
    func_mu = func(mu)
    result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    while b - a > l:

        if func_lmbd > func_mu:
            a = lmbd
            lmbd = mu
            func_mu = func_lmbd
            mu = b - (b - a)/(alpha + 1)
            func_mu = func(mu)
        else:
            b = mu
            mu = lmbd
            func_mu = func_lmbd
            lmbd = a + (b - a)/(alpha + 1)
            func_lmbd = func(lmbd)
        k += 1
        result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    return (a + b)/2, result.get_string()


def Fibonacci_search(func, a: float, b: float, eps: float, l: float) -> tuple[float, str]:
    """Fibonacci search method"""

    result = PrettyTable()
    result.field_names = ["k", "a(k)", "b(k)",
                          "lmbd(k)", "mu(k)",
                          "F(lmbd(k))", "F(mu(k))"
                          ]

    fibs = [1, 1]
    n = 2
    while True:
        fib = fibs[n-1]+fibs[n-2]
        fibs.append(fib)
        if fib > (b - a)/l:
            break
        n += 1

    k = 1
    lmbd = a + fibs[n-2]/fibs[n]*(b-a)
    mu = a + fibs[n-1]/fibs[n]*(b-a)
    func_lmbd = func(lmbd)
    func_mu = func(mu)
    result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    while b - a > l:
        # первый шаг
        if func(lmbd) > func(mu):
            # второй шаг
            a = lmbd
            lmbd = mu
            mu = a + fibs[n-k-1]/fibs[n-k]*(b-a)
            if k == n - 2:
                # пятый шаг
                mu = lmbd + eps
                if func(lmbd) > func(mu):
                    a = lmbd
                else:
                    b = mu
                result.add_row([k+1, a, b, lmbd, mu, func_lmbd, func_mu])
                break
            else:
                func_mu = func(mu)
        else:
            # третий шаг
            b = mu
            mu = lmbd
            lmbd = a + fibs[n-k-2]/fibs[n-k]*(b-a)
            if k == n - 2:
                # 5 шаг
                mu = lmbd + eps
                if func(lmbd) > func(mu):
                    a = lmbd
                else:
                    b = mu
                result.add_row([k+1, a, b, lmbd, mu, func_lmbd, func_mu])
                break
            else:
                func_lmbd = func(lmbd)
        # 4 шаг
        k += 1
        result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    return (a + b)/2, result.get_string()
