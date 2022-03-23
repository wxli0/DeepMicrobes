"""
Generate a bash script for Task 2 of the commands to ART simulate reads for all files in a folder 
Example bash command for ART simulation: art_illumina --noALN -ss HS25 -i label_11861_6_63.fa -p -o art_11861_6_63. -l 150 -f 9.275772424 -m 200 -s 10 -rs 11

Run within ~/DeepMicrobes/scripts

Example:
    python3 ~/DeepMicrobes/scripts/gen_art_sim_file.py (with seed 11)
    python3 ~/DeepMicrobes/scripts/gen_art_sim_file.py --seed=1
"""

# Task 2
file_folder = "/mnt/sda/MLDSP-samples-r202/GTDB_small_label"
out_prefix = "auto_art_Task2_small"

# # Task 2 with 34 species
# file_folder = "/mnt/sda/MLDSP-samples-r202/GTDB_mini_label"
# out_prefix = "auto_art_Task2_mini"

# # Task 2 (test)
# file_folder = "/mnt/sda/DeepMicrobes-data/rumen_mags_Task2"
# out_prefix = "auto_art_Task2_test"

# # Task 3 (training)
# file_folder = "/mnt/sda/DeepMicrobes-data/Task3_g__Methanobrevibacter_B_label"
# out_prefix = "auto_art_Task3"

# # Task 3 (test)
# file_folder = "/mnt/sda/DeepMicrobes-data/rumen_mags_Task3"
# out_prefix = "auto_art_Task3_test"

import argparse
from Bio import SeqIO
import os

parser = argparse.ArgumentParser()
parser.add_argument('--seed',  default = 11, type=int, help='seed number')
args = parser.parse_args()
seed = args.seed

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

# sim_num = 10000 # for test, and train
sim_num = 100000 # for train (large)
sim_len = 150

out_file = out_prefix+"_"+str(seed)+".sh"
if os.path.exists(out_file):
    os.remove(out_file)
for file in os.listdir(file_folder):
    cur_genome_size = genome_size(os.path.join(file_folder, file))
    coverage = sim_num*2*sim_len/cur_genome_size
    id_wout_label = ""
    if file.startswith('label_') and file.endswith('.fa'):
        id_wout_label = file[6:-2] # file starts with label_, ends with fa
    elif file.endswith('.fa'):
        id_wout_label = file[:-2]
    if file.endswith('.fasta'):
        id_wout_label = file[:-5]
    with open(out_file, 'a') as the_file:
        the_file.write(\
            "art_illumina --noALN -ss HS25 -i '" \
                + file + "' -p -o 'art_" + id_wout_label \
                    + "' -l 150 -f " + str(coverage) + " -m 200 -s 10 -rs " + str(seed) + "\n")

