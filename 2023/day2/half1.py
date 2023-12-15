population_limit = {'r': 12, 'g': 13, 'b': 14}
sumup = 0

with open("2023/day2/input.txt", 'r') as src:
    k = 1

    for line in src.readlines():
        data = list(map(lambda s: list(map(lambda x: x.split(' '), s.split(", "))), line.split(": ")[1].split('; ')))
        flag = True

        for hand in data:
            for cubes in hand:
                if int(cubes[0]) > population_limit[cubes[1][0]]:
                    flag = False
        if flag:
            sumup += k

        k += 1

print(sumup)
