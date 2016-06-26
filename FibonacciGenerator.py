def fibonacci():
	i, j = 0, 1
	while True:
		yield j
		i, j = j, i + j

def fibonacci_transform():
	count = 0
	for f in fibonacci():
		if f > 5000:
			break
		if f % 2:
			count += 1
	print count
	return count

fibonacci_transform()
