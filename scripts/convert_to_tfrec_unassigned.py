import os
from os.path import expanduser
import pandas as pd

home = expanduser("~")
S2_path = os.path.join(home, "MLDSP/samples/Table_S2.csv")
df = pd.read_csv(S2_path, skiprows=0, header=1, index_col=0)
for index, row in df.iterrows():
    if row['Genus (reference)'] != 'Unassigned':
        print("skip", index)
        continue
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