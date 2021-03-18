import os
import sys
import shutil

dir = sys.argv[1]
base_path = "/home/w328li/DeepMicrobes/"
label_dir = base_path+dir+"/"
trimed_dir = base_path+dir+"_trimed/"

if os.path.isdir(trimed_dir):
    shutil.rmtree(trimed_dir)
os.mkdir(trimed_dir)

# random_trim all files in label_dir
for file in os.listdir(label_dir):
    input_file = label_dir+file
    output_file = trimed_dir+"trimed_"+file
    os.system("random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + output_file+ "'" + " -f fasta -l 150 -min 0 -max 75")
    print("done random_trim.py -i " + "'"+ input_file + "'" \
        + " -o " + "'" + output_file+ "'" + " -f fasta -l 150 -min 0 -max 75")
