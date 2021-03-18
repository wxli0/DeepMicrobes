import os 
import sys 
from Bio import SeqIO

base_path = "/home/w328li/DeepMicrobes/"
dir = sys.argv[1]
input_path = base_path+dir+"/"
output_path = base_path+dir+"_w_label/"

if os.path.isdir(output_path):
    os.rmdir(output_path)
os.mkdir(output_path)

for file in os.listdir(input_path):
    fasta_sequences = SeqIO.parse(open(input_path+'/'+file),'fasta') 
    file_name = file.split("_trimed", 1)[1]
    output_file_path = output_path+"/"+file_name
    out_file= open(output_file_path, 'w')
    counter = 0
    for fasta in fasta_sequences:
        id, seq = fasta.id, str(fasta.seq)
        out_file.write(">"+id +"|" + file_name + "\n")
        out_file.write(seq+"\n")
    out_file.close()