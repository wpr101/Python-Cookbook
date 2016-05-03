import heapq
import threading

class PriorityQueue:
	def __init__(self):
		self._queue  = []
		self._count = 0
		self._cv = threading.Condition()

	def put(self, item, priority):
		with self._cv:
			heapq.heappush(self._queue, (-priority, self._count, item))
			self._count += 1
			self._cv.notify()

	def get(self):
		with self._cv:
			while len(self._queue) == 0:
				self._cv.wait()
			return heapq.heappop(self._queue)[-1]

pq = PriorityQueue()
pq.put(5, 1)
pq.put(7, 9)
pq.put(6, 0)
pq.put(1, 15)

while pq.count > 0:
	print(pq.get())

