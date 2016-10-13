import collections

circular = collections.deque(maxlen=2)
for i in range(5):
	circular.append(i)
	print(circular)
