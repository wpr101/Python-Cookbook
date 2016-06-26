import numpy as np

a = np.array([0, 0.5, 1.0, 1.5, 2.0])

print(a.sum())
print(a.std())
print(a.cumsum())

print(a*2)
print(a**2)
print(np.sqrt(a))

b = np.array([a, a*2])
print(b)

#sum along columns
print(b.sum(axis=0))

#sum along rows
print(b.sum(axis=1))

r = np.random.standard_normal((4,3))
print(r)
