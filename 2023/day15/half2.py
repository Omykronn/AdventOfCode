def HASH_algorithm(string: str):
    current_value = 0

    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


def find_special_char(string):
    i = 0

    while i < len(string) and string[i] != '=' and string[i] != '-':
        i += 1

    return i


def dash_operation(n, label):
    i = len(boxes[n]) - 1

    while i >= 0:
        if boxes[n][i][0] == label:
            boxes[n].pop(i)

        i -= 1


def equal_operation(n, label, focal_length):
    i = len(boxes[n]) - 1
    flag = True

    while i >= 0 and flag:
        if boxes[n][i][0] == label:
            boxes[n][i] = (label, focal_length)
            flag = False

        i -= 1

    if flag:
        boxes[n].append((label, focal_length))


boxes = [[] for _ in range(256)]

for word in open("2023/day15/input.txt", 'r').readline().replace('\n', '').split(','):
    i = find_special_char(word)

    if word[i] == '=':
        equal_operation(HASH_algorithm(word[:i]), word[:i], int(word[i+1]))
    elif word[i] == '-':
        dash_operation(HASH_algorithm(word[:i]), word[:i])


sum_ = 0

for n in range(256):
    for i in range(len(boxes[n])):
        sum_ += (n + 1) * (i + 1) * boxes[n][i][1]

print(sum_)
