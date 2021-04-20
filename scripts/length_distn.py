import os 
import sys 
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

lens = []
for file in os.listdir('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/'):
    if file.startswith('label_') and file.endswith('.fa'):
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            lens.append(len(seq))

print(lens)
binwidth = 1000
bins = np.arange(min(lens), max(lens) + binwidth, binwidth)
counts, edges, plot = plt.hist(lens, bins=bins, density=True)
for i in range(len(bins)):
    print(bins[i]+":", counts[i])
plt.savefig("/home/w328li/DeepMicrobes/results/lens_hist.png")