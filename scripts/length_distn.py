import os 
import sys 
from Bio import SeqIO
import matplotlib.pyplot as plt

lens = []
for file in os.listdir('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/'):
    if file.startswith('label_') and file.endswith('.fa'):
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            lens.append(len(seq))

print(lens)
plt.hist(lens)
plt.savefig("/home/w328li/DeepMicrobes/results/lens_hist.png")