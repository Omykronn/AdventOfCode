def correctDilatation(location: (int, int), empty_column: [(int, int)], empty_raws: [(int, int)]) -> (int, int):
    """
    Corrects positions because of dilatation
    """

    i = 0
    j = 0

    while j < len(empty_column) and empty_column[j] < location[1]: j += 1
    while i < len(empty_raws) and empty_raws[i] < location[0]: i += 1

    return (location[0] + i, location[1] + j)

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

    # Finding galaxies and empty columns and raws
    empty_column = []
    empty_raws = []
    galaxies = []

    for i in range(len(data)):
        flag_vertical = True
        flag_horizontal = True

        for j in range(len(data[i])):
            if data[i][j] == '#': 
                flag_horizontal = False
                galaxies.append((i, j))

            if data[j][i] == '#': 
                flag_vertical = False

        if flag_vertical: empty_column.append(i)
        if flag_horizontal: empty_raws.append(i)


    for i in range(len(galaxies)):
        galaxies[i] = correctDilatation(galaxies[i], empty_column, empty_raws)


    # Calculating shortest distance
    counter = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            # In these cases, one can prove that the distance of the shortest path is |x1 - x2| + |y1 + y2|
            counter += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

    return counter
