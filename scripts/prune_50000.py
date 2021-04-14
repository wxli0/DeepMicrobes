import sys 
import os 
from Bio import SeqIO

dir = '/mnt/sda/DeepMicrobes-data/labeled_genome_genus'
dir_pruned = dir+"_pruned"
os.mkdir(dir_pruned)
for file in os.listdir(dir):
    if file.endswith('.fa'):
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(os.path.join(dir, file)),'fasta')
        for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            if len(sequence) > 50000:
                out_file= open(os.path.join(dir_pruned, file), mode)
                out_file.write(">"+id+"\n")
                out_file.write(sequence+"\n")
                out_file.close()
                mode = 'a'
        print("done", file)
