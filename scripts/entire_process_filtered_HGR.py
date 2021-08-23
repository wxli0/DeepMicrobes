"""
Executes the entire procss of DeepMicrobes for Task 1 (HGR/ERP108418). \
	The phases are converting test dataset to tfrec (tfrec_predict_kmer.sh), \
		  using pre-trained model to predict tfrec test dataset (DeepMicrobes.py), \
			  reporting profiles of the testing result (report_profile.sh)

No command line arguments are required.
This file has to be run in /mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_results/
"""

import argparse
import config
import pandas as pd 
import os
from os.path import expanduser

parser = argparse.ArgumentParser(description='Execute entire process of Task 1 (simulated/sparse)')
parser.add_argument('--result_path', help='path of result files', \
	default='/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_results/')
args = parser.parse_args()
if os.getcwd() != args.result_path:
	raise Exception("Sorry, this file has to be run in args.result_path")

S2_path = os.path.join(config.base_path, "MLDSP/samples/Table_S2.csv")
df = pd.read_csv(S2_path, skiprows=0, header=1, index_col=0)
for index, row in df.iterrows():
	prefix = "even_"+index
	print("======================= start", prefix, "=======================")
	tfrec_file = '/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000/'+prefix+".tfrec"
	result_file = prefix+".result.txt"
	profile_file = prefix+".profile.txt"
	profile_0_file = prefix+".0_profile.txt"
	category_file = prefix+".category_paired.txt"
	prob_file = prefix+".prob_paired.txt"
	if not os.path.exists(profile_0_file) or not os.path.exists(profile_file):
		print('skip', index)
	else:
		os.system("DeepMicrobes.py --num_classes=2299 \
			--model_name=attention --encode_method=kmer \
			--model_dir=/mnt/sda/DeepMicrobes-weights/HGR_r202_train_weights \
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
			-l " + os.path.join(config.base_path, "DeepMicrobes/data/name2label_hgr_species_r202.txt"))
		print("======= done report_profile 50 =======")
		os.system("report_profile.sh \
			-i "+result_file+" \
			-o "+profile_0_file+" \
			-t 0 \
			-l " + os.path.join(config.base_path, "DeepMicrobes/data/name2label_hgr_species_r202.txt"))
		print("======= done report_profile_0 =======")
		print("======================= done", prefix, "=======================")
			