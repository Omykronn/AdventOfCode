from toolbox.Vector import Vector
from toolbox.polygons import isIn


def prepare(src: str) -> [[str]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.split(' ') for line in file.readlines()]

    return data

def solve(data: [[str]]) -> int:
    """
    Determine the flag of data
    """

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
        
        if isIn(normal_vector + polygon[i], polygon):
            transformed_polygon.append(polygon[i] - normal_vector)
        else:
            transformed_polygon.append(polygon[i] + normal_vector)

    # Algebric Area calculation

    area = 0

    for i in range(N):
        if transformed_polygon[i][0] == transformed_polygon[(i + 1) % N][0]:
            area += transformed_polygon[i][0] * (transformed_polygon[(i + 1) % N][1] - transformed_polygon[i][1])

    return int(abs(area))
