def extrapolate(sequence):
    k = sequence[-1]

    while sequence != [0] * len(sequence):
        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        k += sequence[-1]

    return k


data = open("2023/day9/input.txt", 'r').readlines()
sumup = 0

for line in data:
    sumup += extrapolate(list(map(int, line.replace('\n', '').split(' '))))

print(sumup)
