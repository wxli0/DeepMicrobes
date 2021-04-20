import os 
import sys
from Bio import SeqIO

len_dict = {}
for file in os.listdir('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/'):
    if file.startswith('label_') and file.endswith('.fa'):
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            frag_id = id.split('|')[4]
            if frag_id in len_dict:
                print(frag_id)
            len_dict[frag_id] = len(str(seq))

