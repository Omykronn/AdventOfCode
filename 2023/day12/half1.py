def is_enough_slots(string, n: int):
    flag = n <= len(string)
    i = 0

    while flag and i < n:
        if string[i] == '.':
            flag = False

        i += 1

    return flag


def nb_arrangements(string, array, need_sep: bool = False):
    if len(array) == 0:
        if '#' in string: return 0
        else: return 1
    elif len(string) == 0:
        return 0
    elif string[0] == '.':
        return nb_arrangements(string[1:], array, False)
    elif string[0] == '#':
        if not need_sep and is_enough_slots(string, array[0]): return nb_arrangements(string[array[0]:], array[1:], True)
        else: return 0
    else:
        if not need_sep and is_enough_slots(string, array[0]): return nb_arrangements(string[array[0]:], array[1:], True) + nb_arrangements(string[1:], array, False)
        else: return nb_arrangements(string[1:], array, False)


k = 0

with open("2023/day12/input.txt") as src:
    line = src.readline()

    while len(line) != 0:
        data = line.replace('\n', '').split(' ')

        k += nb_arrangements(data[0], list(map(int, data[1].split(','))))

        line = src.readline()

print(k)

