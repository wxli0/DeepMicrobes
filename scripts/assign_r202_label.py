import sys
import os 
import pandas as pd
from Bio import SeqIO

input_dir = '/mnt/sda/DeepMicrobes-data/labeled_genome/'
output_dir = '/mnt/sda/DeepMicrobes-data/labeled_genome_new_label-r202/'
S1_path = '/home/w328li/MLDSP/samples/Table_S1_new.csv'

S1 = pd.read_csv(S1_path, header=0, index_col=0)

os.mkdir(output_dir)
visited = []
for file in os.listdir(input_dir):
    index = file[:-3]
    cur_species = S1[index]['Species']
    if cur_species not in visited:
        visited.append(cur_species)
    label = visited.index(cur_species)
    mode = 'w'
    fasta_sequences = SeqIO.parse(open(os.path.join(output_dir, file)),'fasta')
    for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            out_file= open(os.path.join(dir, file[:-3]+'_new.fa'), mode)
            out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
            out_file.write(sequence+"\n")
            out_file.close()
            mode = 'a'
    print("done", file)

