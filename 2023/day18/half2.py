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


data = list(map(lambda s: s.split(' '), open("2023/day18/input.txt", 'r').readlines()))
directions = {'0': Vector((0, 1)),
              '2': Vector((0, -1)),
              '3': Vector((-1, 0)),
              '1': Vector((1, 0))}

# Generation of the polygon

point = Vector((0, 0))
polygon = []

for info in data:
    polygon.append(point := point + directions[info[2][7]] * int(info[2][2:7], 16))

# Enlarge the polygon for simple area calculation

transformed_polygon = []
N = len(polygon)

for i in range(N):
    normal_vector = (polygon[(i - 1) % N] - polygon[i]).normalize() + (polygon[(i + 1) % N] - polygon[i]).normalize()
    normal_vector = normal_vector * (0.5 / abs(normal_vector[0]))
    
    if is_in(normal_vector + polygon[i], polygon):
        transformed_polygon.append(polygon[i] - normal_vector)
    else:
        transformed_polygon.append(polygon[i] + normal_vector)

# Algebric Area calculation

area = 0

for i in range(N):
    if transformed_polygon[i][0] == transformed_polygon[(i + 1) % N][0]:
        area += transformed_polygon[i][0] * (transformed_polygon[(i + 1) % N][1] - transformed_polygon[i][1])

print(int(abs(area)))
