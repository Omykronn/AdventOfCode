def find_digits(s: str):
    first = 0
    last = 0

    for c in s:
        if 48 <= ord(c) <= 57:
            last = int(c)

            if first == 0:
                first = int(c)

    return 10*first + last


sumup = 0

with open("day1/input.txt", 'r') as src:    
    for line in src.readlines():
        sumup += find_digits(line)

print(sumup)
