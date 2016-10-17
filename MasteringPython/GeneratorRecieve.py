def generator():
	value = yield 'spam'
	print('Generator recieved: %s' % value)
	yield 'Previous value: %r' % value

g = generator()
print('Result from generator: %s' % next(g))
print(g.send('eggs'))
