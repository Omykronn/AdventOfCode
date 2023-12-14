def find_numbers(matrix, height, width):
	locations = []
	k = 0

	for i in range(height):
		for j in range(width):
			if matrix[i][j].isdigit():
				k += 1
			elif k > 0:
				locations.append((i, j-k, k))
				k = 0 

	return locations

def check_around(matrix, height, width, i, j, k):
	flag = (j - 1 >= 0 and matrix[i][j - 1] != '.') or (j + k < width and matrix[i][j + k] != '.')

	if (j - 1 >= 0 and matrix[i][j - 1] != '.'):

	if (j + k < width and matrix[i][j + k] != '.'):

	for m in range(j - 1, j + k + 1):
		# Check above
		if i - 1 >= 0 and 0 <= m < width and matrix[i - 1][m] != '.':
			flag = True

		# Check below
		if i + 1 < height and 0 <= m < width and matrix[i + 1][m] != '.':
			flag = True

	return flag


data = open("2023/day3/input.txt").readlines()

HEIGHT = 140
WIDTH = 140

sumup = 0

for i, j, k in find_numbers(data, HEIGHT, WIDTH + 1):  # WIDTH + 1 because of \n at the end of each line
	if check_around(data, HEIGHT, WIDTH, i, j, k):
		sumup += int(data[i][j:j+k])

print(sumup)
