primes = set((1,2,3,5,7))

'''
items = list(range(10))
for prime in primes:
	items.remove(prime)
print(items)
'''

'''
items = list(range(10))
print([item for item in items if item not in primes])
'''

items = list(range(10))
print(list(filter(lambda item: item not in primes, items)))

