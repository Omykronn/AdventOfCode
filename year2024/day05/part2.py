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

def sort(raw: [int], before: {int: [int]}, after: {int: [int]}) -> [(int, int)]:
    """
    Sort a list of page numbers according to the after and before rules
    """

    sorted_update = [0] * len(raw)

    # Looks for the right place of each page number in raw
    for k in range(len(raw)):
        flag = False
        i = -1

        # Tries each position until finding the right one
        while not flag and i < k:
            i += 1
            flag = True

            # For each already-placed number, checks if a rule forbidding the position exists
            for j in range(k):
                if ((j < i and raw[k] in after and sorted_update[j] in after[raw[k]]) or (i <= j and raw[k] in before and sorted_update[j] in before[raw[k]])):
                    flag = False

        # Moves the tail of sorted_update to add the new page number at its found position
        j = k

        while j > i:
            sorted_update[j] = sorted_update[j - 1]
            j -= 1

        # Adds the new page number at its found position
        sorted_update[i] = raw[k]

    return sorted_update 
    

def solve(data: ({int: [int]}, {int: [int]}, [[int]])) -> int:
    """
    Determine the flag of data
    """

    before, after, updates = data
    sum_ = 0

    for update in updates:
        new_update = sort(update, before, after)

        if new_update != update:
            sum_ += new_update[len(update) // 2]

    return sum_
