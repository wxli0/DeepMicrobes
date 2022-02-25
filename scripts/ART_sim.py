# use ART simulator on tml3 to simulate reads for DeepMicrobes

import config
import os

data_path = config.DM_data_path
# for Task 1 (sparse)
task_folder = "HGR_species" 
dest_folder = "HGR_species_reads"

src = os.path.join(data_path, task_folder) 
dest = os.path.join(data_path, dest_folder) 

if not os.path.exists(dest):
    os.mkdir(dest)

for fasta_file in os.listdir(src):
    genome = None
    print(fasta_file)
    if fasta_file.endswith('.fa'):
        genome = fasta_file[:-3]
    os.system("~/DeepMicrobes/art_bin_MountRainier/art_illumina -ss HS25  -i " \
            + "'"+os.path.join(src, fasta_file)+"'" + " -p -na -l 150 -f 2 -m 400  -s 50 -o "+"'"+os.path.join(dest, genome)+"'")
    print("============= completed " + fasta_file + "=============")

