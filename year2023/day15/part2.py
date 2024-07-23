def HashAlgorithm(string: str) -> int:
    """
    Executes HASH algorithm
    """

    current_value = 0

    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value

def findSpecialCharacter(string: str) -> int:
    """
    Returns index of = or -
    """

    i = 0

    while i < len(string) and string[i] != '=' and string[i] != '-':
        i += 1

    return i

def dash(n: int, label: str, boxes: [[str]]) -> None:
    """
    Performs dash operations
    """

    i = len(boxes[n]) - 1

    while i >= 0:
        if boxes[n][i][0] == label:
            boxes[n].pop(i)

        i -= 1

def equal(n: int, label: str, focal_length: int, boxes: [[str]]) -> None:
    """
    Performs equal operations
    """

    i = len(boxes[n]) - 1
    flag = True

    while i >= 0 and flag:
        if boxes[n][i][0] == label:
            boxes[n][i] = (label, focal_length)
            flag = False

        i -= 1

    if flag:
        boxes[n].append((label, focal_length))

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.readline().replace('\n', '').split(',')

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    boxes = [[] for _ in range(256)]
    counter = 0

    for word in data:
        i = findSpecialCharacter(word)

        if word[i] == '=':
            equal(HashAlgorithm(word[:i]), word[:i], int(word[i+1]), boxes)
        elif word[i] == '-':
            dash(HashAlgorithm(word[:i]), word[:i], boxes)

    for n in range(256):
        for i in range(len(boxes[n])):
            counter += (n + 1) * (i + 1) * boxes[n][i][1]

    return counter
