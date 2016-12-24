from nose.tools import assert_equal

def find_common_kmers(dna, k, threshold):
    if k < 1:
        return []
    result = []
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        if dna.count(kmer) >= threshold and kmer not in result:
            result.append(kmer)
    return result

def test_3mers():
    assert_equal(find_common_kmers('atgaatgcaaatga', 3, 3), ['atg'])
