import config
import os
import pandas as pd

def result(thres, gt_path):
    """
    Computes the constrained accuracy and absolute accuracy for threshold thres
    The ground-truth information is in the csv in gt_path
    """
    gt_df = pd.read_csv(gt_path, skiprows=0, header=1, index_col=0)
    result_dir = "/mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_split"
    total_count = 0
    conf_count = 0
    conf_correct_count = 0

    for index, row in gt_df.iterrows():
        res_file_name = "even_"+index+".result.txt"
        if not os.path.exists(os.path.join(result_dir, res_file_name)): # delete this line when entire_process_Task1_DM completes
            continue
        with open(os.path.join(result_dir, res_file_name)) as res_file:
            for line in res_file:
                total_count += 1
                pred = int(line.split()[0])
                conf = float(line.split()[1])
                if conf >= thres:
                    conf_count += 1
                    if pred == int(row['Species label']):
                        conf_correct_count += 1

    return conf_correct_count/conf_count, conf_correct_count/total_count


gt_path = os.path.join(config.MLDSP_path, "samples/Table_S2.csv")
thres_list = list(range(0,100,10))
for thres in thres_list:
    CA, AA = result(thres, gt_path)
    print("threshold:", thres, "CA:", CA, "AA:", AA)