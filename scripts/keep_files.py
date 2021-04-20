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
            len_dict[frag_id] = len(seq)

label_dict = {}
label = 0
for file in os.listdir('/mnt/sda/DeepMicrobes-data/labeled_genome_genus_pruned'):
    if file.endswith('.fa') and file.startswith('label_'):
        fasta_sequences = SeqIO.parse(open("/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"+file),'fasta') 
        for fasta in fasta_sequences:
            id, seq = fasta.id, str(fasta.seq)
            label_dict[frag_id] = label
        label += 1
print("end label is:", label)



fasta_sequences = SeqIO.parse(open('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/trimmed_150_var/HGR_var_train.fa'), 'fasta')
mode = 'w'
for fasta in fasta_sequences:
    id, seq = fasta.id, str(fasta.seq)
    frag_id = id.split('|')[4]
    if len_dict[frag_id] <= 50000:
        continue

    out_file= open(os.path.join('/mnt/sda/DeepMicrobes-data/labeled_genome_genus/trimmed_150_var/HGR_pruned_var_train.fa'), mode)
    label = label_dict[frag_id]
    out_file.write("> label|"+str(label)+"|"+"|".join(id.split("|", 2)[2:])+"\n")
    out_file.write(seq+"\n")
    out_file.close()
    mode = 'a'

