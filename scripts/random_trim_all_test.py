"""
Ramdom trims test dataset files in a directory using ART simulator

No command line arguments are required
"""

import os


dir = "rumen_mags"
base_path = "/home/w328li/DeepMicrobes/"
label_dir = base_path+dir+"/"

# random_trim all files in label_dir, assume file ends with .fa
for file in os.listdir(label_dir):
    input_file = label_dir+file
    # trim from 3' and 5'
    forward_file = label_dir+file[:-3]+"_1.fa"
    reverse_file = label_dir+file[:-3]+"_2.fa"
    os.system("random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + forward_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r False")
    print("done random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + forward_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r False")
    os.system("random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + reverse_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r True")
    print("done random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + reverse_file+ "'" + " -f fasta -l 150 -min 0 -max 0 -r True")
