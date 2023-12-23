def sum_2D_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])


data = list(map(lambda s: s.replace('\n', ''), open("2023/day16/input.txt")))
footprint = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]

rays = [[(0,0), (0,1)]]  # Position / Direction

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

print(sum_)
