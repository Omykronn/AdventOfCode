# NB: Check if final solution is not already reached


def move_north(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):            
            if matrix[i][j] == 'O':     
                k = i
                                                   
                while k > 0 and matrix[k - 1][j] == '.':
                    k -= 1
                
                matrix[i][j] = '.'
                matrix[k][j] = 'O'

        
def move_south(matrix):
    for i in reversed(range(len(matrix))):
        for j in range(len(matrix[0])):            
            if matrix[i][j] == 'O':     
                k = i
                                                   
                while k < len(matrix) - 1 and matrix[k + 1][j] == '.':
                    k += 1
                
                matrix[i][j] = '.'
                matrix[k][j] = 'O'


def move_west(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):            
            if matrix[i][j] == 'O':     
                k = j
                                                   
                while k > 0 and matrix[i][k - 1] == '.':
                    k -= 1
                
                matrix[i][j] = '.'
                matrix[i][k] = 'O'
        
def move_east(matrix):
    for i in range(len(matrix)):
        for j in reversed(range(len(matrix[0]))):            
            if matrix[i][j] == 'O':     
                k = j
                                                   
                while k < len(matrix[0]) - 1 and matrix[i][k + 1] == '.':
                    k += 1
                
                matrix[i][j] = '.'
                matrix[i][k] = 'O'


def find_cycle(sequ):
    i = 0

    while i < len(sequ) and sequ[i] != sequ[-1]:
        i += 1
    
    return i


def get_load(matrix):
    sum_ = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                sum_ += len(data) - i

    return sum_


data = list(map(lambda s: list(s.replace('\n', '')), open("2023/day14/input.txt", 'r')))
sequence = []
loads = [get_load(data)]

while find_cycle(sequence) == len(sequence) - 1 or len(sequence) == 0:  # len(sequence) == 0 is necessary to start the loop
    move_north(data)
    move_west(data)
    move_south(data)    
    move_east(data)

    loads.append(get_load(data))
    sequence.append(hash(tuple([tuple(line) for line in data])))


# We use the fact that the transformations lead to a cycle, which can be use to determine the state after 1,000,000,000 transformations without directly calculating it
start = find_cycle(sequence)
length = len(sequence) - start - 1

print(loads[start + int((1e9 - start) % length)])
