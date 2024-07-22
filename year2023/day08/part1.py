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

    counter = 0
    i = 0
    position = "AAA"

    while position != "ZZZ":
        position = nodes[position][int(instructions[i])]

        counter += 1
        i += 1

        if i == len(instructions):
            i = 0

    return counter