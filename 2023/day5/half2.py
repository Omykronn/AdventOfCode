# GENERAL PRINCIPLE
# 
# Instead of calculating each value in each intervals (calculating time skyrocketing), I treat each interval with its endpoints. But the maps might not 
# respect the endpoints of an interval, so one interval might be divided in smaller intervals (but their union is still equal to the first interval).
# At the end, the smallest inferior endpoint is the answer.
#
# All of this is possible because the maps represent 1-slope linear function.


def evolv(intervals, maps):
    # We keep track of which intervals are modified by maps because modified intervals should not be changed another map, but modified ones must.

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


with open("day5/input.txt", 'r') as src:
    seeds = list(map(int, src.readline().replace('\n', '').split(": ")[1].split(' ')))
    intervals_to_scan = [(seeds[2*k], seeds[2*k] + seeds[2*k+1]) for k in range(len(seeds) // 2)]  # Interval (a, b) is a the mathematical interger interval [a; b[

    next_intervals = []  # Will contains intervals which were changed by a map in a section and must not be changed by another map of the section

    line = src.readline()

    while len(line) > 0:
        if line[0].isdigit():
            intervals_done, intervals_to_scan = evolv(intervals_to_scan, list(map(int, line.replace('\n', '').split(' '))))
            next_intervals += intervals_done
        elif line == '\n':  # Is True when line is the title of a section (e.g "humidity-to-location map:")
            intervals_to_scan += next_intervals  # All intervals which weren't modified my a map are merged with modified one
            next_intervals = []
            pass
            
        line = src.readline()

min_loc = float("inf")

for x, _ in intervals_to_scan:
    if x < min_loc:
        min_loc = x

print(min_loc)
