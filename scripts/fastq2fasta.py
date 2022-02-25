# convert fastq files in a directory to fasta files

import config
import os

task = "HGR_species_label_reads"
dest = os.path.join(config.DM_data_path, task)

for fastq_file in os.listdir(dest):
    os.system("os.sed -n '1~4s/^@/>/p;2~4p' "+ "'" + fastq_file + "'" + " > "+ "'" + fastq_file[:-2]+"fa" + "'")
    print("done", fastq_file)