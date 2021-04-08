import os 
import sys 
from Bio import SeqIO


dir = sys.argv[1]

for forward_file in os.listdir(dir):
    if forward_file.endswith('1.fa'):
        reverse_path = dir+"/"+forward_file[:-4]+"2"+".fa"
        forward_path = dir+forward_file
        output_path = dir+"/"+forward_file[:-4]+"fa"

        data_forward = data_reverse = ""
        with open(forward_path) as fp:
            data_forward = fp.read()
        
        # Reading data from file2
        with open(reverse_path) as fp:
            data_reverse = fp.read()
        
        data_forward += "\n"
        data_forward += data_reverse

        with open (output_path, 'w') as fp:
            fp.write(data_forward)

        print(forward_file, "done")