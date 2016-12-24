def at_content(dna):
    return (dna.count('A') + dna.count('T')) / len(dna)

def same_start(dna1, dna2):
    return dna1[0:5] == dna2[0:5]

def find_interesting(dnas, cutoff):
    interesting = set()
    for one in dnas:
        at = at_content(one)
        if at > cutoff:
            for two in dnas:
                if one != two and same_start(one, two):
                    interesting.add(one)

    return(interesting)
