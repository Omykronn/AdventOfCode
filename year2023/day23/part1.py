from toolbox.graph import longuestTrail


def prepare(src: str) -> (dict, int, int):
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [list(line.replace('\n', '')) for line in file.readlines()]

    graph = {}

    def addVertex(ptA, ptB, weight, sense):
        if sense != -1: # Direct sense OK
            if ptA in graph:
                graph[ptA].append((ptB, weight))
            else:
                graph[ptA] = [(ptB, weight)]

        if sense != 1: # Indirect sense OK
            if ptB in graph:
                graph[ptB].append((ptA, weight))
            else:
                graph[ptB] = [(ptA, weight)]

    # HORIZONTAL
    for i in range(len(data)):
        j_orig = -1
        sense = 0

        for j in range(len(data[0])):
            if j_orig == -1 and data[i][j] != '#':
                j_orig = j

            if j_orig != -1:
                if data[i][j] == ">":
                    sense = 1
                if data[i][j] == "<":
                    sense = -1

            # Check if forward is dead-end
            if j_orig != -1 and data[i][j] == '#':
                if j - j_orig > 1:  # Check if not length 1
                    addVertex((i, j_orig), (i, j - 1), j - j_orig - 1, sense)
                    sense = 0

                j_orig = -1

            # Check intersection
            if j_orig != -1 and j - j_orig > 1 and ((i > 0 and data[i - 1][j] != '#') or (i < len(data) - 1 and data[i + 1][j] != '#')):
                addVertex((i, j_orig), (i, j), j - j_orig, sense)
                sense = 0

                j_orig = j

        if j_orig != -1:
            addVertex((i, j_orig), (i, j), j - j_orig, sense)

    # VERTICAL
    for j in range(len(data[0])):
        i_orig = -1

        for i in range(len(data)):
            if i_orig == -1 and data[i][j] != '#':
                i_orig = i

            if i_orig != -1:
                if data[i][j] == "v":
                    sense = 1
                if data[i][j] == "^":
                    sense = -1

            # Check if forward is dead-end
            if i_orig != -1 and data[i][j] == '#':
                if i - i_orig > 1:
                    addVertex((i_orig, j), (i - 1, j), i - i_orig - 1, sense)  # Check if not length 1
                    sense = 0

                i_orig = -1

            # Check intersection
            if i_orig != -1 and i - i_orig > 1 and ((j > 0 and data[i][j - 1] != '#') or (j < len(data[0]) - 1 and data[i][j + 1] != '#')):
                addVertex((i_orig, j), (i, j), i - i_orig, sense)
                sense = 0

                i_orig = i

        if i_orig != -1:
            addVertex((i_orig, j), (i, j), i - i_orig, sense)

    return graph, len(data), len(data[0])


def solve(data: (dict, int, int)) -> int:
    """
    Determine the flag of data
    """
    
    graph, height, width = data

    return longuestTrail(graph, (0, 1), (height - 1, width - 2))[0]
