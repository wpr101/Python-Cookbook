import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')

# BEGIN TAXI PROCESS
def taxi_process(ident, trips, start_time=0):
	"""Yield to simulator issuing event at each state change"""
	time = yield Event(start_time, ident, 'leave garage')
	for i in range(trips):
		time = yield Event(time, ident, 'pick up passenger')
		time = yield Event(time, ident, 'drop off passenger')
	yield Event(time, ident, 'going home')

class Simulator:

	def __init__(self, procs_map):
		self.events = queue.PriorityQueue()
		self.procs = dict(procs_map)

	def run(self, end_time):
		"""Schedule and display events until time is up"""
		for _, proc in sorted(self.procs.items()):
			first_event = next(proc)
			self.events.put(first_event)

		sim_time = 0
		while sim_time < end_time:
			if self.events.empty():
				print('*** end of events ***')
				break

			current_event = self.events.get()
			sim_time, proc_id, previous_action, = current_event
			print('taxi:', proc_id, proc_id * ' ', current_event)
			active_proc = self.procs[proc_id]
			next_time = sim_time + compute_duration(previous_action)
			try:
				next_event = active_proc.send(next_time)
			except StopIteration:
				del self.procs[proc_id]
			else:
				self.events.put(next_event)

		else:
			msg = '*** end of simulation time: {} events pending ***'
			print(msg.format(self.events.qsize()))

def compute_duration(previous_action):
	"""Compute action duration using exponential distribution"""
	if previous_action in ['leave garage', 'drop off passenger']:
		interval = SEARCH_DURATION
	elif previous_action == 'pick up passenger':
		interval = TRIP_DURATION
	elif previous_action == 'going home':
		interval = 1
	else:
		raise ValueError('Unknown previous_action: %s' % previous_action)
	return int(random.expovariate(1/interval)) + 1

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
		 seed=None):
	if seed is not None:
		random.seed(seed)

	taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
			for i in range(num_taxis)]
	sim = Simulator(taxis)
	sim.run(end_time)

if __name__ == '__main__':
	parser = argsparse.ArgumentParser(
					description = 'Taxi fleet simulator.')
	#TODO
		


