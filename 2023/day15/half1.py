def HASH_algorithm(string: str):
    current_value = 0

    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


sum_ = 0

for word in open("2023/day15/input.txt", 'r').readline().replace('\n', '').split(','):
    sum_ += HASH_algorithm(word)

print(sum_)
