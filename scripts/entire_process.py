import sys
import os
import pd 

df = pd.read_csv("/home/w328li/MLDSP/samples/Table_S2.csv", skiprows=0, header=1, index=0)
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
	os.system("tfrec_predict_kmer.sh \
		-f /mnt/sda/DeepMicrobes-data/"+forward_file+" \
		-r /mnt/sda/DeepMicrobes-data/"+reverse_file+" \
		-t fasta \
		-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
		-o "+prefix+" \
		-s 4000000 \
		-k 12")
	os.system("predict_DeepMicrobes.sh \
		-i "+tfrec_file+" \
		-b 8192 \
		-l genus \
		-p 8 \
		-m /mnt/sda/DeepMicrobes-data/weights_genus \
		-o "+prefix)
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_file+" \
		-t 50 \
		-l /home/w328li/DeepMicrobes/data/name2label_genus.txt")
	print("======================= done", prefix, "=======================")
	