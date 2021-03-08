import sys
import os 
import shutil
import glob

dir = sys.argv[1]
combine_dir = dir+"_combined/"
dest_dir = dir+"_w_label_trimed/"
label_dir = 'label_files/'

base_path = "/home/w328li/DeepMicrobes/"

# remove combined_dir if exists
if os.path.isdir(base_path+combine_dir):
    os.rmdir(base_path+combine_dir)

# concatenate all files in subdir to _combined.fna
for subdir in os.listdir(base_path+dir):
    with open(base_path+combine_dir+subdir+"_combined.fna", 'wb') as outfile:
        for filename in glob.glob(base_path+dir+subdir+'/*.fna'):
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)

# # generate label_{dir}.txt
# label_id = 0
# with open(base_path+label_dir, 'w') as f:
#     for subdir in os.listdir(base_path+dir):
#         f.write(subdir+"\t"+str(label_id)+"\n")
#         label_id += 1

# # execute fna_label.py

# os.system("fna_label.py -m"+base_path+dest_dir+'/label_'+dir+'.txt'+"-o output_dir")


# 
