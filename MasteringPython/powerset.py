import itertools

def powerset(iterable):
	return itertools.chain.from_iterable(
		itertools.combinations(iterable, i)
		for i in range(len(iterable) + 1))

print(list(powerset(range(3))))
