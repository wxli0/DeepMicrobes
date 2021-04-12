import os 
import sys 
import pandas as pd 
import platform
import math 
import shutil

S1_path = "/Users/wanxinli/Desktop/project.nosync/MLDSP-desktop/samples/Table_S1.csv"
if platform.node() == 'tml3':
    S1_path = "~/MLDSP-desktop/samples/Table_S1.csv"
S1 = pd.read_csv(S1_path, index_col=0, header=1, dtype = str)
print(S1['Genus'])

S1_na = S1[S1['Genus'].notnull()]
src = '/mnt/sda/DeepMicrobes-data/labeled_genome/'
dest = '/mnt/sda/DeepMicrobes-data/labeled_genome_no_na/'
for index, row in S1_na.iterrows():
    file = 'label_'+index+'.fa'
    shutil.copyfile(src+file, dest+file)
