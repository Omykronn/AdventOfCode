def lcd(n_list):
    """
    Calculate the Least Common Multiple (lcd) by reckonning the integer factorization of each number and keeping the higher
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
                

instructions = ""
nodes = {}

with open("2023/day8/input.txt") as src:
    data = src.readlines()
    instructions = data[0].replace('L', '0').replace('R', '1')[:-1]

    for line in data[2:]:
        nodes[line[:3]] = (line[7:10], line[12:15])


positions = []

for key in nodes:
    if key[-1] == 'A':
        positions.append(key)

hops = [0 for _ in positions]

for j in range(len(positions)):
    k = 0
    i = 0

    while positions[j][-1] != 'Z':
        positions[j] = nodes[positions[j]][int(instructions[i])]

        k += 1
        i += 1

        if i == len(instructions):
            i = 0

    hops[j] = k


print(lcd(hops))
