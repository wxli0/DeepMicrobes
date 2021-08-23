"""
Executes the entire procss of DeepMicrobes for Task 2 (GTDB/cow rumen mags). \
	The phases are converting test dataset to tfrec (tfrec_predict_kmer.sh), \
		  using pre-trained model to predict tfrec test dataset (DeepMicrobes.py), \
			  reporting profiles of the testing result (report_profile.sh)

No command line arguments are required.
This script must be run in result_path (default: /mnt/sda/DeepMicrobes-data/rumen_mags)
"""

import argparse
import config
import os

parser = argparse.ArgumentParser(description='Execute entire process of Task 2 (real/dense)')
parser.add_argument('--result_path', help='path of result files', \
	default='/mnt/sda/DeepMicrobes-data/rumen_mags')
args = parser.parse_args()
if os.getcwd() != args.result_path:
	raise Exception("Sorry, this file has to be run in args.result_path. \
		Default: /mnt/sda/DeepMicrobes-data/rumen_mags")

dir = config.GTDB_test_path
for forward_file in os.listdir(dir):
	if forward_file.endswith('_1.fa'):
		if os.path.exists(profile_file) and os.path.exists(profile_0_file):
			print("======================= skip "+forward_file+" =======================")
			continue
		prefix = forward_file[:-5]
		print("======================= start", prefix, "=======================")
		reverse_file = prefix+'_2.fa'
		tfrec_file = prefix+".tfrec"
		result_file = prefix+".result.txt"
		profile_file = prefix+".profile.txt"
		profile_0_file = prefix+".0_profile.txt"
		category_file = prefix+".category_paired.txt"
		prob_file = prefix+".prob_paired.txt"

		# converts test dataset to tfrec
		if not os.path.exists(tfrec_file):
			os.system("tfrec_predict_kmer.sh \
				-f "+dir+forward_file+" \
				-r "+dir+reverse_file+" \
				-t fasta \
				-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
				-o "+prefix+" \
				-s 4000000 \
				-k 12")
			print("======= done tfrec_predict_kmer =======")

		# use pre-trained model to predict tfrec test dataset
		os.system("DeepMicrobes.py --num_classes=601 \
			--model_name=attention --encode_method=kmer \
			--embedding_dim=100 --model_dir=/mnt/sda/DeepMicrobes-weights/GTDB_r202_train_weights \
			--input_tfrec="+tfrec_file + " \
			--vocab_size=8390658 --cpus=1 \
			--translate=False --pred_out=" + prefix + " \
			--running_mode=predict_paired_class")
		print("======= done DeepMicrobes =======")
		os.system("paste " + category_file + " " + prob_file + " > " + result_file)
		os.system("rm " + category_file+ " " + prob_file)

		# reports profiles of the testing result
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_file+" \
			-t 50 \
			-l "+ os.path.join(config.DM_path, "data/name2label_gtdb_species_r202.txt"))
		print("======= done report_profile 50 =======")
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_0_file+" \
			-t 0 \
			-l " +  os.path.join(config.DM_path, "data/name2label_gtdb_species_r202.txt"))
		print("======= done report_profile_0 =======")
		print("======================= done", prefix, "=======================")
		