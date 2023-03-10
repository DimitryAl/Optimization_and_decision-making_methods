from prettytable import PrettyTable

result_files = {
    "Dichotomic_search": "dich.txt",
    "Golden_search": "golden_search.txt",
    "Fibonacci": "fib.txt"
}


def Dichotomic_search(func, a: float, b: float, eps: float, l: float) -> None:
    """Dichotomic search method"""
    
    result = PrettyTable()
    result.field_names = ["k","a(k)", "b(k)",
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
    f = open(result_files["Dichotomic_search"], 'w')
    f.write(result.get_string())
    f.write(f'\nx* = {(a + b)/2}')
    f.close()


def Golden_search(func, a: float, b: float, eps: float, l: float) -> None:
    """Golden-section search method"""

    alpha = (5 ** 0.5 - 1) / 2

    result = PrettyTable()
    result.field_names = ["k","a(k)", "b(k)",
                          "lmbd(k)", "mu(k)",
                          "F(lmbd(k))", "F(mu(k))"
                          ]
            
    k = 1
    lmbd = a + (1 - alpha) * (b - a)
    mu = a + alpha * (b - a)
    func_lmbd = func(lmbd)
    func_mu = func(mu)
    result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    while b - a > l:
        
        #result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])
        
        if func_lmbd > func_mu:
            a = lmbd
            lmbd = mu
            mu = a + alpha * (b - a)
            func_mu = func(mu)
            func_lmbd = func(lmbd)
        else:
            b = mu
            mu = lmbd
            lmbd = a + (1 - alpha) * (b - a)
            func_lmbd = func(lmbd)
            func_mu = func(mu)
        k += 1
        result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])
        
    result.add_row([k, a, b, lmbd, mu, func_lmbd, func_mu])

    f = open(result_files["Golden_search"], 'w')
    f.write(result.get_string())
    f.write(f'\nx* = {(a + b)/2}')
    f.close()

