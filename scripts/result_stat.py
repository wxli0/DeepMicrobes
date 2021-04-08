import os 
import sys 
import pandas as pd 

# read tab-deliminated file
def read_profile(file):
    with open(file) as fin:
        rows = ( line.split('\t') for line in fin )
        d = { row[0]:row[1] for row in rows }
        return d


df = pd.read_csv("/home/w328li/MLDSP/samples/Table_S2.csv", skiprows=0, header=1, index_col=0)
dir = "/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_results/"
for profile_0 in os.listdir(dir):
    if profile_0.endswith('0_profile.txt'):
        # construct propfile_0_dict
        prefix = profile_0[:-14]    
        index = prefix[5:]
        profile_0_dict = read_profile(dir+profile_0)
        true_label = df.loc[index]['Genus (reference)']
        recall = 0
        if true_label in profile_0_dict:
            recall = profile_0_dict[true_label]/sum(profile_0_dict.values())
        
        # construct profile_50_dict
        profile_50 = prefix+'.profile.txt'
        profile_50_dict = read_profile(dir+profile_50)
        precision = 0
        if true_label in profile_50_dict:
            precision = profile_50_dict[true_label]/sum(profile_50_dict.values())
        print("====", prefix, "true_label:", true_label, "precision:", precision, "recall:", recall)

