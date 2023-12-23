data = list(map(lambda s: s.replace('\n', ''), open("2023/day16/input.txt")))


def sum_2D_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])


def run_configuration(start, direction):
    footprint = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]

    rays = [[start, direction]]

    while len(rays) > 0:
        if 0 <= rays[-1][0][0] < len(data) and 0 <= rays[-1][0][1] < len(data) and rays[-1][1] not in footprint[rays[-1][0][0]][rays[-1][0][1]]:
            footprint[rays[-1][0][0]][rays[-1][0][1]].append(rays[-1][1])  # Save the direction to check later in it is not following the same path

            match data[rays[-1][0][0]][rays[-1][0][1]]:
                case '.':
                    rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                case '|':
                    if rays[-1][1][0] == 0:
                        rays[-1][1] = (1, 0)
                        rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                        rays.append([sum_2D_tuples(rays[-1][0], (-1, 0)), (-1, 0)])
                    else:
                        rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                case '-':
                    if rays[-1][1][1] == 0:
                        rays[-1][1] = (0, 1)
                        rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                        rays.append([sum_2D_tuples(rays[-1][0], (0, -1)), (0, -1)])
                    else:
                        rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                case '/':
                    rays[-1][1] = (-rays[-1][1][1], -rays[-1][1][0])
                    rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])

                case '\\':
                    rays[-1][1] = (rays[-1][1][1], rays[-1][1][0])
                    rays[-1][0] = sum_2D_tuples(rays[-1][0], rays[-1][1])
        else:
            rays.pop()

    sum_ = 0

    for line in footprint:
        for liste in line:
            if len(liste) > 0:
                sum_ += 1

    return sum_


max_ = 0

for i in range(len(data)):
    # From Left Side
    energized_tiles = run_configuration((i, 0), (0, 1))

    if energized_tiles > max_:
        max_ = energized_tiles

    # From Right Side
    energized_tiles = run_configuration((i, len(data[0]) - 1), (0, -1))

    if energized_tiles > max_:
        max_ = energized_tiles

for j in range(len(data[0])):
    # From Up Side
    energized_tiles = run_configuration((0, j), (1, 0))

    if energized_tiles > max_:
        max_ = energized_tiles

    # From Bottom Side
    energized_tiles = run_configuration((len(data) - 1, j), (-1, 0))

    if energized_tiles > max_:
        max_ = energized_tiles

print(max_)  # Execution in less than 10 sec
