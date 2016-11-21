from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total/count
	return Result(count, average)

#coro_avg = averager()
#next(coro_avg)
#coro_avg.send(10)
#coro_avg.send(30)
#coro_avg.send(6.5)
#coro_avg.send(None)
