gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'GAT':'D', 'CGG':'R'
    }


def split_dna(dna):
    codons = []
    for start in range(0, len(dna)-2, 3):
        codons.append(dna[start:start+3])
    print('codons', codons)
    return codons

dna = 'GTTCACTTGGCCAAGCTATC'
protein = ""
for codon in split_dna(dna):
    aa = gencode.get(codon, '*')
    print('protein', protein)
    print('aa', aa)
    protein = protein + aa
print(protein)
