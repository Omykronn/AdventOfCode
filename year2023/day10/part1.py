from toolbox.Vector import Vector
from toolbox.AoCutils import findStart


sym2moves = {'|': (Vector((1,0)), Vector((-1,0))),
             '-': (Vector((0,1)), Vector((0,-1))),
             'L': (Vector((-1,0)), Vector((0, 1))),
             'J': (Vector((0,-1)), Vector((-1, 0))),
             '7': (Vector((0,-1)), Vector((1,0))),
             'F': (Vector((1,0)), Vector((0,1))),
             '.': ()}


def possibleMovesFromStart(matrix: [str], i: int, j: int) -> (int, int):
    possible_moves = []

    # North
    if i - 1 >= 0 and (1, 0) in sym2moves[matrix[i-1][j]]:
        possible_moves.append(Vector((-1,0)))

    # South
    if i + 1 < len(matrix) and (-1, 0) in sym2moves[matrix[i+1][j]]:
        possible_moves.append(Vector((1,0)))

    # West
    if j - 1 >= 0 and (0, 1) in sym2moves[matrix[i][j-1]]:
        possible_moves.append(Vector((0,-1)))
    
    # East
    if j + 1 < len(matrix[0]) and (0, -1) in sym2moves[matrix[i][j+1]]:
        possible_moves.append(Vector((0,1)))

    return possible_moves

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

    start = Vector(findStart(data))

    moves = possibleMovesFromStart(data, start[0], start[1])

    locations = [moves[i] + start for i in range(2)]
    counter = 1

    while locations[0] != locations[1]:
        for i in range(2):
            symbol = data[locations[i][0]][locations[i][1]]

            if sym2moves[symbol][0] + moves[i] == (0, 0):  # A null sum means a come back the previous position
                moves[i] = sym2moves[symbol][1]
            else:
                moves[i] = sym2moves[symbol][0]

            locations[i] = moves[i] + locations[i]

        counter += 1

    return counter
