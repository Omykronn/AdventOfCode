def findHorizontalSymetry(matrix: [[int]]) -> int:
    i_reg = 0
    i = 0
    j = 1
    nb_smudge = 0

    while 0 <= i and j < len(matrix) :
        for k in range(len(matrix[0])):
            if matrix[i][k] != matrix[j][k]:
                nb_smudge += 1

        if nb_smudge <= 1:
            i += -1
            j += 1
        else:
            nb_smudge = 0
            i_reg += 1
            i = i_reg
            j = i + 1

        if nb_smudge == 1:
            if i == -1:
                return int((j - i) / 2)
            elif j == len(matrix):
                return len(matrix) - int((j - i) / 2)
        else:
            if i == -1 or j == len(matrix):
                nb_smudge = 0
                i_reg += 1
                i = i_reg
                j = i + 1

    return 0


def findVerticalSymetry(matrix: [[int]]) -> int:
    i_reg = 0
    i = 0
    j = 1
    nb_smudge = 0

    while 0 <= i and j < len(matrix[0]) :
        for k in range(len(matrix)):
            if matrix[k][i] != matrix[k][j]:
                nb_smudge += 1

        if nb_smudge <= 1:
            i += -1
            j += 1
        else:
            nb_smudge = 0
            i_reg += 1
            i = i_reg
            j = i + 1

        if nb_smudge == 1:
            if i == -1:
                return int((j - i) / 2)
            elif j == len(matrix[0]):
                return len(matrix[0]) - int((j - i) / 2)
        else:
            if i == -1 or j == len(matrix[0]):
                nb_smudge = 0
                i_reg += 1
                i = i_reg
                j = i + 1

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

