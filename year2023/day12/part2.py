def isEnoughSlots(string: str, n: int) -> bool:
    """
    Checks if possible
    """

    flag = n <= len(string)
    i = 0

    while flag and i < n:
        if string[i] == '.':
            flag = False

        i += 1

    return flag

memo = {}

def arrangements(string: str, array: (int), need_sep: bool = False) -> int:
    if (string, array, need_sep) not in memo:
        if len(array) == 0:
            if '#' in string: memo[(string, array, need_sep)] = 0
            else: memo[(string, array, need_sep)] = 1
        elif len(string) == 0:
            memo[(string, array, need_sep)] = 0
        elif string[0] == '.':
            memo[(string, array, need_sep)] = arrangements(string[1:], array, False)
        elif string[0] == '#':
            if not need_sep and isEnoughSlots(string, array[0]): memo[(string, array, need_sep)] = arrangements(string[array[0]:], array[1:], True)
            else: memo[(string, array, need_sep)] = 0
        else:
            if not need_sep and isEnoughSlots(string, array[0]): memo[(string, array, need_sep)] = arrangements(string[array[0]:], array[1:], True) + arrangements(string[1:], array, False)
            else: memo[(string, array, need_sep)] = arrangements(string[1:], array, False)

    return memo[(string, array, need_sep)]

def prepare(src: str) -> [[str, [int]]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '').split(' ') for line in file.readlines()]

    for i in range(len(data)):
        data[i][0] = data[i][0] + ('?' + data[i][0]) * 4
        data[i][1] = tuple([int(n) for n in data[i][1].split(',')] * 5)

    return data

def solve(data: [[str, [int]]]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    for string, numbers in data:
        counter += arrangements(string, numbers)

    return counter
