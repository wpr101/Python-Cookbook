def square(n):
	'''

	>>> square(0)
	0
	>>> square(1)
	1
	>>> square(2)
	4
	>>> square(3)
	9

	Args:
		n (int): The number to square

	Returns:
		int: The sqaured result
	'''
	return n * n

if __name__ == '__main__':
	import doctest
	doctest.testmod()
