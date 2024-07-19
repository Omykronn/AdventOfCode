def evolv(intervals: [(int, int)], maps: (int, int, int)) -> ([(int, int)], [(int, int)]):
    """
    Keep track of which intervals are modified by maps because modified intervals should not be changed another map, but modified ones must.
    """

    modified_intervals = []
    unmodified_intervals = []

    for i in range(len(intervals)):
        # Both maps' endpoints are in intervals[i]
        if intervals[i][0] <= maps[1] < intervals[i][1] and intervals[i][0] <= maps[1] + maps[2] < intervals[i][1]:
            modified_intervals.append((maps[0], maps[0] + maps[2]))
            unmodified_intervals += [(intervals[i][0], maps[1]), (maps[1] + maps[2], intervals[i][1])]
        # Only maps' inferior endpoint is in intervals[i]
        elif intervals[i][0] < maps[1] < intervals[i][1]:  
            modified_intervals.append((maps[0], maps[0] + intervals[i][1] - maps[1]))
            unmodified_intervals.append((intervals[i][0], maps[1]))
        # Only maps' superior endpoint is in intervals[i]
        elif intervals[i][0] < maps[1] + maps[2] < intervals[i][1]:  
            modified_intervals.append((maps[0] + intervals[i][0] - maps[1], maps[0] + maps[2]))
            unmodified_intervals.append((maps[1] + maps[2], intervals[i][1]))
        # intervals[i] is inside maps
        elif maps[1] <= intervals[i][0] and intervals[i][1] <= maps[1] + maps[2]: 
            modified_intervals += [(maps[0] + intervals[i][0] - maps[1], maps[0] + intervals[i][1] - maps[1])]
        # The union of intervals[i] and maps is empty
        else: 
            unmodified_intervals.append(intervals[i])

    return modified_intervals, unmodified_intervals

def prepare(src: str) -> ([[(int, int, int)]], [int]):
    """
    Import data from a file, and format them
    """

    maps = [[]]

    with open(src, 'r') as file:
        seeds = [int(n) for n in file.readline().replace('\n', '').split(": ")[1].split(' ')]

        for line in file.readlines():
            if line[0].isdigit():
                maps[-1].append([int(n) for n in line.replace('\n', '').split(' ')])
            elif line == '\n':
                maps.append([])

    return maps, seeds

def solve(data: ([[(int, int, int)]], [int])) -> int:
    """
    Determine the flag of data
    """
    maps, seeds = data

    intervals_to_scan = [(seeds[2*k], seeds[2*k] + seeds[2*k+1]) for k in range(len(seeds) // 2)]  # Interval (a, b) is a the mathematical interger interval [a; b[        
    next_intervals = []  # Will contains intervals which were changed by a map in a section and must not be changed by another map of the section

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            intervals_done, intervals_to_scan = evolv(intervals_to_scan, maps[i][j])
            next_intervals += intervals_done

        # All intervals which weren't modified by a map are merged with modified one
        intervals_to_scan += next_intervals  
        next_intervals = []

    min_location = float("inf")

    for x, _ in intervals_to_scan:
        if x < min_location:
            min_location = x

    return min_location
