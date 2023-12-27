import heapq


NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

data = list(map(lambda s: list(map(int, s.replace('\n', ''))), open("2023/day17/input.txt", 'r').readlines()))


def forward(position):
    if position[2] == NORTH:
        return (position[0] - 1, position[1], NORTH)
    if position[2] == SOUTH:
        return (position[0] + 1, position[1], SOUTH)
    if position[2] == EAST:
        return (position[0], position[1] + 1, EAST)
    if position[2] == WEST:
        return (position[0], position[1] - 1, WEST)


def turn_left(position):
    if position[2] == NORTH:
        return (position[0], position[1], WEST)
    if position[2] == SOUTH:
        return (position[0], position[1], EAST)
    if position[2] == EAST:
        return (position[0], position[1], NORTH)
    if position[2] == WEST:
        return (position[0], position[1], SOUTH)

def turn_right(position):
    if position[2] == NORTH:
        return (position[0], position[1], EAST)
    if position[2] == SOUTH:
        return (position[0], position[1], WEST)
    if position[2] == EAST:
        return (position[0], position[1], SOUTH)
    if position[2] == WEST:
        return (position[0], position[1], NORTH)

def is_legit(position):
    return 0 <= position[0] < len(data) and 0 <= position[1] < len(data[0])


queue = [(0, (0, 0, WEST)), (0, (0, 0, NORTH))]  # (Heat Loss, (Absciss, Ordinate, Orientation))
visited = set()

# Store heat loss for each coordinates and orientation to avoid following a path which already have a greater heat loss than another one
cost = [[[float("inf"), float("inf"), float("inf"), float("inf")] for _ in range(len(data[0]))] for _ in range(len(data))]

heapq.heapify(queue)
flag = True

while len(queue) and flag:
    heat_loss, position = heapq.heappop(queue)

    if position not in visited:
        visited.add(position)

        for new_position in [turn_left(position), turn_right(position)]:
            sum_heat_loss = heat_loss

            for _ in range(3):
                new_position = forward(new_position)

                if is_legit(new_position):
                    sum_heat_loss += data[new_position[0]][new_position[1]]

                    if sum_heat_loss < cost[new_position[0]][new_position[1]][new_position[2]]:
                        cost[new_position[0]][new_position[1]][new_position[2]] = sum_heat_loss
                        heapq.heappush(queue, (sum_heat_loss, new_position))
            

    if position[0] == len(data) - 1 and position[1] == len(data[0]) - 1:
        print(heat_loss)
        flag = False    
