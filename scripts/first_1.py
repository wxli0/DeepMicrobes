import os
import sys
from Bio import SeqIO

input_dir="/mnt/sda/MLDSP-samples-r202/rumen_mags/root"
new_dir = input_dir+"_kraken"
for file in os.listdir(input_dir):
    if file.endswith('.fasta'):
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(input_dir, file)),'fasta')
        output_file = open(os.path.join(new_dir, file), 'w')
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            output_file.write(">"+id + "\n")
            output_file.write(seq+"\n")
            break # only the first