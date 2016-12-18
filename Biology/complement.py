import pdb

dna = "ATGCGTGATGC"
pdb.set_trace()

dna = dna.replace("A", "T")
dna = dna.replace("C", "G")
dna = dna.replace("G", "C")
dna = dna.replace("T", "A")

print(dna)
