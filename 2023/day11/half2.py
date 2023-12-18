data = list(map(lambda s: s.replace('\n', ''), open("2023/day11/input.txt", 'r').readlines()))
dim = len(data)

# Finding galaxies and empty columns and raws
empty_column = []
empty_raws = []
galaxies = []

for i in range(dim):
    flag_vertical = True
    flag_horizontal = True

    for j in range(dim):
        if data[i][j] == '#': 
            flag_horizontal = False
            galaxies.append((i, j))

        if data[j][i] == '#': 
            flag_vertical = False

    if flag_vertical: empty_column.append(i)
    if flag_horizontal: empty_raws.append(i)

# Correcting positions because of dilatation
def correct_dilatation(location):
    i = 0
    j = 0

    while j < len(empty_column) and empty_column[j] < location[1]: j += 1
    while i < len(empty_raws) and empty_raws[i] < location[0]: i += 1

    return (location[0] + i * 999999, location[1] + j * 999999)


for i in range(len(galaxies)):
    galaxies[i] = correct_dilatation(galaxies[i])


# Calculating shortest distance
k = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        # In these cases, one can prove that the distance of the shortest path is |x1 - x2| + |y1 + y2|
        k += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(k)
