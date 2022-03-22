import config
import sys
import os 
import shutil
import glob

label_dir = 'file2label/'
name_dir = 'name2label/'
DM_path = config.DM_path

# nested folder generated by prep_DM_HGR.py, with the following structure
# - folder
#   - species 1
#       - species 1 file 1
#   - species 2
#       - species 2 file 1
#       - species 2 file 2

###############################

# # for Task 1 provided
# src = 'HGR_species_folder' 
# dest = 'HGR_species'

# data_path = config.DM_data_path

###############################

# # for Task 2 with 3355 classes
data_path = config.MLDSP_data_path
# src = 'GTDB_subset_representative_folder' 
# dest = 'GTDB_subset_representative'

# # for Task 2 with 601 classes
# src = 'GTDB_small_representative_folder' 
# dest = 'GTDB_small_representative'

# for Task 2 with 34 classes
src = 'GTDB_mini_folder' 
dest = 'GTDB_mini'

# # for Task 3 with 4 classes
# src = 'Task3_g__Methanobrevibacter_B_folder' 
# dest = 'Task3_g__Methanobrevibacter_B'

# data_path = config.DM_data_path

###############################

# make dest folder
if not os.path.exists(os.path.join(data_path, dest)):
    os.mkdir(os.path.join(data_path, dest))

# concatenate all files in subdir to _combined.fna
empty_class = []
for subdir in os.listdir(os.path.join(data_path, src)):
    if len(os.listdir(os.path.join(data_path, src, subdir))) != 0: # the folder is not empty
        with open(os.path.join(data_path, dest, subdir+".fa"), 'wb') as outfile:
            for filename in \
                (glob.glob(data_path+"/"+src+'/'+subdir+'/*.fa')+ \
                    glob.glob(data_path+"/"+src+'/'+subdir+'/*.fna') + \
                        glob.glob(data_path+"/"+src+'/'+subdir+'/*.fasta')):
                with open(filename, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)
    else:
        empty_class.append(subdir)
print("empty_class is:", empty_class)

# generate label_{dir}.txt
label_id = 0
with open(os.path.join(DM_path,label_dir, dest+".txt"), 'w') as f:
    for fna_file in os.listdir(os.path.join(data_path, dest)):
        f.write(fna_file+"\t"+str(label_id)+"\n")
        label_id += 1

# generate name2label_{dir}.txt
label_id=0
with open(os.path.join(DM_path, "name2label", dest+".txt"), "w") as f:
    for fna_file in os.listdir(os.path.join(data_path, dest)):
        if fna_file.endswith('.fa'):
            cur_class = fna_file[:-3]
        elif fna_file.endswith('.fna'):
            cur_class = fna_file[:-4]
        elif fna_file.endswith('.fasta'):
            cur_class = fna_file[:-6]
        f.write(cur_class+"\t"+str(label_id)+"\n")
        label_id += 1
