import at_calculator

dna = raw_input("Enter a DNA sequence:\n")
output_filename = raw_input("Enter a filename:\n")

with open(output_filename, "w") as out:
    out.write(str(at_calculator.calculate_at(dna)))
