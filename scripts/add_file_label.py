import os 
import sys 
from Bio import SeqIO

base_path = "/home/w328li/DeepMicrobes/"
dir = sys.argv[1]
input_path = base_path+dir+"/"
output_path = base_path+dir+"w_label/"

if os.path.isdir(output_path):
    os.rmdir(output_path)
os.mkdir(output_path)

for file in os.listdir(input_path):
    fasta_sequences = SeqIO.parse(open(input_path+'/'+file),'fasta') 
    output_file_path = output_path+"/"+file
    out_file= open(output_file_path, 'w')
    counter = 0
    for fasta in fasta_sequences:
        id, seq = fasta.id, str(fasta.seq)
        out_file.write(">"+id +"|" + file + "\n")
        out_file.write(seq+"\n")
    out_file.close()