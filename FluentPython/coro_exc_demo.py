class DemoException(Exception):
	"""An exception type for the demonstration."""

def demo_exc_handling():
	print('-> coroutine started')
	while True:
		try:
			x = yield
		except DemoException:
			print('*** DemoException handled. Continuing...')
		else:
			print('-> coroutine received: {!r}'.format(x))
	raise RuntimeError('This line should never run.')

#exc_coro = demo_exc_handling()
#next(exc_coro)
#exc_coro.send(11)
#exc_coro.send(22)
#exc_coro.close()
from inspect import getgeneratorstate
#print(getgeneratorstate(exc_coro))

#16-10
#exc_coro = demo_exc_handling()
#next(exc_coro)
#exc_coro.send(11)
#exc_coro.throw(DemoException)
#print(getgeneratorstate(exc_coro))

#16-11
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(ZeroDivisionError)
print(getgeneratorstate(exc_coro))



