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