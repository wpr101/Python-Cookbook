#import pdb

sequences = [
'ATCGTAGTCGA',
'ATCGTTAGCT',
'ATCGTAGCGTGTAC'
]
total_at = 0

for dna in sequences:
    
    for base in dna:
        if base == 'A' or base == 'T':
            total_at = total_at + 1
        #pdb.set_trace()

total_length = sum(map(len,sequences))

print("Average AT content: " + str(total_at/total_length))
