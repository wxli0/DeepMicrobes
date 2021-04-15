import sys
import os

dir = "/mnt/sda/DeepMicrobes-data/rumen_mags/"
for forward_file in os.listdir(dir):
	if forward_file.endswith('_1.fa'):
		prefix = forward_file[:-5]
		print("======================= start", prefix, "=======================")
		tfrec_file = prefix+".tfrec"
		result_file = prefix+".result.txt"
		profile_file = prefix+".profile.txt"
		profile_0_file = prefix+".0_profile.txt"
		category_file = prefix+".category_paired.txt"
		prob_file = prefix+".prob_paired.txt"

		os.system("DeepMicrobes.py --num_classes=120 \
			--model_name=attention --encode_method=kmer \
			--embedding_dim=30 --model_dir=/mnt/sda/DeepMicrobes/HGR_embed_30_weights \
			--input_tfrec="+tfrec_file + " \
			--vocab_size=8390658 --cpus=1 \
			--translate=False --pred_out=" + prefix + " \
			--running_mode=predict_paired_class")
		print("======= done DeepMicrobes =======")
		os.system("paste " + category_file + " " + prob_file + " > " + result_file)
		os.system("rm " + category_file+ " " + prob_file)
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_file+" \
			-t 50 \
			-l /home/w328li/DeepMicrobes/data/name2label_gtdb_genus.txt")
		print("======= done report_profile 50 =======")
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_0_file+" \
			-t 0 \
			-l /home/w328li/DeepMicrobes/data/name2label_gtdb_genus.txt")
		print("======= done report_profile_0 =======")
		print("======================= done", prefix, "=======================")
		