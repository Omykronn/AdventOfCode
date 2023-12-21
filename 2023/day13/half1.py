def find_horizontal_sym(matrix):
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


def find_vertical_sym(matrix):
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
