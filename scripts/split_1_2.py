import os 
import sys 
from Bio import SeqIO


dir = sys.argv[1]

for file in os.listdir(dir):
    if file.endswith('.fa'):
        mode = 'w'
        fasta_sequences = SeqIO.parse(open(dir+'/'+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            forward_path = dir+"/"+file[:-3]+"_1"+".fa"
            reverse_path = dir+"/"+file[:-3]+"_2"+".fa"
            forward_file = open(forward_path, mode)
            reverse_file = open(reverse_path, mode)
            if id.endswith('/1'):
                forward_file.write(">"+id + "\n")
                forward_file.write(seq+"\n")
            elif id.endswith('/2'):
                reverse_file.write(">"+id + "\n")
                reverse_file.write(seq+"\n")
            mode = 'a'