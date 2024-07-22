def extrapolate(sequence: [int]) -> int: 
    """
    One can prove (by recurrence) that 
        k = x_0 - x_1 + x_2 - x_3 + ... + (-1)^n * x_n
    where x_i is the first number of i-th sequence
    """

    k = sequence[0]
    i = 0

    while sequence != [0] * len(sequence):
        i += 1

        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        k += ((-1)**i) * sequence[0]

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
