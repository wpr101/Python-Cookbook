import operator
import functools
print(functools.reduce(operator.mul, range(1,6)))
