class Map:
    def __init__(self):
        self.interval_src = []
        self.interval_dst = []
        self.length = 0

    def append(self, start_src, start_dst, range_length):
        self.interval_src.append((start_src, start_src + range_length))
        self.interval_dst.append(start_dst)
        self.length += 1

    def correspondance(self, value):
        for i in range(len(self.interval_src)):
            if self.interval_src[i][0] <= value < self.interval_src[i][1]:
                return self.interval_dst[i] + value - self.interval_src[i][0]

        return value


maps = [Map() for _ in range(7)]

with open("day5/input.txt", 'r') as src:
    seeds = list(map(int, src.readline().replace('\n', '').split(": ")[1].split(' ')))

    line = src.readline()
    i = -1

    while len(line) > 0:
        if line == '\n':
            i += 1
        elif line[0].isdigit():
            converted_list = list(map(int, line.replace('\n', '').split(' ')))
            maps[i].append(converted_list[1], converted_list[0], converted_list[2])

        line = src.readline()

min_location = float("inf")

for i in seeds:
    for j in range(7):
        i = maps[j].correspondance(i)

    if min_location > i:
        min_location = i

print(min_location)
