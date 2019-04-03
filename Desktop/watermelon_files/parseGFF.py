gff_file = "watermelon.gff"
gff = open(gff_file, "r")
gff_output = open("gff_output.txt", "w")

for line in gff:
    fields = line.split('\t')
    start = int(fields[3])
    stop = int(fields[4])
    print(str(start) + "\t" + str(stop))
    
    gff_substring = (fields[3], fields[4])
    
    gff_output.write(str(start) + "\t" + str(stop) + "\n")

fasta_file = open("watermelon.fsa").read()
fasta_output = open("gff_output.txt")
substring = open("substring.txt", "w")

for lines in fasta_output:
    positions = lines.split('\t')
    start = int(positions[0])
    stop = int(positions[1])
    substring_sequence = fasta[start:stop]
    print(substring_sequence)
    