from math import sqrt


class Vector(tuple):
    def __add__(self, x):
        assert len(self) == len(x)

        return Vector(self[i] + x[i] for i in range(len(self)))

    def __sub__(self, x):
        assert len(self) == len(x)

        return Vector(self[i] - x[i] for i in range(len(self)))

    def __mul__(self, x):
        if type(x) is int or type(x) is float:
            return Vector(u * x for u in self)
        elif type(x) is Vector:
            assert len(self) == len(x)

            return Vector(self[i] * x[i] for i in range(len(self)))

    def __truediv__(self, x):
        if type(x) is int or type(x) is float:
            return Vector(u / x for u in self)
        elif type(x) is Vector:
            assert len(self) == len(x)

            return Vector(self[i] / x[i] for i in range(len(self)))

    def norm(self):
        return sqrt(sum([u**2 for u in self]))

    def normalize(self):
        return self / self.norm()

    def dot_product(self, x):
        assert len(self) == len(x)

        return sum([self[i] * x[i] for i in range(len(self))])


def is_in(point: (int, int), polygon: [(int, int)]) -> bool:
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


def z_cross_product(x, y):
    return x[0] * y[1] - x[1] * y [0]


def find_start(matrix: [str]) -> [(int, int)]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                return Vector((i, j))


sym2moves = {'|': (Vector((1,0)), Vector((-1,0))),
             '-': (Vector((0,1)), Vector((0,-1))),
             'L': (Vector((-1,0)), Vector((0, 1))),
             'J': (Vector((0,-1)), Vector((-1, 0))),
             '7': (Vector((0,-1)), Vector((1,0))),
             'F': (Vector((1,0)), Vector((0,1))),
             '.': ()}


def sym2moves_from_start(matrix: [str], i: int, j: int) -> (int, int):
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


data = list(map(lambda s: s.replace('\n', ''), open("2023/day10/input.txt", 'r')))
start = find_start(data)

# Initialisiation of the movement from the start

move = sym2moves_from_start(data, start[0], start[1])
location = move[0] + start

polygon = []
vertex_convexity = []  # To devide every vertexes in two categories, depending on their convexity
perimeter = 1

if move[0].dot_product(move[1]) == 0:
    polygon.append(start)
    vertex_convexity.append(z_cross_product(move[0], move[1]) > 0)

move = move[0]

# Exploring the loop, and saving it as a polynom

while location != start:
    symbol = data[location[0]][location[1]]

    if sym2moves[symbol][0] + move == (0, 0):  # A null sum means a come back the previous position
        next_move = sym2moves[symbol][1]
    else:
        next_move = sym2moves[symbol][0]    

    if move.dot_product(next_move) == 0:
        polygon.append(location)
        vertex_convexity.append(z_cross_product(move, next_move) > 0)

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

if is_in(normal_vector, polygon):
    convexity_correction = 0.25
else:
    convexity_correction = -0.25

# Correction of the area because of the corners

for i in range(N):
    if vertex_convexity[i] == vertex_convexity[1]:
        area += convexity_correction
    else:
        area -= convexity_correction

print(area)
