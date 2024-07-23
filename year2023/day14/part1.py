def nextAbsciss(matrix: [str], i: int, j: int):
    k = i
    
    while k > 0 and matrix[k - 1][j] == '.':
        k -= 1
        
    return k

def prepare(src: str) -> [[str]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [list(line.replace('\n', '')) for line in file.readlines()]

    return data

def solve(data: [[str]]) -> int:
    """
    Determine the flag of data
    """
    counter = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':                        
                new_i = nextAbsciss(data, i, j)
                
                data[i][j] = '.'
                data[new_i][j] = 'O'
                
                counter += len(data) - new_i
                
    return counter