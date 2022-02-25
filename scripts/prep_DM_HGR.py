import os
import pandas as pd
from shutil import copyfile

gtdbtk_path = "~/DeepMicrobes/label_files/gtdbtk.bac120.summary.tsv"
gtdbtk_res = pd.read_excel(gtdbtk_path, index_col=0, header=0, sheet_name="gtdbtk.bac120.summary")
output_dir = "/mnt/sda/DeepMicrobes-data/HGR_species_folder"
src = "/mnt/sda/DeepMicrobes-data/labeled_genome_original"

for index, row in gtdbtk_res.iterrows():
    cur_species = row['classification'].split(';')[-1]
    genome = row['user_genome']
    if not os.path.exists(os.path.join(output_dir, cur_species)):
        os.mkdir(os.path.join(output_dir, cur_species))
    copyfile(os.path.join(src, genome+".fa"), \
        os.path.join(output_dir, cur_species, genome+".fa"))

