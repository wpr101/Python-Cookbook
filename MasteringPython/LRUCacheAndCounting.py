import functools

def counter(function):
	function.calls = 0
	@functools.wraps(function)
	def _counter(*args, **kwargs):
		function.calls += 1
		return function(*args, **kwargs)
	return _counter

@functools.lru_cache(maxsize=3)
@counter
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
print(fibonacci.cache_info())
print(fibonacci.__wrapped__.__wrapped__.calls)

