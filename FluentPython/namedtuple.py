from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo[1])

print(City._fields)
print(tokyo._asdict())

for key, value in tokyo._asdict().items():
	print(key + ':', value)
