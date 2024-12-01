from toolbox.sort import bubbleSort


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
    bubbleSort(data[0])
    bubbleSort(data[1])

    flag = 0

    for i in range(len(data[0])):
        flag += abs(data[0][i] - data[1][i])

    return flag
