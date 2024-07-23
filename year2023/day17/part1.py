import heapq


NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3


def forward(position: (int, int, int)) -> (int, int, int):
    """
    Returns positions after one step forward
    """

    if position[2] == NORTH:
        return (position[0] - 1, position[1], NORTH)
    if position[2] == SOUTH:
        return (position[0] + 1, position[1], SOUTH)
    if position[2] == EAST:
        return (position[0], position[1] + 1, EAST)
    if position[2] == WEST:
        return (position[0], position[1] - 1, WEST)


def turnLeft(position: (int, int, int)) -> (int, int, int):
    """
    Returns positions after turning left
    """

    if position[2] == NORTH:
        return (position[0], position[1], WEST)
    if position[2] == SOUTH:
        return (position[0], position[1], EAST)
    if position[2] == EAST:
        return (position[0], position[1], NORTH)
    if position[2] == WEST:
        return (position[0], position[1], SOUTH)

def turnRight(position: (int, int, int)) -> (int, int, int):
    """
    Returns positions after turning right
    """

    if position[2] == NORTH:
        return (position[0], position[1], EAST)
    if position[2] == SOUTH:
        return (position[0], position[1], WEST)
    if position[2] == EAST:
        return (position[0], position[1], SOUTH)
    if position[2] == WEST:
        return (position[0], position[1], NORTH)

def isLegit(position: (int, int, int), height: int, width: int) -> bool:
    """
    Check if position is in matrix
    """

    return 0 <= position[0] < height and 0 <= position[1] < width

def prepare(src: str) -> [[int]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[int(n) for n in line.replace('\n', '')] for line in file.readlines()]

    return data

def solve(data: [[int]]) -> int:
    """
    Determine the flag of data
    """

    queue = [(0, (0, 0, WEST)), (0, (0, 0, NORTH))]  # (Heat Loss, (Absciss, Ordinate, Orientation))
    visited = set()

    # Store heat loss for each coordinates and orientation to avoid following a path which already have a greater heat loss than another one
    cost = [[[float("inf"), float("inf"), float("inf"), float("inf")] for _ in range(len(data[0]))] for _ in range(len(data))]

    heapq.heapify(queue)

    while len(queue) > 0:
        heat_loss, position = heapq.heappop(queue)

        if position not in visited:
            visited.add(position)

            for new_position in [turnLeft(position), turnRight(position)]:
                sum_heat_loss = heat_loss

                for _ in range(3):
                    new_position = forward(new_position)

                    if isLegit(new_position, len(data), len(data[0])):
                        sum_heat_loss += data[new_position[0]][new_position[1]]

                        if sum_heat_loss < cost[new_position[0]][new_position[1]][new_position[2]]:
                            cost[new_position[0]][new_position[1]][new_position[2]] = sum_heat_loss
                            heapq.heappush(queue, (sum_heat_loss, new_position))
                

        if position[0] == len(data) - 1 and position[1] == len(data[0]) - 1:
            return heat_loss  
