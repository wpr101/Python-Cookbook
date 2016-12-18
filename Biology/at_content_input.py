#import pdb

dna = raw_input("Enter a DNA sequence:\n")
at = (float(dna.count('A')) + float(dna.count('T'))) / len(dna)
#pdb.set_trace()
print("AT content is " + str(at))
