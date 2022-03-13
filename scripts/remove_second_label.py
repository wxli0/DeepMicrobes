"""
Removes the first label from the concatenated trimed simulated reads fasta files

This script must be run within the folder there the concatenated file (e.g. train.fa) is in
"""

from Bio import SeqIO
import config 
import os 
import sys 

file = "/mnt/sda/DeepMicrobes-data/HGR_species_label_reads/Task1_w_old_label.fa"
output_file = ""

fasta_sequences = SeqIO.parse(open(os.path.join(file)),'fasta') 
out_file= open(output_file, 'w')
counter = 0
for fasta in fasta_sequences:
    id, seq = fasta.id, str(fasta.seq)
    seq_split = seq.split("|")
    del seq_split[2:4]
    new_id = "|".join(seq_split)
    print(new_id)

#     out_file.write(">"+new_id+"\n")
#     out_file.write(seq+"\n")
# out_file.close()