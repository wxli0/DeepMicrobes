import sys
import os
import pandas as pd

df = pd.read_csv("/home/w328li/MLDSP/samples/Table_S2.csv", skiprows=0, header=1, index_col=0)
for index, row in df.iterrows():
	if row['Genus (reference)'] == 'Unassigned':
		print("skip", index)
		continue
	print("======================= start", index, "=======================")
	prefix = "even_"+index
	forward_file = prefix+"_1.fa"
	reverse_file = prefix+"_2.fa"
	tfrec_file = prefix+".tfrec"
	result_file = prefix+".result.txt"
	profile_file = prefix+".profile.txt"
	profile_0_file = prefix+".0_profile.txt"
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_0_file+" \
		-t 0 \
		-l /home/w328li/DeepMicrobes/data/name2label_genus.txt")
	print("======================= done", prefix, "=======================")
	