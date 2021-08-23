import config
import os 
import pandas as pd
from Bio import SeqIO

input_dir = '/mnt/sda/DeepMicrobes-data/labeled_genome/'
output_dir = '/mnt/sda/DeepMicrobes-data/labeled_genome_new_label-r202/'
S1_path = os.path.join(config.MLDSP_path, 'samples/Table_S1_new.csv')

S1 = pd.read_csv(S1_path, header=0, index_col=0)

# construct visited
visited = []
for file in os.listdir(input_dir):
    index = file[:-3]
    cur_species = S1.loc[index]['Species']
    if cur_species not in visited:
        visited.append(cur_species)

# construct name2label_species_r202.txt
name2label_path = os.path.join(config.DM_path, 'data/name2label_species_r202.txt')
if not os.path.exists(name2label_path):
    name2label_file = open(name2label_path, mode='w')
    for v in visited:
        name2label_file.write(v+'\t'+str(visited.index(v))+'\n')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)
    for file in os.listdir(input_dir):
        index = file[:-3]
        cur_species = S1.loc[index]['Species']
        mode = 'w'
        label = visited.index(cur_species)
        fasta_sequences = SeqIO.parse(open(os.path.join(input_dir, file)),'fasta')
        for fasta in fasta_sequences:
                id, sequence = fasta.id, str(fasta.seq) 
                out_file= open(os.path.join(output_dir, file[:-3]+'_new.fa'), mode)
                out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
                out_file.write(sequence+"\n")
                out_file.close()
                mode = 'a'
        print("done", file)

