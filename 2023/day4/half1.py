def score(ref_nb, nb):
    total = 0

    for n in nb:
        if n in ref_nb:
            if total == 0:
                total = 1
            else:
                total *= 2

    return total

sumup = 0

with open("2023/day4/input.txt", 'r') as src:
    for line in src.readlines():
        winning_numbers, my_numbers = map(lambda s: s.split(' '), line.replace('\n', '').replace("  ", ' ').split(": ")[1].split(" | "))
        sumup += score(winning_numbers, my_numbers)

print(sumup)
