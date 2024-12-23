from toolbox.string import findWordInDirections

def prepare(src: str) -> [str]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.read().split('\n')

    return data

def solve(data: [str]) -> int:
    """
    Determine the flag of data
    """

    return len(findWordInDirections("XMAS", data))
