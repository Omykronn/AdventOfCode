instructions = ""
nodes = {}

with open("2023/day8/input.txt") as src:
    data = src.readlines()
    instructions = data[0].replace('L', '0').replace('R', '1')[:-1]

    for line in data[2:]:
        nodes[line[:3]] = (line[7:10], line[12:15])

k = 0
i = 0
position = "AAA"

while position != "ZZZ":
    position = nodes[position][int(instructions[i])]

    k += 1
    i += 1

    if i == len(instructions):
        i = 0

print(k)
