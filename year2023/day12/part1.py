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

def arrangements(string: str, array: (int), need_sep: bool = False) -> int:
    """
    Returns the number of possible answers given string and array
    """

    if len(array) == 0:
        if '#' in string: return 0
        else: return 1
    elif len(string) == 0:
        return 0
    elif string[0] == '.':
        return arrangements(string[1:], array, False)
    elif string[0] == '#':
        if not need_sep and isEnoughSlots(string, array[0]): return arrangements(string[array[0]:], array[1:], True)
        else: return 0
    else:
        if not need_sep and isEnoughSlots(string, array[0]): return arrangements(string[array[0]:], array[1:], True) + arrangements(string[1:], array, False)
        else: return arrangements(string[1:], array, False)

def prepare(src: str) -> [[str, (int)]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '').split(' ') for line in file.readlines()]

    for i in range(len(data)):
        data[i][1] = [int(n) for n in data[i][1].split(',')]

    return data

def solve(data: [[str, (int)]]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    for string, numbers in data:
        counter += arrangements(string, numbers)

    return counter

