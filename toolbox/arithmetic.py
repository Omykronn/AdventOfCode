def lcd(n_list: [int]) -> int:
    """
    Calculates the Least Common Multiple (lcd) by reckonning the integer factorization of each number and keeping the higher
    exponent for each prime number
    """

    factorization = {}
    k = 2

    while n_list != [1] * len(n_list):
        for i in range(len(n_list)):
            exp = 0

            while n_list[i] % k == 0:
                n_list[i] = n_list[i] // k
                exp += 1

            if exp != 0:
                if k in factorization:
                    if factorization[k] < exp:
                        factorization[k] = exp
                else:
                    factorization[k] = exp

        k += 1

    result = 1

    for prime in factorization:
        result *= prime ** factorization[prime]

    return result