from nose.tools import assert_equal

def filter_reads(reads, threshold):
    for read in list(reads):
        if read.count('N') >= threshold:
            reads.remove(read)

reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']

#filter_reads(reads, 1)
#assert reads == ['ATCGTAC']

filter_reads(reads, 2)
assert_equal( reads, ['ATCGTAC', 'ACTGNTTACGT'])
