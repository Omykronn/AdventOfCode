def extrapolate(sequence):
    """
    One can prove (by recurrence) that 
        k = x_0 - x_1 + x_2 - x_3 + ... + (-1)^n * x_n
    where x_i is the first number of i-th sequence
    """

    k = sequence[0]
    i = 0

    while sequence != [0] * len(sequence):
        i += 1

        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        k += ((-1)**i) * sequence[0]

    return k


data = open("2023/day9/input.txt", 'r').readlines()
sumup = 0

for line in data:
    sumup += extrapolate(list(map(int, line.replace('\n', '').split(' '))))
    
print(sumup)
