import os 
import sys 
from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/HGR_train.fa"),'fasta') 
lens = []
for fasta in fasta_sequences:
    id, seq = fasta.id, str(fasta.seq)
    lens.append(len(seq))

plt.hist(lens)
plt.savefig("/home/w328li/DeepMicrobes/results/lens_hist.png")