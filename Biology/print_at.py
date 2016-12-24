import at_calculator

dna = open('dna.txt').read().rstrip("\n")

print("AT content is " + str(at_calculator.calculate_at(dna)))
