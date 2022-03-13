"""
Ramdom trims training or test dataset files in a directory using ART simulator

No command line arguments are required
"""

import config
import os

###### For training ########
# task = "labeled_genome_train_species_reads" # for Task 1 in DeepMicrobes
# task = "HGR_species_label_reads" # for Task 1 (sparse)

###### For test ########
task = "mag_reads_150bp_1w_split" # for Task 1 in DeepMicrobes

dir = os.path.join(config.DM_data_path, task)

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
