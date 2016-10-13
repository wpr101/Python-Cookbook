import functools

eggs = [functools.partial(lambda i, a: i * a, i) for i in range(3)]

for egg in eggs:
	print(egg(5))
