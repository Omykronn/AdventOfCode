def score(ref_nbs: [int], nbs: [int]) -> int:
    """
    Returns the score of card, given its winning numbers (ref_nbs) and the other numbers (nbs)
    """
    total = 0

    for n in nbs:
        if n in ref_nbs:
            if total == 0:
                total = 1
            else:
                total *= 2

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

    counter = 0

    for winning_numbers, my_numbers in data:
        counter += score(winning_numbers, my_numbers)

    return counter 
