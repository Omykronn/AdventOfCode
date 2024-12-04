def prepare(src: str) -> [[int]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[int(n) for n in line.replace('\n', '').split(' ')] for line in file.readlines()]

    return data

def check(report: [int]):
    """
    Check a report's validity
    """

    i = 0
    direction = report[1] - report[0]
    flag = True

    while i < len(report) - 1 and flag:
        flag = (report[i + 1] - report[i]) * direction > 0 and abs(report[i + 1] - report[i]) <= 3
        # Two adjacent report differ of at least 1 is check by the first condition : if null, then the product is zero

        i += 1

    return flag
    


def solve(data: [[int]]) -> int:
    """
    Determine the flag of data
    """
    sum_ = 0

    for report in data:
        if check(report):
            sum_ += 1

    return sum_
