"""
runs the TFRecord convertino, prediction, profiling for Task 1 in DeepMicrobes, using their provided Species model

This script must be run in /mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_provided_split/
"""
import config
import os
import pandas as pd


S2_path = os.path.join(config.MLDSP_path, "samples/Table_S2.csv")
df = pd.read_csv(S2_path, skiprows=0, header=1, index_col=0)
for index, row in df.iterrows():
	print("======================= start", index, "=======================")
	prefix = "even_"+index
	forward_file = prefix+"_1_trimmed.fa"
	reverse_file = prefix+"_2_trimmed.fa"
	tfrec_file = prefix+".tfrec"
	result_file = prefix+".result.txt"
	profile_file = prefix+".profile.txt"
	profile_0_file = prefix+".0_profile.txt"
	if not os.path.exists(tfrec_file): # if the tfrecord does not exist in the current dir
		if os.path.exists(os.path.join(config.DM_data_path, "mag_reads_150bp_1w_split", tfrec_file)): #exists in the other dir, copy
			os.system("cp "+ os.path.join(config.DM_data_path, "mag_reads_150bp_1w_split", tfrec_file) + " " + tfrec_file)
		else: # generate
			os.system("tfrec_predict_kmer.sh \
				-f /mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_provided_split/"+forward_file+" \
				-r /mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_provided_split/"+reverse_file+" \
				-t fasta \
				-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
				-o "+prefix+" \
				-s 4000000 \
			-k 12")
	# changed batch seize from 8192 to 4096
	os.system("predict_DeepMicrobes.sh \
		-i "+tfrec_file+" \
		-b 4096 \
		-l species \
		-p 8 \
		-m /mnt/sda/DeepMicrobes-data/weights/weights_species \
		-o "+prefix)
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_file+" \
		-t 50 \
		-l "+ os.path.join(config.DM_path, "name2label/name2label_species.txt"))
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_0_file+" \
		-t 0 \
		-l " + os.path.join(config.DM_path, "name2label/name2label_species.txt"))
	print("======================= done", prefix, "=======================")
	