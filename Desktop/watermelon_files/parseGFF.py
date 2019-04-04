#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = "")

# add positional arguments, i.e., the required input

parser.add_argument( "-gf", "--gff", help="the name of the gff file", default="watermelon.gff")
# when running the script, ./parseGff.py -gf watermelon.gff
parser.add_argument( "-fa", "--fasta", help="the name of the fasta file", default="watermelon.fsa")
# when running the script, ./parseGFF.py -fa watermelon.fsa

#parser.add_argument( "go", "--output", help="the name of the written output file" )?
    # when running the script, ./parseGff.py -go gff_ouput.txt

#parser.add_argument( "ss", "--substring_txt", help="the name of the written substring file" )?
    # when running the script, ./parseGFF.py -ss substring

# parse the command line arguments
args = parser.parse_args()

gff_file = args.gff
gff = open(gff_file, "r")
gff_output = open("gff_output.txt", "w")

for line in gff:
    fields = line.split('\t')
    start = int(fields[3])
    stop = int(fields[4])
    print(str(start) + "\t" + str(stop))
    
    gff_substring = (fields[3], fields[4])
    
    gff_output.write(str(start) + "\t" + str(stop) + "\n")

fasta_file = open(args.fasta).read()
fasta_output = open("gff_output.txt")
substring = open("substring.txt", "w")

for lines in fasta_output:
    positions = lines.split('\t')
    start = int(positions[0])
    stop = int(positions[1])
    substring_sequence = fasta[start:stop]
    print(substring_sequence)
    

    # ./parseGFF.py -gf watermelon.gff -fa watermelon.fsa