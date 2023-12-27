def look_around(matrix, height, width, i, j):
	positions = []

	# Check on the left
	if 0 <= j - 1 and matrix[i][j - 1].isdigit():
		positions.append((i, j - 1))

	# Check on the right
	if j + 1 < width and matrix[i][j + 1].isdigit():
		positions.append((i, j + 1))

	# To not return the same numbers more than one time when looking above / below
	flag_above = True 
	flag_below = True

	for k in range(-1, 2):
		# Check above
		if i - 1 >= 0 and 0 <= j + k < width and matrix[i - 1][j + k].isdigit():
			if flag_above:
				positions.append((i - 1, j + k))
				flag_above = False
		else:
			flag_above = True

		# Check below
		if i + 1 < height and 0 <= j + k < width and matrix[i + 1][j + k].isdigit():
			if flag_below:
				positions.append((i + 1, j + k))
				flag_below = False
		else:
			flag_below = True

	return positions

def get_full_number(line, width, j):
	a = 0
	b = 0

	while j - a >= 0 and line[j - a].isdigit():
		a += 1

	while j + b < width and line[j + b].isdigit():
		b += 1

	return int(line[j - a + 1:j + b])


data = open("2023/day3/input.txt").readlines()

HEIGHT = 140
WIDTH = 140

sumup = 0

for i in range(HEIGHT):
	for j in range(WIDTH):
		if data[i][j] == '*':
			locations = look_around(data, HEIGHT, WIDTH, i, j)

			if len(locations) == 2:
				product = 1

				for (m, n) in locations:
					product *= get_full_number(data[m], WIDTH, n)

				sumup += product

print(sumup)
