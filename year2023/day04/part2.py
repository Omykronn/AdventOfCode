def score(ref_nbs: [int], nbs: [int]) -> int:
    """
    Returns the number of nbs' element in ref_nbs
    """
    total = 0

    for n in nbs:
        total += n in ref_nbs

    return total

def prepare(src: str) -> [[[int]]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[[int(n) for n in serie.split(' ')] for serie in line.replace('  ', ' ').split(': ')[1].replace('\n', '').split(' | ')] for line in file.readlines()]

    return data

def solve(data: [[[int]]]) -> int:
    """
    Determine the flag of data
    """

    nb_win = [score(winning_numbers, my_numbers) for winning_numbers, my_numbers in data]
       
    total = [1 for _ in range(len(nb_win))]

    for i in range(len(nb_win)):
        for j in range(nb_win[i]):
            total[i + j + 1] += total[i]

    return sum(total)
