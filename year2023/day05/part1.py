class Map:
    def __init__(self) -> None:
        """
        Initialized as empty
        """

        self.interval_src = []
        self.interval_dst = []
        self.length = 0

    def append(self, start_src: int, start_dst: int, range_length: int) -> None:
        """
        Appends a new transformation
        """

        self.interval_src.append((start_src, start_src + range_length))
        self.interval_dst.append(start_dst)
        self.length += 1

    def correspondance(self, value: int) -> int:
        """
        Return the new value in function of the transfomation
        """

        for i in range(len(self.interval_src)):
            if self.interval_src[i][0] <= value < self.interval_src[i][1]:
                return self.interval_dst[i] + value - self.interval_src[i][0]

        return value

def prepare(src: str) -> ([Map], [int]):
    """
    Import data from a file, and format them
    """

    maps = [Map()]

    with open(src, 'r') as file:
        seeds = [int(n) for n in file.readline().replace('\n', '').split(": ")[1].split(' ')]

        for line in file.readlines():
            if line == '\n':
                maps.append(Map())
            elif line[0].isdigit():
                split_line = line.replace('\n', '').split(' ')
                maps[-1].append(int(split_line[1]), int(split_line[0]), int(split_line[2]))

    return maps, seeds

def solve(data: ([Map], [int])) -> int:
    """
    Determine the flag of data
    """

    maps, seeds = data
    min_location = float("inf")

    for i in seeds:
        for j in range(len(maps)):
            i = maps[j].correspondance(i)

        if min_location > i:
            min_location = i

    return min_location
