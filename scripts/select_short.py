import os
import sys
from Bio import SeqIO

input_dir="/mnt/sda/MLDSP-samples-r202/rumen_mags/root"
new_dir = input_dir+"_short_kraken"
new_seq_count = 0
for file in os.listdir(input_dir):
    if file.endswith('.fasta'):
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(input_dir, file)),'fasta')
        output_file = open(os.path.join(new_dir, file), 'w')
        shortest_seq = ''
        shortest_id = None
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            if shortest_id == None:
                shortest_id = id
                shortest_seq = seq
                new_seq_count += 1
            elif len(seq) < len(shortest_seq):
                shortest_seq = seq
                shortest_id = id
        output_file.write(">"+shortest_id + "\n")
        output_file.write(shortest_seq+"\n")
