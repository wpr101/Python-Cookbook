dna = "ATCGTACGTACT"
motifs = ["ATCG", "ATCC"]

@profile
def classify_chunks():
    frequent_chunks = []
    for start in range(len(dna) - 3):
        chunk = dna[start:start + 4]
        if dna.count(chunk) > 50:
            frequent_chunks.append(chunk)

    for chunk in frequent_chunks:
        if chunk in motifs:
            print(chunk + " is frequent and interesting")
        else:
            print(chunk + " is frequent but not interesting")

classify_chunks()
