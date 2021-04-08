import sys
import os

dir = "/mnt/sda/DeepMicrobes-data/rumen_mags"
for forward_file in os.listdir(dir):
	if forward_file.endswith('_1.fa'):
		prefix = forward_file[:-5]
		print("======================= start", prefix, "=======================")
		reverse_file = prefix+'_2.fa'
		tfrec_file = prefix+".tfrec"
		result_file = prefix+".result.txt"
		profile_file = prefix+".profile.txt"
		profile_0_file = prefix+".0_profile.txt"
		category_file = prefix+".category_paired.txt"
		prob_file = prefix+".prob_paired.txt"
		os.system("tfrec_predict_kmer.sh \
			-f "+dir+forward_file+" \
			-r "+dir+reverse_file+" \
			-t fasta \
			-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
			-o "+prefix+" \
			-s 4000000 \
			-k 12")
		os.system("DeepMicrobes.py \
			--input_tfrec="+tfrec_file+" \
			--model_name=attention \
			--model_dir=/home/w328li/DeepMicrobes/dm_genus_balanced_embed_20_weights \
			--embedding_dim=20 --num_classes=205")
		os.system("paste " + category_file + " " + prob_file + " > " + result_file)
		os.system("rm " + category_file+ " " + prob_file)
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_file+" \
			-t 50 \
			-l /home/w328li/DeepMicrobes/data/name2label_gtdb_genus.txt")
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_0_file+" \
			-t 0 \
			-l /home/w328li/DeepMicrobes/data/name2label_gtdb_genus.txt")
		print("======================= done", prefix, "=======================")
		