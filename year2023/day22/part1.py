from year2023.day22.common import Block


def prepare(src: str) -> [Block]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.read().split('\n')

    data = [[[int(n) for n in coordinates.split(',')] for coordinates in line.split('~')] for line in data]

    return [Block(coors[0], coors[1]) for coors in data] 


def solve(data: [Block]) -> int:
    """
    Determine the flag of data
    """

    # Determine the list of all blocks that are under each block
    for block1 in data:
        for block2 in data:
            if block1.is_above(block2):
                block1.underlist.append(block2)
    
    for block in data:
        for underBlock in block.underlist:
            if underBlock.getFinalZ() + underBlock.height + 1 == block.getFinalZ():
                underBlock.supported.append(block)
                block.nb_supporters += 1

    counter = 0

    for block in data:
        flag = True
        i = 0

        while i < len(block.supported) and flag:
            flag = flag and block.supported[i].nb_supporters > 1
            i += 1
        
        counter += flag

    return counter
