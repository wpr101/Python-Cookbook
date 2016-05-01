def primes():
	n = 100
	flags = [1 for _ in range(n)]
	for i in range(2,n):
		if flags[i] == 0:
			continue
		for j in range(i,n):
			if (j%i == 0 and (i != j)):
				flags[j] = 0
	for x in range(2, len(flags)):
		if flags[x] == 1:
			print(x)
	
primes()
