sym2moves = {'|': ((1,0), (-1,0)),
         '-': ((0,1), (0,-1)),
         'L': ((-1,0), (0, 1)),
         'J': ((0,-1), (-1, 0)),
         '7': ((0,-1), (1,0)),
         'F': ((1,0), (0,1)),
         '.': ()}


def sum_2D_tuples(a: (int, int), b: (int, int)) -> (int, int):
    return (a[0] + b[0], a[1] + b[1])


def find_start(matrix: [str], dim: int) -> [(int, int)]:
    i = 0
    j = 0

    while i < dim:
        j = 0
        
        while j < dim:
            if matrix[i][j] == 'S':
                return (i, j)

            j += 1

        i += 1


def sym2moves_from_start(matrix: [str], dim: int, i: int, j: int) -> (int, int):
    possible_sym2moves = []

    # North
    if i - 1 >= 0 and (1, 0) in sym2moves[matrix[i-1][j]]:
        possible_sym2moves.append((-1,0))
    
    # South
    if i + 1 < dim and (-1, 0) in sym2moves[matrix[i+1][j]]:
        possible_sym2moves.append((1,0))

    # West
    if j - 1 >= 0 and (0, 1) in sym2moves[matrix[i][j-1]]:
        possible_sym2moves.append((0,-1))
    
    # East
    if j + 1 < dim and (0, -1) in sym2moves[matrix[i][j+1]]:
        possible_sym2moves.append((0,1))

    return possible_sym2moves


data = list(map(lambda s: s.replace('\n', ''), open("2023/day10/input.txt", 'r')))
start = find_start(data, len(data))

moves = sym2moves_from_start(data, len(data), start[0], start[1])

locations = [sum_2D_tuples(moves[i], start) for i in range(2)]
k = 1

while locations[0] != locations[1]:
    for i in range(2):
        symbol = data[locations[i][0]][locations[i][1]]

        if sum_2D_tuples(sym2moves[symbol][0], moves[i]) == (0, 0):  # A null sum means a come back the previous position
            moves[i] = sym2moves[symbol][1]
        else:
            moves[i] = sym2moves[symbol][0]

        locations[i] = sum_2D_tuples(moves[i], locations[i])

    k += 1

print(k)
