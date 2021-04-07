import sys
import os

os.system("tfrec_predict_kmer.sh \
	-f /mnt/sda/DeepMicrobes-data/SRR5935743_clean_1.fastq \
	-r /mnt/sda/DeepMicrobes-data/SRR5935743_clean_2.fastq \
	-t fastq \
	-v /mnt/sda/DeepMicrobes-data/tokens_merged_12mers.txt \
	-o SRR5935743 \
	-s 4000000 \
	-k 12")
os.system("predict_DeepMicrobes.sh \
	-i SRR5935743.tfrec \
	-b 8192 \
	-l genus \
	-p 8 \
	-m /mnt/sda/DeepMicrobes-data/weights_species \
	-o SRR5935743")
os.system("report_profile.sh \
	-i SRR5935743.result.txt \
	-o SRR5935743.profile.txt \
	-t 50 \
	-l /home/w328li/DeepMicrobes/data/name2label_genus.txt")