import sys
import os 
import shutil
import glob

dir = sys.argv[1]
combined_dir = dir+"_combined/"
dest_dir = dir+"_w_label_trimed/"
label_dir = 'label_files/'

base_path = "/home/w328li/DeepMicrobes/"

# remove combined_dir if exists
if os.path.isdir(base_path+combined_dir):
    shutil.rmtree(base_path+combined_dir)
os.mkdir(base_path+combined_dir)

# concatenate all files in subdir to _combined.fna
for subdir in os.listdir(base_path+dir):
    with open(base_path+combined_dir+subdir+"_combined.fna", 'wb') as outfile:
        print("pattern is:", base_path+dir+subdir+'/*.fna')
        for filename in glob.glob(base_path+dir+subdir+'/*.fna'):
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)

# remove label_{dir}.txt if exists
if os.path.isdir(base_path+label_dir+"label_"+dir+".txt"):
    shutil.rmtree(base_path+label_dir+"label_"+dir+".txt")

# generate label_{dir}.txt
label_id = 0
with open(base_path+label_dir+"label_"+dir+".txt", 'w') as f:
    for fna_file in os.listdir(base_path+combined_dir):
        f.write(fna_file+"\t"+str(label_id)+"\n")
        label_id += 1

# remove name2label_{dir}.txt if exists
if os.path.isdir(base_path+"data/name2label_"+dir+".txt"):
    shutil.rmtree(base_path+"data/name2label_"+dir+".txt")

# generate name2label_{dir}.txt
with open(base_path+"data/name2label_"+dir+".txt", "w") as f:
    for subdir in os.listdir(base_path+dir):
        f.write(subdir+"\t"+str(label_id)+"\n")
        label_id += 1
