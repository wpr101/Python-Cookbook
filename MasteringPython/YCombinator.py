Y = lambda f: lambda *args: f(Y(f))(*args)

def factorial(combinator):
	def _factorial(n):
		if n:
			return n * combinator(n-1)
		else:
			return 1
	return _factorial

print(Y(factorial)(5))


print(Y(lambda c: lambda n: n and n * c(n-1) or 1)(5))
