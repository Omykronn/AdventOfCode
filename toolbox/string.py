def readNextInt(string: str, i: int) -> int:
    """
    Read the next next integer from a position in a string 
    """
    n = 0

    while i < len(string) and string[i].isdigit():
        n = 10*n + int(string[i])
        i += 1

    return n

ALL_DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def findWordInDirections(word: str, matrix: [str], directions=ALL_DIRECTIONS) -> [(int, int)]:
    """ 
    Returns all positions of the beginning of the word in the matrix in the given directions
    """

    def testInOneDirection(word: str, matrix: [str], i, j, direction: (int, int)) -> bool:
        """
        Walks through the matrix from cell (i, j) in the given direction while the cells are the word
        """

        flag = True
        k = 0

        while flag and k < len(word) and 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
            flag = matrix[i][j] == word[k]

            i += direction[0]
            j += direction[1]
            k += 1

        if k < len(word) and (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i])):
            flag = False

        return flag

    coords = []

    # For each cell of matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # Test if it is the first character of word
            if matrix[i][j] == word[0]:

                # If yes, test all directions
                for direction in directions:
                    if testInOneDirection(word, matrix, i, j, direction):
                        coords.append((i, j))

    return coords

def findCharacter(matrix: [str], char: str) -> [(int, int)]:
    """
    Find a character in a 2D-matrix of string
    """

    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                positions.append((i,j))

    return positions
