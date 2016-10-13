import random
numbers = [random.random() for _ in range(10)]
print([x for x in numbers if x >= 0.5])
