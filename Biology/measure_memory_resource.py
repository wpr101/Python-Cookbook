from __future__ import division
import resource

r = range(1000000)

resource_object = resource.getrusage(resource.RUSAGE_SELF)
memory = resource_object.ru_maxrss

print("Used this much memory: " + str(memory))
