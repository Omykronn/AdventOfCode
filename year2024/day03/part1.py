from re import findall
from toolbox.string import readNextInt

def prepare(src: str) -> str:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.read()

    return data

def calculate(instruction: str) -> int:
    """
    Get the result of the instruction (supposed licit)
    """
    n1 = readNextInt(instruction, 4)
    
    if n1 > 99:
        offset = 3
    elif n1 > 9:
        offset = 2
    else:
        offset = 1

    n2 = readNextInt(instruction, 5 + offset)

    return n1 * n2


def solve(data: str) -> int:
    """
    Determine the flag of data
    """
    sum_ = 0

    for instruction in findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data):
        sum_ += calculate(instruction)

    return sum_
