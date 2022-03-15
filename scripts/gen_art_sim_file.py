"""
Generate a bash script for Task 2 of the commands to ART simulate reads for all files in a folder 
Example bash command for ART simulation: art_illumina --noALN -ss HS25 -i label_11861_6_63.fa -p -o art_11861_6_63. -l 150 -f 9.275772424 -m 200 -s 10 -rs 11
"""

from Bio import SeqIO
import os

def genome_size(data_path):
    """
    Calculates the genome size of the fasta file in data_path
    """
    genome_size = 0

    fasta_sequences = SeqIO.parse(open(data_path),'fasta') 
    for fasta in fasta_sequences:
        _, sequence = fasta.id, str(fasta.seq)
        genome_size += len(sequence)
    return genome_size

file_folder = "/mnt/sda/MLDSP-samples-r202/GTDB_subset_representative"
sim_num = 10000
sim_len = 150
for file in os.listdir(file_folder):
    cur_genome_size = genome_size(os.path.join(file_folder, file))
    coverage = sim_num*2*sim_len/cur_genome_size
    id_wout_label = file[6:-2] # file starts with label_, ends with fa
    with open('auto_art_Task2.sh', 'a') as the_file:
        the_file.write(\
            "art_illumina --noALN -ss HS25 -i " \
                + file + " -p -o art_" + id_wout_label \
                    + " -l 150 -f " + str(coverage) + " -m 200 -s 10 -rs 11\n")

