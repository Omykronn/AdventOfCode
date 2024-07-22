def extrapolate(sequence: [int]) -> int:
    """
    Executes the process described in the challenge
    """
    k = sequence[-1]

    while sequence != [0] * len(sequence):
        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        k += sequence[-1]

    return k

def prepare(src: str) -> [[int]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[int(n) for n in line.replace('\n', '').split()] for line in file.readlines()]

    return data

def solve(data: [[int]]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    for serie in data:
        counter += extrapolate(serie)

    return counter
