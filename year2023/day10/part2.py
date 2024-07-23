from toolbox.AoCutils import findStart
from toolbox.Vector import Vector


sym2moves = {'|': (Vector((1,0)), Vector((-1,0))),
             '-': (Vector((0,1)), Vector((0,-1))),
             'L': (Vector((-1,0)), Vector((0, 1))),
             'J': (Vector((0,-1)), Vector((-1, 0))),
             '7': (Vector((0,-1)), Vector((1,0))),
             'F': (Vector((1,0)), Vector((0,1))),
             '.': ()}

def isIn(point: (int, int), polygon: [(int, int)]) -> bool:
    degree = len(polygon)
    even = False

    for i in range(degree):
        # If point is concerned by an non-horizontal edge
        if ((polygon[i][0] <= point[0] < polygon[(i + 1) % degree][0] or polygon[(i + 1) % degree][0] < point[0] <= polygon[i][0])
            and polygon[i][0] != polygon[(i + 1) % degree][0]): 
            if polygon[i][1] == polygon[(i + 1) % degree][1]:  # vertical edge
                y_intersec = polygon[i][1]
            else:
                y_intersec = (polygon[(i + 1) % degree][1] - polygon[i][1]) * (point[0] - polygon[i][0]) / (polygon[(i + 1) % degree][0] - polygon[i][0]) + polygon[i][1]

            if y_intersec < point[1]:
                even = not even
            elif y_intersec == point[1]:  # exactly on the edge
                return True
        # If point is on an horizontal edge
        elif ((polygon[i][1] <= point[1] < polygon[(i + 1) % degree][1] or polygon[(i + 1) % degree][1] < point[1] <= polygon[i][1])
              and polygon[i][0] == polygon[(i + 1) % degree][0] == point[0]):
              return True

        
    return even


def possibleMovesFromStart(matrix: [str], i: int, j: int) -> (int, int):
    possible_sym2moves = []

    # North
    if i - 1 >= 0 and (1, 0) in sym2moves[matrix[i-1][j]]:
        possible_sym2moves.append(Vector((-1,0)))
    
    # South
    if i + 1 < len(matrix) and (-1, 0) in sym2moves[matrix[i+1][j]]:
        possible_sym2moves.append(Vector((1,0)))

    # West
    if j - 1 >= 0 and (0, 1) in sym2moves[matrix[i][j-1]]:
        possible_sym2moves.append(Vector((0,-1)))
    
    # East
    if j + 1 < len(matrix[0]) and (0, -1) in sym2moves[matrix[i][j+1]]:
        possible_sym2moves.append(Vector((0,1)))

    return possible_sym2moves

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

    # Initialisiation of the movement from the start

    move = possibleMovesFromStart(data, start[0], start[1])
    location = move[0] + start

    polygon = []
    vertex_convexity = []  # To devide every vertexes in two categories, depending on their convexity
    perimeter = 1

    if move[0].dotProduct(move[1]) == 0:
        polygon.append(start)
        vertex_convexity.append(move[0].crossProduct(move[1])[2] > 0)

    move = move[0]

    # Exploring the loop, and saving it as a polynom

    while location != start:
        symbol = data[location[0]][location[1]]

        if sym2moves[symbol][0] + move == (0, 0):  # A null sum means a come back the previous position
            next_move = sym2moves[symbol][1]
        else:
            next_move = sym2moves[symbol][0]    

        if move.dotProduct(next_move) == 0:
            polygon.append(location)
            vertex_convexity.append(move.crossProduct(next_move)[2] > 0)

        location = next_move + location
        move = next_move
        perimeter += 1

    # Algebric Area calculation

    N = len(polygon)
    area = 0

    for i in range(N):
        if polygon[i][0] == polygon[(i + 1) % N][0]:
            area += polygon[i][0] * (polygon[(i + 1) % N][1] - polygon[i][1])  # Calculation of the raw algebric area

    area = abs(area) - perimeter / 2  # Each tile on an edge has a half of it in the loop, but this little area should not be counting. We do the same for the corner, a correction is applied later

    # Determination of convexity of each category

    normal_vector = (polygon[-1] - polygon[0]).normalize() + (polygon[1] - polygon[0]).normalize()

    if isIn(normal_vector, polygon):
        convexity_correction = 0.25
    else:
        convexity_correction = -0.25

    # Correction of the area because of the corners

    for i in range(N):
        if vertex_convexity[i] == vertex_convexity[1]:
            area += convexity_correction
        else:
            area -= convexity_correction

    return int(area)
