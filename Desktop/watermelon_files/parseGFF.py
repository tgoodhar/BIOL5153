#! /usr/bin/env python3

from Bio import SeqIO
for seq_record in SeqIO.parse("watermelon.fsa", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))



import csv

#make an output file. Needed when writing out file (create csv writer object).
outfile = 'watermelon.tab'

#open the output file.  "tabout is the file handle".
with open(outfile, 'w') as tabout:

# open the data file
    with open('watermelon.csv', 'r') as watermelon:

        # create a csv reader object
        csvreader = csv.reader(shaver, delimiter=',')

        for line in csvreader:
            if not line:
                continue
            else:
                # create csv writer object
                linewriter = csv.writer(tabout, delimiter='\t', quotechar='"')
                linewriter.writerow(line)
