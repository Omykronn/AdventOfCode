def findDigits(s: str) -> int:
    """
    Finds the first and last digits in s, then returns their concatenation
    """
    first = 0
    last = 0

    for c in s:
        if 48 <= ord(c) <= 57:  # ASCCI codes for 0, 1, ..., 9
            last = int(c)

            if first == 0:
                first = int(c)

    return 10*first + last

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.readlines()

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """
    
    counter = 0

    for line in data:
        counter += findDigits(line)

    return counter
