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
    counter = 0

    for line in data:
        # Finds min value for each color of cube
        population = {'r': 0, 'g': 0, 'b': 0}

        for hand in line:
            for cubes in hand:
                if population[cubes[1][0]] < int(cubes[0]):
                    population[cubes[1][0]] = int(cubes[0])

        counter += population['r']*population['g']*population['b']

    return counter
