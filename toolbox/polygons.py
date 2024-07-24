def isIn(point: (int, int), polygon: [(int, int)]) -> bool:
    """
    Tests if a point is inside a polygon
    """

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

def segmentIntercept(seg1: (int, int), seg2: (int, int)):
    """
    Checks if the union of segments seg1 and seg2 is not empty
    """

    return (seg2[0] <= seg1[1] and seg1[1] <= seg2[1]) or (seg1[0] <= seg2[1] and seg2[0] <= seg1[0]) or (seg1[0] <= seg2[0] and seg2[1] <= seg1[1]) or (seg2[0] <= seg1[0] and seg1[1] <= seg2[1])
