class Node:
    END_OF_TEXT = chr(3)

    def __init__(self):
        self.sons = {}

    def append(self, sequence):
        if len(sequence) == 0:
            self.sons[Node.END_OF_TEXT] = None
        else:
            if not sequence[0] in self.sons:
                self.sons[sequence[0]] = Node()

            self.sons[sequence[0]].append(sequence[1:])

    def is_prefix_in(self, sequence):
        if Node.END_OF_TEXT in self.sons:
            return 0

        if len(sequence) > 0 and sequence[0] in self.sons:
            next = self.sons[sequence[0]].is_prefix_in(sequence[1:])
            
            return next + (next >= 0)
        else:
            return -1


table = {"one": 1, "1": 1, "two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5, "5": 5, "six": 6, "6": 6, "seven": 7, "7": 7, "eight": 8, "8": 8, "nine": 9, "9": 9}
tree = Node()

for word in table:
    tree.append(word)


def find_digits(s: str):
    first = 0
    last = 0

    for i in range(len(s)):
        j = tree.is_prefix_in(s[i:])

        if j >= 0:
            last = table[s[i:i+j]]
        
            if first == 0:
                first = table[s[i:i+j]]

    return 10*first + last


sumup = 0

with open("2023/day1/input.txt", 'r') as src:    
    for line in src.readlines():
        sumup += find_digits(line)

print(sumup)