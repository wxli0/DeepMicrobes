"""
Splits file in a directiry (sys.argv[1]) containing multiple sequences into \
    mutiple files containing one sequence. The sequences are disgarded \
        if the length is < 5000. Prepares Task 1 (simulated/sparse) training dataset.

:param sys.argv[1]: dir. Target directory
:type sys.argv[1]: str
"""

from Bio import SeqIO
import os 
import sys 

dir = sys.argv[1]
dir_split = dir+"_split_pruned"
os.mkdir(dir_split)
for sub_dir in os.listdir(dir):
    os.mkdir(os.path.join(dir_split, sub_dir))
    for file in os.listdir(os.path.join(dir, sub_dir)):
        file_short = file
        if file.endswith('.fa'):
            file_short = file[:-3]
        elif file.endswith('.fasta'):
            file_short = file[:-6]
        fasta_sequences = SeqIO.parse(open(os.path.join(dir, sub_dir, file)),'fasta')
        i = 0
        for fasta in fasta_sequences:
            id, sequence = fasta.id, str(fasta.seq) 
            if len(sequence) > 5000:
                out_file= open(os.path.join(dir_split, sub_dir, file_short+"_"+str(i)+".fasta"), 'w')
                out_file.write(">"+id+"\n")
                out_file.write(sequence+"\n")
                out_file.close()
                i += 1
