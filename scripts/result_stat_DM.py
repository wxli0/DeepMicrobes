import config
import os
import pandas as pd

gt_path = os.path.join(config.MLDSP_path, "samples/Table_S2.csv")
gt_df = pd.read_csv(gt_path, skiprows=0, header=1, index_col=0)
thres = 0

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

print("constrained accuracy is:", conf_correct_count/conf_count)
print("absolute accuracy is:", conf_correct_count/total_count)
