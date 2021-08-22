"""
Not in use
"""

import os 
from os.path import expanduser
from Bio import SeqIO


len_dict = {}
label_dict = {}
label = 0
mode = 'w'
home = expanduser("~")
for file in os.listdir('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/'):
    if file.startswith('label_') and file.endswith('.fa'):
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            frag_id = id.split('|')[4]
            len_dict[frag_id] = len(seq)
        used = False
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            frag_id = id.split('|')[4]
            if len(seq) <= 50000:
                continue
            label_dict[frag_id] = label
            used = True
        if used:
            output_file_path = os.path.join(home, "DeepMicrobes/data/name2label_pruned_genus.txt")
            out_file= open(output_file_path, mode)
            out_file.write(file[6:-3]+'\t'+str(label)+'\n')
            label += 1
            mode = 'a'
            out_file.close()

print("end label is:", label)



# fasta_sequences = SeqIO.parse(open('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/trimmed_150_var/HGR_var_train.fa'), 'fasta')
# mode = 'w'
# for fasta in fasta_sequences:
#     id, seq = fasta.id, str(fasta.seq)
#     frag_id = id.split('|')[4]
#     if len_dict[frag_id] <= 50000:
#         continue

#     out_file= open(os.path.join('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/trimmed_150_var/HGR_pruned_var_train.fa'), mode)
#     label = label_dict[frag_id]
#     out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
#     out_file.write(seq+"\n")
#     out_file.close()
#     mode = 'a'

