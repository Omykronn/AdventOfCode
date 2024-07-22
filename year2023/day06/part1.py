from math import sqrt, ceil, floor
from re import sub

def margin(time, distance):
    """
    Solves the inequation t * (time - t) >= distance with t an integer to determine the number of way to beat the record
    """

    delta = time**2 - 4*distance

    if delta >= 0:
        x1, x2 = (time - sqrt(delta))/2, (time + sqrt(delta))/2
        int_x1, int_x2 = ceil(x1), floor(x2)
        distance = int_x2 - int_x1 + 1

        # If a root is an integer, then it doesn't beat the record so it should be exclude
        if x1 == int_x1:
            distance -= 1
        
        if x2 == int_x2:
            distance -= 1

        return distance
    else:
        return 0

def prepare(src: str) -> [[int]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[int(n) for n in sub(r' +', ' ', line).replace('\n', '').split(': ')[1].split(' ')] for line in file.readlines()]

    return data

def solve(data: [[int]]) -> int:
    """
    Determine the flag of data
    """

    product = 1

    for i in range(len(data[1])):
        product *= margin(data[0][i], data[1][i])

    return product
