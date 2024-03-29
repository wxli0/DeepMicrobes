"""
Executes the entire procss of DeepMicrobes for Task 2 (GTDB/cow rumen mags) mini with 34 classes. \
	The phases are converting test dataset to tfrec (tfrec_predict_kmer.sh), \
		  using pre-trained model to predict tfrec test dataset (DeepMicrobes.py), \
			  reporting profiles of the testing result (report_profile.sh)

No command line arguments are required.
This script must be run in result_path (default: /mnt/sda/DeepMicrobes-data/rumen_mags_Task2_reads)
"""

import argparse
import config
import os

parser = argparse.ArgumentParser(description='Execute entire process of Task 2 (mini) with 34 classes')
parser.add_argument('--result_path', help='path of result files', \
	default='/mnt/sda/DeepMicrobes-data/rumen_mags_Task2_reads')
args = parser.parse_args()
if os.getcwd() != args.result_path:
	raise Exception("Sorry, this file has to be run in args.result_path. \
		Default:/mnt/sda/DeepMicrobes-data/rumen_mags_Task2_reads")

for forward_file in os.listdir(args.result_path):
	prefix = forward_file[:-13]
	reverse_file = prefix+'.2_trimmed.fa'
	tfrec_file = prefix+".tfrec"
	result_file = prefix+".result.txt"
	profile_file = prefix+".profile.txt"
	profile_0_file = prefix+".0_profile.txt"
	category_file = prefix+".category_paired.txt"
	prob_file = prefix+".prob_paired.txt"
	if forward_file.endswith('.1_trimmed.fa'):
		print("======================= start", prefix, "=======================")

		# converts test dataset to tfrec
		if not os.path.exists(tfrec_file): # if tfrec file has not been created
			os.system("tfrec_predict_kmer.sh \
				-f '"+forward_file+"' \
				-r '"+reverse_file+"' \
				-t fasta \
				-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
				-o '"+prefix+"' \
				-s 4000000 \
				-k 12")
			print("======= done tfrec_predict_kmer =======")

		# use pre-trained model to predict tfrec test dataset
		os.system("DeepMicrobes.py --num_classes=34 \
			--model_name=attention --encode_method=kmer \
			--embedding_dim=10 --model_dir=/mnt/sda/DeepMicrobes-data/weights/Task2_mini_weights \
			--input_tfrec='"+tfrec_file + "' \
			--vocab_size=8390658 --cpus=1 \
			--translate=False --pred_out='" + prefix + "' \
			--running_mode=predict_paired_class")
		print("======= done DeepMicrobes =======")
		os.system("paste '" + category_file + "' '" + prob_file + "' > '" + result_file + "'")
		os.system("rm '" + category_file+ "' '" + prob_file + "'")

		# reports profiles of the testing result
		os.system("report_profile.sh \
			-i '"+result_file+"' \
			-o '"+profile_file+"' \
			-t 50 \
			-l "+ os.path.join(config.DM_path, "name2label/GTDB_mini.txt"))
		print("======= done report_profile 50 =======")
		os.system("report_profile.sh \
			-i '"+result_file+"' \
			-o '"+profile_0_file+"' \
			-t 0 \
			-l " +  os.path.join(config.DM_path, "name2label/GTDB_mini.txt"))
		print("======= done report_profile_0 =======")
		print("======================= done", prefix, "=======================")
		