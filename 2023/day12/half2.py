def is_enough_slots(string, n: int):
    flag = n <= len(string)
    i = 0

    while flag and i < n:
        if string[i] == '.':
            flag = False

        i += 1

    return flag

memo = {}

def solve(string, array: tuple, need_sep: bool = False):
    if (string, array, need_sep) not in memo:
        if len(array) == 0:
            if '#' in string: memo[(string, array, need_sep)] = 0
            else: memo[(string, array, need_sep)] = 1
        elif len(string) == 0:
            memo[(string, array, need_sep)] = 0
        elif string[0] == '.':
            memo[(string, array, need_sep)] = solve(string[1:], array, False)
        elif string[0] == '#':
            if not need_sep and is_enough_slots(string, array[0]): memo[(string, array, need_sep)] = solve(string[array[0]:], array[1:], True)
            else: memo[(string, array, need_sep)] = 0
        else:
            if not need_sep and is_enough_slots(string, array[0]): memo[(string, array, need_sep)] = solve(string[array[0]:], array[1:], True) + solve(string[1:], array, False)
            else: memo[(string, array, need_sep)] = solve(string[1:], array, False)

    return memo[(string, array, need_sep)]


i = 1
k = 0

with open("2023/day12/input.txt") as src:
    line = src.readline()

    while len(line) != 0:
        data = line.replace('\n', '').split(' ')
        data[0] = data[0] + ('?' + data[0]) * 4
        data[1] = tuple(map(int, data[1].split(','))) * 5

        print(i, end=' ')
        k += solve(data[0], data[1])
        print("DONE")

        line = src.readline()
        i += 1

print('\n', k)
