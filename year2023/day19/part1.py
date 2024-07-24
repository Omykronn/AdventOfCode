def applyWorkflow(piece: (int, int, int, int), workflow: dict):
    """
    Applies workflow's instructions to piece
    """

    i = 0
    
    while i < len(workflow[0]):
        if (piece[workflow[0][i][0]] < workflow[0][i][2]) == workflow[0][i][1]:
            return workflow[0][i][3]

        i += 1

    return workflow[1]

def prepare(src: str) -> (dict, [(int, int, int, int)]):
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = file.read().split('}\n\n')

    # Mapping workflows

    workflows_list = {}
    translator = {'x': 0, 'm': 1, 'a': 2, 's': 3}

    for workflow in data[0].split("}\n"):
        name, conditions = workflow.split('{')

        workflows_list[name] = [[], None]

        conditions = [instructions.split(':') for instructions in conditions.split(',')]

        for item in conditions:
            if len(item) == 1:
                workflows_list[name][1] = item[0]
            else:
                workflows_list[name][0].append((translator[item[0][0]], item[0][1] == '<', int(item[0][2:]), item[1]))

    # Mapping pieces

    pieces_list = []

    for piece in data[1].split('}\n'):
        piece = piece[1:].replace('=', ',').split(',')

        if len(piece) > 1:
            pieces_list.append(tuple(int(piece[2*k+1]) for k in range(4)))

    return workflows_list, pieces_list

def solve(data: (dict, [(int, int, int, int)])) -> int:
    """
    Determine the flag of data
    """

    workflows_list, pieces_list = data
    counter = 0

    for piece in pieces_list:
        position = "in"

        while len(position) > 1:
            position = applyWorkflow(piece, workflows_list[position])

        if position == 'A':
            counter += sum(piece)

    return counter
