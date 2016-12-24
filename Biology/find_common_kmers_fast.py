def find_common_kmers(dna, k, threshold):
    if k < 1:
        return []

    kmer2count = {}
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        old_count = kmer2count.get(kmer,0)
        kmer2count[kmer] = old_count + 1

    result = []
    for kmer, count in kmer2count.items():
        if count >= threshold:
            result.append(kmer)
    return result
