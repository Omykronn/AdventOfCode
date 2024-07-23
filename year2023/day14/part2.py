def moveNorth(matrix: [[str]]) -> None:
    """
    Simulates the fall to north
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):            
            if matrix[i][j] == 'O':     
                k = i
                                                   
                while k > 0 and matrix[k - 1][j] == '.':
                    k -= 1
                
                matrix[i][j] = '.'
                matrix[k][j] = 'O'

        
def moveSouth(matrix: [[str]]) -> None:
    """
    Simulates the fall to south
    """

    for i in reversed(range(len(matrix))):
        for j in range(len(matrix[i])):            
            if matrix[i][j] == 'O':     
                k = i
                                                   
                while k < len(matrix) - 1 and matrix[k + 1][j] == '.':
                    k += 1
                
                matrix[i][j] = '.'
                matrix[k][j] = 'O'

def moveWest(matrix: [[str]]) -> None:
    """
    Simulates the fall to west
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):            
            if matrix[i][j] == 'O':     
                k = j
                                                   
                while k > 0 and matrix[i][k - 1] == '.':
                    k -= 1
                
                matrix[i][j] = '.'
                matrix[i][k] = 'O'
        
def moveEast(matrix: [[str]]) -> None:
    """
    Simulates the fall to east
    """

    for i in range(len(matrix)):
        for j in reversed(range(len(matrix[i]))):            
            if matrix[i][j] == 'O':     
                k = j
                                                   
                while k < len(matrix[0]) - 1 and matrix[i][k + 1] == '.':
                    k += 1
                
                matrix[i][j] = '.'
                matrix[i][k] = 'O'

def findCycleLength(sequ: [int]) -> int:
    """
    Finds length of cycle in a sequence of hashes
    """

    i = 0

    while i < len(sequ) and sequ[i] != sequ[-1]:
        i += 1
    
    return i

def getLoad(matrix: [[str]]) -> int:
    k = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O':
                k += len(matrix) - i

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
    sequence = []
    loads = [getLoad(data)]

    while findCycleLength(sequence) == len(sequence) - 1 or len(sequence) == 0:  # len(sequence) == 0 is necessary to start the loop
        moveNorth(data)
        moveWest(data)
        moveSouth(data)    
        moveEast(data)

        loads.append(getLoad(data))
        sequence.append(hash(tuple([tuple(line) for line in data])))

    # This uses the fact that the transformations lead to a cycle, which can be use to determine the state after 1,000,000,000 transformations without directly calculating it
    start = findCycleLength(sequence)
    length = len(sequence) - start - 1

    return loads[start + int((1e9 - start) % length)]
