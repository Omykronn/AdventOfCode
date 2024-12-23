def prepare(src: str) -> ({int: [int]}, {int: [int]}, [[int]]):
    """
    Import data from a file, and format them
    """

    before = {}  # For each number, which number must be before
    after = {}  # For each number, which number must be after
    updates = []

    with open(src, 'r') as file:
        line = file.readline().replace('\n', '')

        # Getting ordering rules
        while line != '':
            n, m = [int(x) for x in line.split('|')]
            
            if n in after:
                after[n].append(m)
            else:
                after[n] = [m]

            if m in before:
                before[m].append(n)
            else:
                before[m] = [n]

            line = file.readline().replace('\n', '')

        # Getting updates
        line = file.readline().replace('\n', '')

        while line != '':
            updates.append([int(x) for x in line.split(',')])
            line = file.readline().replace('\n', '')   

    return before, after, updates

def checkValidity(update: [int], before: {int: [int]}, after: {int: [int]}) -> bool:
    """
    Check the validity of update according to the before and after rules
    """

    flag = True
    i = 0

    while flag and i < len(update):
        j = 0

        while flag and j < len(update):
            if j < i and update[i] in after and update[j] in after[update[i]]:
                flag = False

            if i < j and update[i] in before and update[j] in before[update[i]]:
                flag = False

            j += 1

        i += 1

    return flag

def solve(data: ({int: [int]}, {int: [int]}, [[int]])) -> int:
    """
    Determine the flag of data
    """

    before, after, updates = data
    sum_ = 0

    for update in updates:
        if checkValidity(update, before, after):
            sum_ += update[len(update) // 2]

    return sum_
