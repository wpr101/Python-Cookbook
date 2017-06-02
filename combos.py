import itertools

iterable = range(10)
def combos():

    for s in xrange(len(iterable)+1):
        for comb in itertools.combinations(iterable, s):
            yield comb

c = combos()
while True:
    try:
        print(c.next())
    except StopIteration:
        print('Done!')
        break
