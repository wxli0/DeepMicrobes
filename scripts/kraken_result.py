import os 
import pandas as pd
import sys

# read in ground-truth labels by GTDB-Tk
gtdb_tk_ground_truth = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/Task2-ground_truth.csv", header=0, index_col=0)
print(gtdb_tk_ground_truth.head())
gtdb_db = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/db_samples.tsv", sep='\t', header=0, index_col=2)
print(gtdb_db.head())
# calculate classification accuracies

rumen_folder_ids = range(0, 4)
base_path = "/mnt/sda/DeepMicrobes-data"
correct = 0
weighted_correct = 0
total = 0
classified = 0
gtdb_tk_ranks = ["gtdb-tk-domain","gtdb-tk-phylum","gtdb-tk-class","gtdb-tk-order","gtdb-tk-family","gtdb-tk-genus","gtdb-tk-species"]
for rumen_folder_id in rumen_folder_ids:
    cur_dir = os.path.join(base_path, "rumen_mags_reads_Task2_small_all_kraken_"+str(rumen_folder_id))
    print("cur_dir is:", cur_dir)
    for file in os.listdir(cur_dir):
        if file.endswith("_result.txt"):
            file_id = file.split('_')[1][:-2]+".fasta"
            print("file_id is:", file_id)
            # look up the file_id classification by GTDB-Tk
            gtdb_tk_label_list = gtdb_tk_ground_truth.loc[file_id]
            kraken_df = pd.read_csv(os.path.join(cur_dir, file), sep='\t')
            total += kraken_df.shape[0]
            kraken_preds = list(kraken_df.iloc[:, 2])
            for kraken_pred in kraken_preds:
                if kraken_pred != 0:
                    classified += 1
                if kraken_pred not in list(gtdb_db.index):
                    continue
                gtdb_taxonomy_list =  gtdb_db.loc[kraken_pred]['gtdb_taxonomy'].str.split(";")
                del gtdb_taxonomy_list[1]
                
                correct_label_len = 0
                for i in range(0, min(len(gtdb_taxonomy_list), len(gtdb_tk_ranks))):
                    rank = gtdb_tk_ranks[i]
                    if gtdb_taxonomy_list[i] == gtdb_tk_label_list[rank]:
                        correct_label_len += 1
                    else:
                        break
                weighted_correct += correct_label_len/len(gtdb_tk_ranks)
                if len(gtdb_taxonomy_list) >= 7 and gtdb_taxonomy_list[6] == gtdb_tk_label_list["gtdb-tk-species"]:
                    correct += 1

            print("current CA is:", correct/classified)
            print("current AA is:", correct/total)
            print("current WA is:", weighted_correct/total)
            print("current CR is:", classified/total)

print("CA is:", correct/classified)
print("AA is:", correct/total)
print("WA is:", weighted_correct/total)
print("CR is:", classified/total)

