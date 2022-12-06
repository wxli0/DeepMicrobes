import os 
import pandas as pd
import sys

# read in ground-truth labels by GTDB-Tk
gtdb_tk_ground_truth = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/Task2-ground_truth.csv", header=0, index_col=0)
print(gtdb_tk_ground_truth.head())
gtdb_db = pd.read_csv("~/MT-MAG/outputs-GTDB-r202-archive3/db_samples.tsv", sep='\t', header=0, index_col=2)
print(gtdb_db.head())
# calculate classification accuracies

result_dir_path = "/mnt/sda/MLDSP-samples-r202/rumen_mags/d__Bacteria_kraken/"

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
                
                correct_label_len = 0
                for i in range(0, min(len(gtdb_taxonomy_list), rank_index+1)):
                    rank = gtdb_tk_ranks[i]
                    if gtdb_taxonomy_list[i] == gtdb_tk_label_list[rank]:
                        correct_label_len += 1
                    else:
                        break
                gtdb_tk_rank_index = gtdb_tk_ranks.index(gtdb_tk_rank)
                weighted_correct += correct_label_len/(rank_index+1)
                if len(gtdb_taxonomy_list) >= (gtdb_tk_rank_index+1) and gtdb_taxonomy_list[gtdb_tk_rank_index] == gtdb_tk_label_list[gtdb_tk_rank]:
                    correct += 1
    CA = 0
    if classified != 0:
        CA = correct/classified
    AA = correct/total
    WA = weighted_correct/total
    CR = classified/total
    return CA, AA, WA, CR

for rank in ranks:
    CA, AA, WA, CR = compute_result_at_rank(result_dir_path, rank)
    print(rank, "accuracies are:", "CA:", CA, "AA", AA, "WA:", WA, "CR:", CR)