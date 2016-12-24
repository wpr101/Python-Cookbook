gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M'
    }

print ("gencode stores " + str(len(gencode)) + " codons")

def translate_dna(dna):
    last_codon_start = len(dna) - 2
    protein = ""

    for start in range(0, last_codon_start, 3):
        codon = dna[start:start+3]
        amino_acid = gencode.get(codon.upper(), 'X')
        protein = protein + amino_acid

    return protein
