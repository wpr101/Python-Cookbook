import profile

if __name__ == '__main__':
	profiler = profile.Profile()
	for i in range(10):
		print(profiler.calibrate(100000))
