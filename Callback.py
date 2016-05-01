def apply_async(func, args, callback):
	result = func(*args)
	callback(result)

def print_result(result):
	print('Got:', result)

def add(x,y):
	return x + y

apply_async(add, (2,3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
