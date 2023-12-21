from math import sqrt, ceil, floor

def margin(time, distance):
    delta = time**2 - 4*distance

    if delta >= 0:
        x1, x2 = (time - sqrt(delta))/2, (time + sqrt(delta))/2
        int_x1, int_x2 = ceil(x1), floor(x2)
        distance = int_x2 - int_x1 + 1

        if x1 == int_x1:
            distance -= 1
        
        if x2 == int_x2:
            distance -= 1

        return distance
    else:
        return 0


data = []

with open("2023\day6\input.txt", 'r') as src:
    for line in src.readlines():
        data.append([0])

        for c in line:
            if c.isdigit():
                data[-1][-1] = data[-1][-1] * 10 + int(c)
            elif data[-1][-1] != 0:
                data[-1].append(0)

product = 1

for i in range(len(data[1])):
    product *= margin(data[0][i], data[1][i])

print(product)
