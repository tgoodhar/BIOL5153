#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = "")

# add positional arguments, i.e., the required input
parser.add_argument( "-gf", "--gff", help="the name of the gff file", default="watermelon.gff")
# when running the script, ./parseGff.py -gf watermelon.gff
parser.add_argument( "-fa", "--fasta", help="the name of the fasta file", default="watermelon.fsa")
# when running the script, ./parseGFF.py -fa watermelon.fsa

# parse the command line arguments
args = parser.parse_args()

# read gff file
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

# read fasta file
fasta_file = open(args.fasta).read()
fasta_output = open("gff_output.txt")
substring = open("substring.txt", "w")

for lines in fasta_output:
    positions = lines.split('\t')
    start = int(positions[0])
    stop = int(positions[1])
    substring_sequence = fasta[start:stop]
    print(substring_sequence)

# calculate GC content of each feature
genome = open("substring.txt").read()
length = len(genome)
G_content = genome.count('G')
C_content = genome.count('C')

print("length: " + str(length))
print("g count: " + str(G_content))
print("C count: " + str(C_content))

GC_content = (G_content + C_content) / length 

print("GC content: " + str(gc_content))


# calculating complements
replacement1 = genome.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)

print("sequence complement: " + replacement4.upper())



#from Bio import SeqIO
#genome = SeqIO.read('watermelon.fsa', 'fasta')
#print(genome.seq)
#print(len(genome.seq))
#print(genome.reverse_complement)