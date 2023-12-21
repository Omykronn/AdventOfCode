def find_horizontal_sym(matrix):
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


def find_vertical_sym(matrix):
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

data = [[]]

with open('2023/day13/input.txt', 'r') as src:
    for line in src.readlines():
        if line == '\n':
            data.append([])
        else:
            data[-1].append(line.replace('\n', ''))

k = 0

for matrix in data:
    k += find_vertical_sym(matrix) + 100 * find_horizontal_sym(matrix)

print(k)
