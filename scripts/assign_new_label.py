import sys 
import os 
from Bio import SeqIO

label = 0
dir = '/mnt/sda/MLDSP-samples-r202/dm_species'
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