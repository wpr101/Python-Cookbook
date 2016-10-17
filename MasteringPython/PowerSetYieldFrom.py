import itertools

def powerset(sequence):
	for size in range(len(sequence) + 1):
		yield from itertools.combinations(sequence, size)

for result in powerset('abc'):
	print(result)	
