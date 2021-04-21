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

print("minimum length:", min(lens))
print("maximum length:", max(lens))
binwidth = 5000
bins = np.arange(0, max(lens) + binwidth, binwidth)
counts, edges, plot = plt.hist(lens, bins=bins, density=True)
plt.xlabel('length of training sequences')
plt.ylabel('frequencies')
plt.title('histogram of lengths of training sequencs')
for i in range(len(bins)-1):
    if counts[i] != 0:
        print("["+str(bins[i])+","+str(bins[i+1])+ "]:", counts[i])
plt.savefig("/home/w328li/DeepMicrobes/results/lens_hist.png")