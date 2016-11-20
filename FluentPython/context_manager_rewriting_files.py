import csv
import contextlib

with inplace(csvfilename, 'r', newline='') as (infh, outfh):
	reader = csv.reader(infh)
	writer = csv.writer(outfh)

	for row in reader:
		row += ['new', 'columns']
		writer.writerow(row)
