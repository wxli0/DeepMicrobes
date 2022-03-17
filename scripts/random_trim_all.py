"""
Ramdom trims training or test dataset files in a directory using ART simulator

No command line arguments are required
"""

import config
import os

###### For Task 1 ########
# task = "labeled_genome_train_species_reads_author" # for Task 1 read simulation provided by the author (training)
# task = "HGR_species_label_reads" # for Task 1 (sparse) (training)
# task = "mag_reads_150bp_1w_split" # for Task 1  (testing)

# base_path = config.DM_data_path

###### For Task 2 ########
# task = "GTDB_subset_representative_label_reads" # for Task 2 (dense) (training) with 3355 classes
# task = "GTDB_small_representative_label_reads" # for Task 2 (dense) (training) with 601 classes with seed 11
# task = "GTDB_small_representative_1_label_reads" # for Task 2 (dense) (training) with 601 classes with seed 1
# base_path = config.MLDSP_data_path


###### For Task 3 ########
base_path = config.DM_data_path

# training
# task = "Task3_g__Methanobrevibacter_B_label_reads_seed_1" # for Task 2 (dense) (training) with 601 classes with seed 1

# testing 
task = "rumen_mags_Task3" # for Task 2 (dense) (training) with 601 classes with seed 1

dir = os.path.join(base_path, task)

# random_trim all files in label_dir, assume file ends with .fa
for file in os.listdir(dir):
    identifier = None
    type = None
    suffix = None
    if file.endswith('.fq'):
        identifier = file[:-3]
        type = "fastq"
    elif file.endswith('.fa'):
        identifier = file[:-3]
        type = "fasta"
    input_file = os.path.join(dir, file)
    # trim from 3' and 5'
    output_file = os.path.join(dir, identifier+"_trimmed.fa")
    os.system("random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + output_file+ "'" + " -f "+ type + " -l 150 -min 0 -max 75")
    print("done random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + output_file+ "'" + " -f "+ type + " -l 150 -min 0 -max 75")
