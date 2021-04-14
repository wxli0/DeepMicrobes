import os
import sys
import shutil

dir = "/mnt/sda/DeepMicrobes-data/labeled_genome_genus/"

# random_trim all files in label_dir, assume file ends with .fa
for file in os.listdir(dir):
    if file.endswith('.fa'):
        input_file = dir+file
        # trim from 3' and 5'
        output_file = dir+file[:-3]+"_trimmed.fa"
        os.system("random_trim.py -i " + "'"+ input_file + "'" \
            + " -o " + "'" + output_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r False")
        print("done random_trim.py -i " + "'"+ input_file + "'" \
            + " -o " + "'" + output_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r False")
