def filter_reads(reads, threshold):
    for read in list(reads):
        if read.count('N') >= threshold:
            reads.remove(read)

reads = []
def create_reads():
    global reads
    reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']

create_reads()
filter_reads(reads, 1)
assert reads == ['ATCGTAC']

create_reads()
filter_reads(reads, 2)
assert reads == ['ATCGTAC', 'ACTGNTTACGT']


create_reads()
filter_reads(reads, 3)
assert reads == ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']
