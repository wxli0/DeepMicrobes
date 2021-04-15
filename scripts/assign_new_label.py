import sys 
import os 
from Bio import SeqIO

label = 0
dir = '/mnt/sda/DeepMicrobes-data/labeled_genome_genus_pruned'
for file in os.listdir(dir):
    if file.endswith('.fa'):
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(dir, file)),'fasta')
        for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            out_file= open(os.path.join(dir, file[:-3]+'_new.fa'), mode)
            out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
            out_file.write(sequence+"\n")
            out_file.close()
            mode = 'a'
        label += 1
        print("done", file)