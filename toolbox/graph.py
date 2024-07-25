def djikstra(graph: dict, start: int, end: int) -> int:
    """
    Returns the cost of the smallest trail in graph from start to end
    """

    def minCostUnexplored(cost: {float}, unexplored: {bool}):
        """
        Returns the name of the unvisited edge with the lowest cost
        """

        key_min = None
        value_min = float('inf')

        for key in cost:
            if unexplored[key] and cost[key] < value_min:
                key_min = key
                value_min = cost[key]

        return key_min

    cost = {float('inf') for edge in graph}
    unexplored = {True for edge in graph}

    cost[start] = 0
    
    while (minEdge := minCostUnexplored(cost, unexplored)) is not None:
        for (neighbor, distance) in graph[minEdge]:
            if cost[neightbor] > cost[minEdge] + distance:
                cost[neightbor] = cost[minEdge] + distance

        unexplored[minEdge] = False

    return cost[end]


def longuestTrail(graph: dict, start, end, cost = 0, path = []) -> int:
    """
    Finds the longuest trail and its cost in graph from start to end
    """

    if start == end:
        return cost, path
    else:
        max_cost = 0
        max_path = []

        for neightbor, distance in graph[start]:
            if neightbor not in path:
                final_cost, final_path = longuestTrail(graph, neightbor, end, cost + distance, path + [start])

                if final_cost > max_cost:
                    max_cost = final_cost
                    max_path = final_path

        return max_cost, max_path


def compressUnoriented(graph: dict) -> None:
    """
    Compresses an unoriented graph by removing every node which are connected to only two others
    """

    to_compress = []

    for node in graph:
        if len(graph[node]) == 2:
            to_compress.append(node)

    for node in to_compress:
        neightborA, distanceA = graph[node][0]
        neightborB, distanceB = graph[node][1]

        graph[neightborA].append((neightborB, distanceA + distanceB))
        graph[neightborB].append((neightborA, distanceA + distanceB))

        graph[neightborA].remove((node, distanceA))
        graph[neightborB].remove((node, distanceB))

        del graph[node]
