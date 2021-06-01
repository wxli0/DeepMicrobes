import os 
import sys
from Bio import SeqIO


dir = '/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_full/'

for file in os.listdir(dir):
    index = 0
    fasta_sequences = SeqIO.parse(open(dir+file),'fasta') 
    os.remove(dir+file)
    output_file_path = dir+file
    out_file= open(output_file_path, 'w')
    counter = 0
    for fasta in fasta_sequences:
        id, seq = fasta.id, str(fasta.seq)
        out_file.write(">"+id +"_"+str(index)+ "\n")
        out_file.write(seq+"\n")
        index += 1
        out_file.close()
