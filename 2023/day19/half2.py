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


queue = [([(1, 4000), (1, 4000), (1, 4000), (1, 4000)], 'in', 0)] 
sum_ = 0

while queue:
    intervals, name, step = queue.pop(0)

    if len(name) == 1:        
        if name == 'A':
            product = 1

            for i in range(4):
                product *= (intervals[i][1] - intervals[i][0] + 1)

            sum_ += product

    else:
        # Workflow end reached
        if step == len(workflows_list[name][0]):
            queue.append((intervals, workflows_list[name][1], 0))

        # Interval must be splat in two
        elif intervals[workflows_list[name][0][step][0]][0] <= workflows_list[name][0][step][2] <= intervals[workflows_list[name][0][step][0]][1]:
            if workflows_list[name][0][step][1]: # <
                queue.append(([(intervals[i][0], workflows_list[name][0][step][2] - 1) 
                            if i == workflows_list[name][0][step][0] else intervals[i] 
                            for i in range(4)], 
                            workflows_list[name][0][step][3],
                            0))

                queue.append(([(workflows_list[name][0][step][2], intervals[i][1]) 
                            if i == workflows_list[name][0][step][0] else intervals[i] 
                            for i in range(4)], 
                            name,
                            step + 1))

            else:  # >
                queue.append(([(intervals[i][0], workflows_list[name][0][step][2]) 
                            if i == workflows_list[name][0][step][0] else intervals[i] 
                            for i in range(4)], 
                            name,
                            step + 1))

                queue.append(([(workflows_list[name][0][step][2] + 1, intervals[i][1]) 
                            if i == workflows_list[name][0][step][0] else intervals[i] 
                            for i in range(4)], 
                            workflows_list[name][0][step][3],
                            0))

        # Interval affecte in the same way
        elif intervals[workflows_list[name][0][step][0]][1] < workflows_list[name][0][step][2]:
            if workflows_list[name][0][step][1]:  # <
                queue.append((intervals, workflows_list[name][0][step][3], 0))
            else:  # >
                queue.append((intervals, name, step + 1))

        elif workflows_list[name][0][step][2] < intervals[workflows_list[name][0][step][0]][0]:
            if workflows_list[name][0][step][1]:  # <
                queue.append((intervals, name, step + 1))
            else:  # >
                queue.append((intervals, workflows_list[name][0][step][3], 0))


print(sum_)