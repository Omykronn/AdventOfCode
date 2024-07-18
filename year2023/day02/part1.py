def prepare(src: str) -> [[[(str, str)]]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[[tuple(cubes.split(' ')) for cubes in hand.split(', ')] for hand in line.replace('\n', '').split(': ')[1].split("; ")] for line in file.readlines()]

    return data

def solve(data: [[[(str, str)]]]) -> int:
    """
    Determine the flag of data
    """

    population_limit = {'r': 12, 'g': 13, 'b': 14}
    counter = 0
    k = 1

    for line in data:
        flag = True

        for hand in line:
            # Test each hand there is more cubes of one color than it could be possible
            for cubes in hand:
                if int(cubes[0]) > population_limit[cubes[1][0]]:
                    flag = False
        if flag:
            counter += k

        k += 1

    return counter
