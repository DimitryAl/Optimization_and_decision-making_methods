from prettytable import PrettyTable


def Dichotomic_search(func, a: float, b: float, eps: float, l: float, extr: str) -> tuple[float, str, int]:
    """Dichotomic search method"""

    if l < 2 * eps: 
        return 0, 'None', 'None'
    
    result = PrettyTable()
    result.field_names = ["k", "a", "b",
                          "lmbd", "mu",
                          "F(lmbd)", "F(mu)"
                          ]
    cnt = 0  # Счетчик вызовов функций
    if extr == 'max':
        sign = -1
    else:
        sign = 1

    k = 1
    while b - a > l:
        lmbd = ((a + b) / 2) - eps
        mu = ((a + b) / 2) + eps

        func_lmbd = func(lmbd)
        func_mu = func(mu)
        if extr == 'max':
            func_lmbd = -func_lmbd
            func_mu = -func_mu
        cnt += 2

        result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

        if func_lmbd > func_mu:
            a = lmbd
        else:
            b = mu

        k += 1

    result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

    return (a + b)/2, result.get_string(), cnt


def Golden_search(func, a: float, b: float, l: float, extr: str) -> tuple[float, str]:
    """Golden-section search method"""

    result = PrettyTable()
    result.field_names = ["k", "a", "b",
                          "lmbd", "mu",
                          "F(lmbd)", "F(mu)"
                          ]
    cnt = 0  # Счетчик вызовов функций
    if extr == 'max':
        sign = -1
    else:
        sign = 1

    #alpha = (5 ** 0.5 + 1) / 2
    alpha = (5 ** 0.5 - 1) / 2
    k = 1
    #lmbd = a + (b - a)/(alpha + 1)
    #mu = b - (b-a)/(alpha + 1)
    lmbd = a + (1 - alpha) * (b - a)
    mu = a + alpha * (b - a)
    func_lmbd = func(lmbd)
    func_mu = func(mu)
    if extr == 'max':
        func_lmbd *= -1
        func_mu *= -1
    cnt += 2
    result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

    while b - a > l:

        if func_lmbd > func_mu:
            a = lmbd
            lmbd = mu
            func_lmbd = func_mu
            #mu = b - (b - a)/(alpha + 1)
            mu = a + alpha * (b - a)
            func_mu = func(mu)
            if extr == 'max':
                func_mu *= -1
            cnt += 1
        else:
            b = mu
            mu = lmbd
            func_mu = func_lmbd
            #lmbd = a + (b - a)/(alpha + 1)
            lmbd = a + (1 - alpha) * (b - a)
            func_lmbd = func(lmbd)
            if extr == 'max':
                func_lmbd *= -1
            cnt += 1
        k += 1
        result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

    return (a + b)/2, result.get_string(), cnt


def Fibonacci_search(func, a: float, b: float, eps: float, l: float, extr: str) -> tuple[float, str]:
    """Fibonacci search method"""

    result = PrettyTable()
    result.field_names = ["k", "a", "b",
                          "lmbd", "mu",
                          "F(lmbd)", "F(mu)"
                          ]
    cnt = 0 # Счетчик вызовов функций
    if extr == 'max':
        sign = -1
    else:
        sign = 1

    # Подсчет чисел Фибоначчи
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
    if extr == 'max':
        func_lmbd *= -1
        func_mu *= -1
    cnt += 2
    result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

    while b - a > l:
        # первый шаг
        if func_lmbd > func_mu:
            # второй шаг
            a = lmbd
            lmbd = mu
            mu = a + fibs[n-k-1]/fibs[n-k]*(b-a)
            if k == n - 2:
                # пятый шаг
                mu = lmbd + eps
                func_lmbd = func(lmbd)
                func_mu = func(mu)
                if extr == 'max':
                    func_lmbd *= -1
                    func_mu *= -1
                #if func(lmbd) > func(mu):
                if func_lmbd > func_mu:
                    a = lmbd
                else:
                    b = mu
                cnt += 2
                result.add_row([k+1, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])
                break
            else:
                func_mu = func(mu)
                func_lmbd = func(lmbd)
                if extr == 'max':
                    func_lmbd *= -1
                    func_mu *= -1
                cnt += 2
        else:
            # третий шаг
            b = mu
            mu = lmbd
            lmbd = a + fibs[n-k-2]/fibs[n-k]*(b-a)
            if k == n - 2:
                # 5 шаг
                mu = lmbd + eps
                func_lmbd = func(lmbd)
                func_mu = func(mu)
                if extr == 'max':
                    func_lmbd *= -1
                    func_mu *= -1
                #if func(lmbd) > func(mu):
                if func_lmbd > func_mu:
                    a = lmbd
                else:
                    b = mu
                cnt += 2
                result.add_row([k+1, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])
                break
            else:
                func_lmbd = func(lmbd)
                func_mu = func(mu)
                if extr == 'max':
                    func_lmbd *= -1
                    func_mu *= -1
                cnt += 2
        # 4 шаг
        k += 1
        result.add_row([k, a, b, lmbd, mu, sign*func_lmbd, sign*func_mu])

    return (a + b)/2, result.get_string(), cnt
