sumup = 0

with open("2023/day2/input.txt", 'r') as src:
    for line in src.readlines():
        data = list(map(lambda s: list(map(lambda x: x.split(' '), s.split(", "))), line.split(": ")[1].split('; ')))
        population = {'r': 0, 'g': 0, 'b': 0}

        for hand in data:
            for cubes in hand:
                if population[cubes[1][0]] < int(cubes[0]):
                    population[cubes[1][0]] = int(cubes[0])

        sumup += population['r']*population['g']*population['b']

print(sumup)
