import config
import os
from scripts.convert_to_tfrec_unassigned import S2_path
import pandas as pd


S2_path = os.path.join(config.MT_MAG_path, "outputs-HGR-r202-archive1/HGR-r202-prediction-full-path.csv")
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
	os.system("tfrec_predict_kmer.sh \
		-f /mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_split/"+forward_file+" \
		-r /mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_split/"+reverse_file+" \
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
		-m /mnt/sda/DeepMicrobes-data/HGR_r202_train_weights/ \
		-o "+prefix)
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_file+" \
		-t 50 \
		-l "+ os.path.join(config.DM_path, "name2label/HGR_species.txt"))
	os.system("report_profile.sh \
		-i "+result_file+" \
		-o "+profile_0_file+" \
		-t 0 \
		-l " + os.path.join(config.DM_path, "name2label/HGR_species.txt"))
	print("======================= done", prefix, "=======================")
	