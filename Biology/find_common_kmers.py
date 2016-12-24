def find_common_kmers(dna, k, threshold):
    if k < 1:
        return []
    result = []
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        if dna.count(kmer) >= threshold and kmer not in result:
            result.append(kmer)
    return result

#print(find_common_kmers('atgaatgc', 3, 2))

#assert find_common_kmers('atgaatgc', 3, 2) == ['atg']

assert find_common_kmers('atgaatgcaaatga', 3, 3) == ['atg']
