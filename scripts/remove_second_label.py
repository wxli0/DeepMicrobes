"""
Removes the second label from the concatenated trimed simulated reads fasta files

This script must be run within the folder there the concatenated file (e.g. train.fa) is in
"""

from Bio import SeqIO
import config 
import os 
import sys 

file = "/mnt/sda/DeepMicrobes-data/HGR_species_label_reads/Task1_w_old_label.fa"
output_file = "/mnt/sda/DeepMicrobes-data/HGR_species_label_reads/Task1.fa"

fasta_sequences = SeqIO.parse(open(os.path.join(file)),'fasta') 
out_file= open(output_file, 'w')
all_labels = []
for fasta in fasta_sequences:
    id, seq = fasta.id, str(fasta.seq)
    id_split = id.split("|")
    del id_split[2:4]
    new_label = int(id_split[1])
    all_labels.append(new_label)
    new_id = "|".join(id_split)
    # print(new_id)
    out_file.write(">"+new_id+"\n")
    out_file.write(seq+"\n")
out_file.close()

print("number of labels is:", len(list(set(all_labels))))