import os

dir = '/mnt/sda/DeepMicrobes-data/HGR_species_label_reads'

for file in os.listdir(dir):
    if file.endswith('_trimmed.fq'):
        os.system("mv "+ "'" + file +"'" + " " + "'" + file[:-2] +"fa" + "'")