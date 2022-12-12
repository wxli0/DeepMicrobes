import numpy as np
import os 
import pandas as pd
import sys

# read in ground-truth labels by GTDB-Tk
gtdb_tk_ground_truth = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/Task2-ground_truth.csv", header=0, index_col=0)
print(gtdb_tk_ground_truth.head())
gtdb_db = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/db_samples.tsv", sep='\t', header=0, index_col=2)
print(gtdb_db.head())
# calculate classification accuracies

result_dir_path = "/mnt/sda/MLDSP-samples-r202/rumen_mags/root_short_kraken/"
# result_dir_path = "/mnt/sda/MLDSP-samples-r202/rumen_mags/root_kraken/"


gtdb_tk_ranks = ["gtdb-tk-domain","gtdb-tk-phylum","gtdb-tk-class","gtdb-tk-order","gtdb-tk-family","gtdb-tk-genus","gtdb-tk-species"]
ranks = ["domain", "phylum", "class", "order", "family", "genus", "species"]

def compute_result_at_rank(result_dir_path, rank):
    """
    Compute the accuracy statistics at a specific rank

    @param: result_dir_path folder path for storing the result 
    @param: rank to compute classification statistics 

    Return the constrained accuracy, absolute accuracy, weighted accuracy and classification rate
    """
    total = 0
    classified = 0
    correct = 0
    weighted_correct = 0
    gtdb_tk_rank = "gtdb-tk-"+rank
    rank_index = ranks.index(rank)
    for file in os.listdir(result_dir_path):
        if file.endswith("_result.txt"):
            file_id = file.split('_')[0]+".fasta"
            # look up the file_id classification by GTDB-Tk
            gtdb_tk_label_list = gtdb_tk_ground_truth.loc[file_id]
            if os.stat(os.path.join(result_dir_path, file)).st_size == 0:
                continue
            kraken_df = pd.read_csv(os.path.join(result_dir_path, file), sep='\t', header=None)
            total += kraken_df.shape[0]
            kraken_preds = list(kraken_df.iloc[:, 2])
            for kraken_pred in kraken_preds:
                if kraken_pred == 0: # definitely not classified
                    continue
                if kraken_pred not in list(gtdb_db.index):
                    continue
                if (isinstance(gtdb_db.loc[kraken_pred]['gtdb_taxonomy'], pd.Series)):
                    continue
                gtdb_taxonomy_list =  gtdb_db.loc[kraken_pred]['gtdb_taxonomy'].split(";")
                del gtdb_taxonomy_list[1] # delete kingdom

                # determine if it is actually classified
                if len(gtdb_taxonomy_list) < (rank_index+1): # not classified at the rank
                    continue
                classified += 1
                
                weight_incre = 0
                for cur_index in range(rank_index+1):
                    cur_rank = ranks[cur_index]
                    predicted_label = gtdb_taxonomy_list[cur_index]
                    true_label = gtdb_tk_label_list[cur_index]
                    if true_label == predicted_label:
                        weight_incre += 1
                    elif 'uncertain' in predicted_label:
                        break
                    elif predicted_label != true_label:
                        weight_incre -= 1/2
                weighted_correct += weight_incre/(rank_index+1)  

                if weight_incre == (rank_index+1):
                    correct += 1

    CA = 0
    if classified != 0:
        CA = correct/classified
    AA = correct/total
    WA = weighted_correct/total
    CR = classified/total
    return round(CA,4), round(AA, 4), round(WA, 4), round(CR, 4)

CAs = []
AAs = []
WAs = []
CRs = []
for rank in ranks:
    CA, AA, WA, CR = compute_result_at_rank(result_dir_path, rank)
    CAs.append(CA)
    AAs.append(AA)
    WAs.append(WA)
    CRs.append(CR)
    print(rank, "accuracies are:", "CA:", CA, "AA", AA, "WA:", WA, "CR:", CR)
print("avg accuracies are:", "CA:", round(np.mean(CAs), 4), "AA", round(np.mean(AAs),4),\
    "WA:", round(np.mean(WAs), 4), "CR:", round(np.mean(CRs), 4))