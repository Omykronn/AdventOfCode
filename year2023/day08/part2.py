from toolbox.arithmetic import lcd


def prepare(src: str) -> (str, dict):
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        instructions = file.readline().replace('L', '0').replace('R', '1')[:-1]
        nodes = {line[:3]: (line[7:10], line[12:15]) for line in file.readlines()}

    return instructions, nodes

def solve(data: (str, dict)) -> int:
    """
    Determine the flag of data
    """

    instructions, nodes = data

    positions = []

    # Find all starting point (A-node)
    for key in nodes:
        if key[-1] == 'A':
            positions.append(key)

    # Calculates the length of each loop from a A-node to a Z-node (the Z-node send to the same A-node)
    hops = [0 for _ in positions]

    for j in range(len(positions)):
        k = 0
        i = 0

        while positions[j][-1] != 'Z':
            positions[j] = nodes[positions[j]][int(instructions[i])]

            k += 1
            i += 1

            if i == len(instructions):
                i = 0

        hops[j] = k

    # The number of steps is the Least Common Multiple of all lengthes

    return lcd(hops)
