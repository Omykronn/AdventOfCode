from toolbox.Vector import Vector


def run_configuration(matrix: [str], start: (int, int), direction: (int, int)) -> int:
    footprint = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    rays = [[Vector(start), Vector(direction)]]

    while len(rays) > 0:
        if 0 <= rays[-1][0][0] < len(matrix) and 0 <= rays[-1][0][1] < len(matrix) and rays[-1][1] not in footprint[rays[-1][0][0]][rays[-1][0][1]]:
            footprint[rays[-1][0][0]][rays[-1][0][1]].append(rays[-1][1])  # Save the direction to check later in it is not following the same path

            match matrix[rays[-1][0][0]][rays[-1][0][1]]:
                case '.':
                    rays[-1][0] = rays[-1][0] + rays[-1][1]

                case '|':
                    if rays[-1][1][0] == 0:
                        rays[-1][1] = Vector((1, 0))
                        rays[-1][0] = rays[-1][0] + rays[-1][1]

                        rays.append([rays[-1][0] + Vector((-1, 0)), Vector((-1, 0))])
                    else:
                        rays[-1][0] = rays[-1][0] + rays[-1][1]

                case '-':
                    if rays[-1][1][1] == 0:
                        rays[-1][1] = Vector((0, 1))
                        rays[-1][0] = rays[-1][0] + rays[-1][1]

                        rays.append([rays[-1][0] + Vector((0, -1)), Vector((0, -1))])
                    else:
                        rays[-1][0] = rays[-1][0] + rays[-1][1]

                case '/':
                    rays[-1][1] = Vector((-rays[-1][1][1], -rays[-1][1][0]))
                    rays[-1][0] = rays[-1][0] + rays[-1][1]

                case '\\':
                    rays[-1][1] = Vector((rays[-1][1][1], rays[-1][1][0]))
                    rays[-1][0] = rays[-1][0] + rays[-1][1]
        else:
            rays.pop()

    counter = 0

    for line in footprint:
        for liste in line:
            if len(liste) > 0:
                counter += 1

    return counter

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '') for line in file.readlines()]

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    max_value = 0

    for i in range(len(data)):
        # From Left Side
        energized_tiles = run_configuration(data, (i, 0), (0, 1))

        if energized_tiles > max_value:
            max_value = energized_tiles

        # From Right Side
        energized_tiles = run_configuration(data, (i, len(data[0]) - 1), (0, -1))

        if energized_tiles > max_value:
            max_value = energized_tiles

    for j in range(len(data[0])):
        # From Up Side
        energized_tiles = run_configuration(data, (0, j), (1, 0))

        if energized_tiles > max_value:
            max_value = energized_tiles

        # From Bottom Side
        energized_tiles = run_configuration(data, (len(data) - 1, j), (-1, 0))

        if energized_tiles > max_value:
            max_value = energized_tiles

    return max_value # Execution in less than 10 sec
