import os
import sys
import pandas as pd

df = pd.read_csv("/home/w328li/MLDSP/samples/Table_S2.csv", skiprows=0, header=1, index_col=0)
for index, row in df.iterrows():
    print("======================= start", index, "=======================")
    prefix = "even_"+index
    forward_file = prefix+"_1.fa"
    reverse_file = prefix+"_2.fa"
    tfrec_file = prefix+".tfrec"
    os.system("tfrec_predict_kmer.sh \
        -f /mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000/"+forward_file+" \
        -r /mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000/"+reverse_file+" \
        -t fasta \
        -v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
        -o "+prefix+" \
        -s 4000000 \
        -k 12")