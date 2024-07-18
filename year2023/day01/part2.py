from toolbox.tree import Node


def findDigits(s: str, tree: Node, translator: dict) -> int:
    """
    Finds the first and last digits in s even in their litteral writing.
    Then returns the concatenation of their numerical writing.
    """
    first = 0
    last = 0

    for i in range(len(s)):
        # Test if the first characters of s[i:] are a number
        j = tree.isPrefixIn(s[i:])  
        
        if j >= 0:
            last = translator[s[i:i+j]]
        
            if first == 0:
                first = translator[s[i:i+j]]

    return 10*first + last

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.readlines()

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    # Initialize tree 
    littToNum = {"one": 1, "1": 1, "two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5, "5": 5, "six": 6, "6": 6, "seven": 7, "7": 7, "eight": 8, "8": 8, "nine": 9, "9": 9}
    tree = Node()

    for word in littToNum:
        tree.append(word)

    # Count
    counter = 0

    for line in data:
        counter += findDigits(line, tree, littToNum)

    return counter