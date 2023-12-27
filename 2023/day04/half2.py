def score(ref_nb, nb):
    total = 0

    for n in nb:
        total += n in ref_nb

    return total


nb_win = []

with open("2023/day4/input.txt", 'r') as src:
    for line in src.readlines():
        winning_numbers, my_numbers = map(lambda s: s.split(' '), line.replace('\n', '').replace("  ", ' ').split(": ")[1].split(" | "))
        nb_win.append(score(winning_numbers, my_numbers))
   
total = [1 for _ in range(len(nb_win))]

for i in range(len(nb_win)):
    for j in range(nb_win[i]):
        total[i + j + 1] += total[i]

print(sum(total))
