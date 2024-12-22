def prepare(src: str) -> [[int]]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [[int(n) for n in line.replace('\n', '').split(' ')] for line in file.readlines()]

    return data

def badLevels(report: [int], variation: int = 1) -> [int]:
    """
    List errors in a report according to the defined variation
    """

    errorIndexes = []

    for i in range(len(report) - 1):
        if (report[i + 1] - report[i]) * variation <= 0 or abs(report[i + 1] - report[i]) > 3:
            errorIndexes.append(i)

    return errorIndexes  

def dampenerPossible(report, errors, variation: int = 1) -> bool:
    """
    Check with the list of errors if they can be corrected according to the defined variation
    """

    flag = False
    
    if len(errors) == 0:
        flag = True
    elif len(errors) == 1:
        i = errors[0]

        # If first (resp. last) variation illicit, just take out first (resp. last) lever
        flag = i == 0 or i == len(report) - 2
        
        # Test if report without (i+1)th lever is legit
        if not(flag) and i + 2 < len(report):
            flag = (report[i + 2] - report[i]) * variation > 0 and abs(report[i + 2] - report[i]) <= 3

        # Test if report without ith lever is legit
        if not(flag) and i - 1 >= 0 and i + 1 < len(report):
            flag = (report[i + 1] - report[i - 1]) * variation > 0 and abs(report[i + 1] - report[i - 1]) <= 3
    elif len(errors) == 2:
        # If there are 2 errors, the only possibility is when they are consecutive
        if not(flag) and errors[1] == errors[0] + 1:
            i = errors[0] 
            flag = (report[i + 2] - report[i]) * variation > 0 and abs(report[i + 2] - report[i]) <= 3

    return flag

def check(report: [int]) -> bool:
    """
    Check if a report is licit
    """ 

    return dampenerPossible(report, badLevels(report)) or dampenerPossible(report, badLevels(report, -1), -1)

def solve(data: [[int]]) -> int:
    """
    Determine the flag of data
    """
    sum_ = 0

    for report in data:
        if check(report):
            sum_ += 1

    return sum_
