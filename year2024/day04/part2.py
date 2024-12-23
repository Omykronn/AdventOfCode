def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.read().split('\n')

    return data

def checkForXMas(i: int, j: int, matrix: [str]) -> bool:
    """
    Check for X-MAS pattern from cell (i, j) of matrix as the center of the X
    """
    flag = False

    if 1 <= i < len(matrix) - 1 and 1 <= j < len(matrix[i]):
        flag = matrix[i][j] == 'A'
        flag = flag and ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S') or (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M'))
        flag = flag and ((matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S') or (matrix[i+1][j-1] == 'S' and matrix[i-1][j+1] == 'M'))

    return flag

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """
    
    sum_ = 0

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[1]) - 1):
            if checkForXMas(i, j, data):
                sum_ += 1

    return sum_
