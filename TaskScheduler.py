from collections import deque

class TaskScheduler:
	def __init__(self):
		self._task_queue = deque()

	def new_task(self, task):
		self._task_queue.append(task)

	def run(self):
		while self._task_queue:
			task = self._task_queue.popleft()
			try:
				next(task)
				self._task_queue.append(task)
			except StopIteration:
				pass

def countdown(n):
	while n > 0:
		print('T-minus', n)
		yield
		n -= 1
	print('Blastoff!')

def countup(n):
	x = 0
	while x < n:
		print('Counting up', x)
		yield
		x += 1

sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()
