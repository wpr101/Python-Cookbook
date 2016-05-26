import functools

def f(x):
    return (x ** 2)

def even(x):
    return (x % 2 == 0)

print(f(2))
print(even(3))

print(list(map(even, range(10))))

print(list(map(lambda x: x ** 2, range(10))))

print(list(filter(even, range(15))))

print(functools.reduce(lambda x, y: x+y, range(10)))
