# get the precision and recall for DeepMicrobes precision, recall, and incorrect rate
# for MLDSP and HGR prediction

import os
import pandas as pd

paths = ['/home/w328li/BlindKameris-new/outputs-r202/MLDSP-prediction-full-path.csv',\
    '/home/w328li/BlindKameris-new/outputs-HGR-r202/HGR-prediction-full-path.csv']


def readin_dict(prof_path):
    file = open(prof_path, 'r')
    lines = file.readlines()
    
    # construct profile dictionary prof_dict
    prof_dict = {}
    for line in lines:
        pair = line.split('\t')
        prof_dict[pair[0]] = int(pair[1])
    return prof_dict



def calc_pr(df_path, res_path):
    total = 0
    correct = 0
    rejected = 0
    df = pd.read_csv(df_path, index_col=0, header=0, dtype = str)

    for res in os.listdir(res_path):
        prof_dict = {}
        prof_0_dict = {}
        if res.endswith('.profile.txt'):
            prof_dict = readin_dict(os.path.join(res_path, res))
            index = res.split('.profile.txt')[0]
            prof_0_dict = readin_dict(os.path.join(res_path, index+'.0_profile.txt'))
            total += sum(prof_0_dict.values())
            rejected += sum(prof_0_dict.values())-sum(prof_dict.values())
            label = ''
            if index in df.index:
                label = df.loc[index]['gtdb-tk-species']
            else:
                index_new = index+'.fa'
                label = df.loc[index_new]['gtdb-tk-species']
            if label in prof_0_dict:
                correct += prof_0_dict[label]
    print(total)
    print(correct)
    print(rejected)
    precision = correct/(total-rejected)
    recall = correct/total
    incorrect = (total-correct-rejected)/total
    
    return precision, recall, incorrect

path1 = '/home/w328li/BlindKameris-new/outputs-r202/MLDSP-prediction-full-path.csv'
res_path1 = '/mnt/sda/DeepMicrobes-data/rumen_mags'
precision, recall, incorrect = calc_pr(path1, res_path1)
print("precision is:", precision)
print("recall is:", recall)
print("incorrect rate is:", incorrect)

path2 = '/home/w328li/BlindKameris-new/outputs-HGR-r202/HGR-prediction-full-path.csv'
res_path2 = '/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_results'
precision, recall, incorrect = calc_pr(path2, res_path2)
print("precision is:", precision)
print("recall is:", recall)
print("incorrect rate is:", incorrect)




