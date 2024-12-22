def readNextInt(string: str, i: int) -> int:
    """
    Read the next next integer from a position in a string 
    """
    n = 0

    while i < len(string) and string[i].isdigit():
        n = 10*n + int(string[i])
        i += 1

    return n