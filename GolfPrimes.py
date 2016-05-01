import array as a

def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

prime_list = a.array('i',[])
flag = False
for i in gen_primes():
    if (i < 1000000):
        print(i)
        prime_list.append(i)
    else:
        print("here")
        break
print(prime_list)
