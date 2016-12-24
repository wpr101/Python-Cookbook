from __future__ import division

def calculate_at(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

if __name__ == "__main__":
    dna = raw_input("Enter a DNA sequence:\n").rstrip("\n")
    print("AT content is " + str(calculate_at(dna)))

