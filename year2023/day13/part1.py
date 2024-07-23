def findHorizontalSymetry(matrix: [[int]]) -> int:
    i_reg = 0
    i = 0
    j = 1

    while 0 <= i and j < len(matrix) :
        flag = True

        for k in range(len(matrix[0])):
            if matrix[i][k] != matrix[j][k]:
                flag = False

        if flag:
            i += -1
            j += 1
        else:
            i_reg += 1
            i = i_reg
            j = i + 1

        if i == -1:
            return int((j - i) / 2)
        elif flag and j == len(matrix):
            return len(matrix) - int((j - i) / 2)

    return 0


def findVerticalSymetry(matrix: [[int]]) -> int:
    i_reg = 0
    i = 0
    j = 1

    while 0 <= i and j < len(matrix[0]) :
        flag = True

        for k in range(len(matrix)):
            if matrix[k][i] != matrix[k][j]:
                flag = False

        if flag:
            i += -1
            j += 1
        else:
            i_reg += 1
            i = i_reg
            j = i + 1

        if i == -1:
            return int((j - i) / 2)
        elif (flag and j == len(matrix[0])):
            return len(matrix[0]) - int((j - i) / 2)

    return 0 

def prepare(src: str) -> [[[int]]]:
    """
    Import data from a file, and format them
    """

    data = [[]]

    with open(src, 'r') as file:
        for line in file.readlines():
            if line == '\n':
                data.append([])
            else:
                data[-1].append(line.replace('\n', ''))

    return data

def solve(data: [[[int]]]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    for matrix in data:
        counter += findVerticalSymetry(matrix) + 100 * findHorizontalSymetry(matrix)

    return counter
