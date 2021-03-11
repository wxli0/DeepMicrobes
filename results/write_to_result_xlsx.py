import os 
import sys
import pandas as pd 

df = pd.read_csv("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_results.csv", header=0, index_col=0)
cat_file = open("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_combined_trimed.category_paired.txt", "r")
cats = cat_file.read().split('\n')

name2label_file = open("/Users/wanxinli/Desktop/project/DeepMicrobes/data/name2label_dm_full.txt", "r")
name2label_list = name2label_file.read().split('\n')
name2label_dict = {}
for pair in name2label_list:
    name = pair.split('\t')[0]
    label = pair.split('\t')[1]
    name2label_dict[label] = name

classes = []
for cat in cats:
    classes.append(name2label_dict[cat])

prob_file = open("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_combined_trimed.prob_paired.txt", "r")
probs = prob_file.read().split('\n')
probs = [float(x)/100 for x in probs]

df['classification'] = classes
df['confidence'] = probs
df = df.reindex(sorted(df.index, key=lambda x: x[-6:-3]))
print(df)

df.to_csv("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_results.csv", header=True, index=True)