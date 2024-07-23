def findStart(matrix: [str], symbol: str = 'S') -> [(int, int)]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == symbol:
                return (i, j)