import os 
import sys
import pandas as pd 

dir = sys.argv[1]
label_file = sys.argv[2]

df = pd.read_csv("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_results.csv", header=0, index_col=0)
reversed_index = sorted(list(df.index), key=str.casefold)
cat_file = open("/Users/wanxinli/Desktop/project/DeepMicrobes/results/"+dir+".category_paired.txt", "r")
cats = cat_file.read().split('\n')

name2label_file = open(label_file, "r")
name2label_list = name2label_file.read().split('\n')
name2label_dict = {}
for pair in name2label_list:
    print(pair)
    name = pair.split('\t')[0]
    label = pair.split('\t')[1]
    if name.endswith('_combined'):
        name = name[:-9]
    if name.endswith('_combined.fna'):
        name = name[:-13]
    name2label_dict[label] = name

classes = []
for cat in cats:
    classes.append(name2label_dict[cat])

prob_file = open("/Users/wanxinli/Desktop/project/DeepMicrobes/results/"+dir+".prob_paired.txt", "r")
probs = prob_file.read().split('\n')
probs = [float(x)/100 for x in probs]

df_new = pd.DataFrame()
df_new['id'] = reversed_index
df_new[dir+'-classification'] = classes
df_new[dir+'-confidence'] = probs
df_new = df_new.set_index(['id'])
df_new = df_new.reindex(sorted(df.index, key=lambda x: x[-6:-3]))
print(df_new)

df[dir+'-classification'] = df_new[dir+'-classification']
df[dir+'-confidence'] = df_new[dir+'-confidence']
print(df)

df.to_csv("/Users/wanxinli/Desktop/project/DeepMicrobes/results/rumen_mags_results.csv", header=True, index=True)