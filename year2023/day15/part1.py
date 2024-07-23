def HashAlgorithm(string: str) -> int:
    """
    Executes HASH algorithm
    """

    current_value = 0

    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.readline().replace('\n', '').split(',')

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    for word in data:
        counter += HashAlgorithm(word)

    return counter

