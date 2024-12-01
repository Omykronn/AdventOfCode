def naturalOrder(n1: int, n2:int) -> bool:
    """
    Check if n1 is greater than n2
    """
    
    return n1 >= n2

def bubbleSort(data: list, superior: callable = naturalOrder) -> None:
    """
    Sort data with the order function superior (must return a boolean)
    """

    for k in range(len(data)):
        for i in range(k - 1, -1, -1):
            if superior(data[i], data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i] 