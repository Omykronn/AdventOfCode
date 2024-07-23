from toolbox.Vector import Vector


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
    footprint = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]

    rays = [[Vector((0,0)), Vector((0,1))]]  # Position / Direction

    while len(rays) > 0:
        if 0 <= rays[-1][0][0] < len(data) and 0 <= rays[-1][0][1] < len(data) and rays[-1][1] not in footprint[rays[-1][0][0]][rays[-1][0][1]]:
            footprint[rays[-1][0][0]][rays[-1][0][1]].append(rays[-1][1])  # Save the direction to check later in it is not following the same path

            match data[rays[-1][0][0]][rays[-1][0][1]]:
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
