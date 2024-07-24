from toolbox.AoCutils import findStart


def findSmallestCost(index: [[(int, int)]]) -> (int, int):
    """
    Returns the key of the smallest value in index
    """

    coor = None
    i = 0

    while coor is None and i < len(index):
        if len(index[i]) > 0:
            coor = index[i][0]

        i += 1

    return coor


def updatePosition(matrix: [str], i: int, j: int, distance_ref: int, distances: [[float]], distances_index: [[(int, int)]]) -> None:
    """
    Updates distances and distances_index
    """

    if i < len(matrix) and j < len(matrix[0]) and distances[i][j] > distance_ref + 1 and matrix[i][j] != '#':
        if distances[i][j] < float("inf"):
            distances_index[distances[i][j]].remove((i, j))  # If (i, j) was already explored and we find a smaller distance, we need to remove it

        distances[i][j] = distance_ref + 1
        distances_index[distances[i][j]].append((i, j))  # (i, j) is added according to its new distance


def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '') for line in file.readlines()]

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    max_steps = 64

    i, j = findStart(data)

    distances = [[float("inf") for _ in range(len(data[0]))] for _ in range(len(data))]

    # After being reached, each point is saved according to its distance (enable fast min for Djikstra Algorithm)
    # NB : distances_index is similar to a dictionnary indexed with integers
    distances_index = [[] for _ in range(max_steps + 1)] 

    distances[i][j] = 0
    distances_index[0] = [(i, j)]

    while distances[i][j] < max_steps:
        updatePosition(data, i + 1, j, distances[i][j], distances, distances_index)
        updatePosition(data, i - 1, j, distances[i][j], distances, distances_index)
        updatePosition(data, i, j + 1, distances[i][j], distances, distances_index)
        updatePosition(data, i, j - 1, distances[i][j], distances, distances_index)

        distances_index[distances[i][j]].remove((i, j))
        i, j = findSmallestCost(distances_index)

    counter = 0

    for line in distances:
        for nb in line:
            # The reachable points have a distance inferior to max_steps and the same parity (a step forward then backward is possible)
            if nb <= max_steps and nb % 2 == max_steps % 2:
                counter += 1

    return counter
