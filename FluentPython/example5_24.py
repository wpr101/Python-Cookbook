from collections import namedtuple
from operator import itemgetter
from operator import attrgetter

metro_data = [
	('Tokyo', 'JP', 37, (35, 139)),
	('Delhi', 'IN', 22, (28, 77)),
	('Mexico City', 'MX', 20, (19, -99)),
	('New York', 'US', 20, (41, -74)),
	('Sao Paulo', 'BR', 19.6, (-24, -46)),
]

for city in sorted(metro_data, key=itemgetter(1)):
	print(city)

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
	for name, cc, pop, (lat, long) in metro_data]

print(metro_areas[0])
print(metro_areas[0].coord.lat)

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
	print(name_lat(city))

