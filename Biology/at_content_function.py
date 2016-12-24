import pdb

def at_content(dna):
    a = dna.count("A")
    t = dna.count("T")
    at_content = float((a + t)) / len(dna)
    return at_content

def clean_dna(dna):
    result = ""
    for base in dna:
        if base.upper() in ['A', 'T', 'G', 'C']:
            result = result + base.upper()
    return result

seqs = [
    "actgtacgtacgtagctacg",
    "CGGCTGGTGTTAACGGCTAT",
    "ACTGTGANTGCTCGATGTGC",
    "CGCNTCGTGCTA"
]

for dna in seqs:
    #pdb.set_trace()
    print("looking at sequence: " + dna)
    cleaned = clean_dna(dna)
    at = at_content(cleaned)
    print("at content is " + str(at))
