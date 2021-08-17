"""
Assigns new numerical labels from 0 to n to (n+1) species to files in \
    '/mnt/sda/MLDSP-samples-r202/dm_species'. The new label assignment map \
        (name -> number) is stored in '/home/w328li/DeepMicrobes/data/name2label_gtdb_species_r202.txt

No command line arguments are required.
"""

from Bio import SeqIO
import os 

label = 0
dir = '/mnt/sda/MLDSP-samples-r202/dm_species'
name2label_path = '/home/w328li/DeepMicrobes/data/name2label_gtdb_species_r202.txt'

for file in os.listdir(dir):
    if file.endswith('.fa') and file.startswith('label_'):
        index = file[:-3]
        print("label is:", label)
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(dir, file)),'fasta')
        for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            out_file= open(os.path.join(dir, index+'_new.fa'), mode)
            out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
            out_file.write(sequence+"\n")
            out_file.close()
            mode = 'a'
        label += 1
    if file.endswith('.fna'):
        index = file[:-4]
        print("label is:", label)
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(dir, file)),'fasta')
        for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            out_file= open(os.path.join(dir, index+'_new.fa'), mode)
            out_file.write("> label|"+str(label)+"|"+id+"\n")
            out_file.write(sequence+"\n")
            out_file.close()
            mode = 'a'
        label += 1      
        print("done", file)

visited = []
for file in os.listdir(dir):
    if file.endswith('_combined_new_trimmed.fa'):
        visited.append(file.split('_combined_new_trimmed.fa')[0])
if not os.path.exists(name2label_path):
    name2label_file = open(name2label_path, mode='w')
    for v in visited:
        name2label_file.write(v+'\t'+str(visited.index(v))+'\n')