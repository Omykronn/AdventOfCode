with open("2023/day19/input.txt", 'r') as src:
    # Mapping workflows
    workflows_list = {}
    translator = {'x': 0, 'm': 1, 'a': 2, 's': 3}

    line = src.readline()
    
    while len(line) > 1:
        name, conditions = line.replace('}\n', '').split('{')

        workflows_list[name] = [[], None]

        conditions = list(map(lambda s: s.split(':'), conditions.split(',')))

        for item in conditions:
            if len(item) == 1:
                workflows_list[name][1] = item[0]
            else:
                workflows_list[name][0].append((translator[item[0][0]], item[0][1] == '<', int(item[0][2:]), item[1]))

        line = src.readline()

    # Mapping pieces
    pieces_list = []

    line = src.readline()

    while line:
        line = line.replace('=', ',').replace("}\n", '').split(',')

        pieces_list.append(tuple(int(line[2*k + 1]) for k in range(4)))

        line = src.readline()

def apply_workflow(piece, workflow):
    i = 0
    
    while i < len(workflow[0]):
        if (piece[workflow[0][i][0]] < workflow[0][i][2]) == workflow[0][i][1]:
            return workflow[0][i][3]

        i += 1

    return workflow[1]


sum_ = 0

for piece in pieces_list:
    position = "in"

    while len(position) > 1:
        position = apply_workflow(piece, workflows_list[position])

    if position == 'A':
        sum_ += sum(piece)

print(sum_)
