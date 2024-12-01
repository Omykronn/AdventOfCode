def prepare(src: str) -> ([int], [int]):
    """
    Import data from a file, and format them
    """
    list1 = []
    list2 = []

    with open(src, 'r') as file:
        for line in file.readlines():
            n1, n2 = line.replace('\n', '').split("   ")

            list1.append(int(n1))
            list2.append(int(n2))

    return (list1, list2)

def solve(data: ([int], [int])) -> int:
    """
    Determine the flag of data
    """
    frequencies = {}
    flag = 0

    for n in data[1]:
        if n in frequencies:
            frequencies[n] += 1
        else:
            frequencies[n] = 1

    for n in data[0]:
        if n in frequencies:
            flag += n * frequencies[n]

    return flag
