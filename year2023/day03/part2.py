def lookAround(matrix: [str], height: int, width: int, i: int, j: int) -> (int, int):
	"""
	Searches around the cell (i, j) for a digit
	"""

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

def getFullNumber(line: str, width: int, j: int) -> int:
	"""
	From the position j in a given line, looks left and right to get a complete number
	"""

	a = 0
	b = 0

	while j - a >= 0 and line[j - a].isdigit():
		a += 1

	while j + b < width and line[j + b].isdigit():
		b += 1

	return int(line[j - a + 1:j + b])


def prepare(src: str) -> ([str], int, int):
	"""
	Import data from a file, and format them
	"""

	with open(src, 'r') as file:
		data = file.readlines()

	return data, len(data), len(data[0]) - 1

def solve(data: ([str], int, int)) -> int:
	"""
	Determine the flag of data
	"""

	matrix, height, width = data	  
	counter = 0

	for i in range(height):
		for j in range(width):
			if matrix[i][j] == '*':
				locations = lookAround(matrix, height, width, i, j)

				if len(locations) == 2:
					product = 1

					for (m, n) in locations:
						product *= getFullNumber(matrix[m], width, n)

					counter += product

	return counter
