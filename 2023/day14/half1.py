def next_absciss(matrix, i, j):
    k = i
    
    while k > 0 and matrix[k - 1][j] == '.':
        k -= 1
        
    return k


data = list(map(lambda s: list(s.replace('\n', '')), open("2023/day14/input.txt", 'r')))
sum_ = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'O':                        
            new_i = next_absciss(data, i, j)
            
            data[i][j] = '.'
            data[new_i][j] = 'O'
            
            sum_ += len(data) - new_i
            
print(sum_)            
