def findNumbers(matrix: [str], height: int, width: int) -> [(int, int, int)]:
	"""
	Returns coordinates of the start of each number, and their length
	"""

	locations = []
	k = 0

	for i in range(height):
		for j in range(width):
			if matrix[i][j].isdigit():
				k += 1
			elif k > 0:
				locations.append((i, j-k, k))
				k = 0 

		if k > 0:
			locations.append((i, j-k + 1, k))
			k = 0 

	return locations

def symbolAround(matrix: [str], height: int, width: int, i: int, j: int, k: int) -> bool:
	"""
	Tests if there is a symbol different of . around the line form (i, j) to (i, j + k - 1)
	"""

	flag = (j - 1 >= 0 and matrix[i][j - 1] != '.') or (j + k < width and matrix[i][j + k] != '.')

	for m in range(j - 1, j + k + 1):
		# Check above
		if i - 1 >= 0 and 0 <= m < width and matrix[i - 1][m] != '.':
			flag = True

		# Check below
		if i + 1 < height and 0 <= m < width and matrix[i + 1][m] != '.':
			flag = True

	return flag

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

	for i, j, k in findNumbers(matrix, height, width):
		if symbolAround(matrix, height, width, i, j, k):
			counter += int(matrix[i][j:j+k])

	return counter
