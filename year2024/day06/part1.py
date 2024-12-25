from toolbox.string import findCharacter
from year2024.day06.Guard import Guard

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '') for line in file.readlines()]

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    guard = Guard(findCharacter(data, '^')[0], (-1, 0))
    previous_positions = set()

    while 0 <= guard.position[0] < len(data) and 0 <= guard.position[1] < len(data[guard.position[1]]):
        previous_positions.add(guard.position)
        guard.next(data)

    return len(previous_positions) 
