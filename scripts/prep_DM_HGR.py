import os
import pandas as pd
from shutil import copyfile

gtdbtk_path = "~/DeepMicrobes/file2label/gtdbtk.bac120.summary.tsv"
gtdbtk_res = pd.read_csv(gtdbtk_path, sep='\t', header = 0)
output_dir = "/mnt/sda/DeepMicrobes-data/HGR_species_folder"
src = "/mnt/sda/DeepMicrobes-data/labeled_genome_original"

# making folders containing species files
all_species = []
for index, row in gtdbtk_res.iterrows():
    cur_species = row['classification'].split(';')[-1]
    all_species.append(cur_species)
    genome = row['user_genome']
    if not os.path.exists(os.path.join(output_dir, cur_species)):
        os.mkdir(os.path.join(output_dir, cur_species))
    copyfile(os.path.join(src, genome+".fa"), \
        os.path.join(output_dir, cur_species, genome+".fa"))

# making a flat folder containing all concatenated species files
print("is s__ in all_species?", 's__' in all_species)
print("number of all_species", len(list(set(all_species))))