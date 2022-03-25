import config
import os
import pandas as pd

def const_label2name(file):
    """
    Constructs label to name mapping from file
    """
    ret = {}
    with open(file) as map_file:
        for line in map_file:
            line = line.strip()
            ret[int(line.split()[1])] = line.split()[0]
    return ret

ori_label2name = const_label2name(os.path.join(config.DM_path, "name2label/name2label_species.txt"))
new_tax = pd.read_csv(os.path.join(config.DM_path, "file2label/gtdbtk.bac120.summary.tsv"), sep='\t', header = 0, index_col = 0)

def check_correct(pred, label):
    """
    :params pred: number from prediction, in original HGR taxonomy
    :param label: number from ground-truth, in original HGR taxonomy

    :return checks if pred == label in our GTDB updated taxomomy
    """
    if pred == label:
        return True
    
    
    pred_name = ori_label2name[pred]
    label_name = ori_label2name[label]
    return new_tax.loc["label_"+pred_name]["classification"] == new_tax.loc["label_"+label_name]["classification"]


def result(thres, gt_path, ignore_indices = []):
    """
    Computes the constrained accuracy, absolute accuracy, weighted accuracy and unclassification rate for threshold thres
    The ground-truth information is in the csv in gt_path
    """
    gt_df = pd.read_csv(gt_path, skiprows=0, header=1, index_col=0)
    result_dir = "/mnt/sda/DeepMicrobes-data/mag_reads_150bp_1w_provided_split"
    total_count = 0
    conf_count = 0
    conf_correct_count = 0

    for index, row in gt_df.iterrows():
        res_file_name = "even_"+index+".result.txt"
        if not os.path.exists(os.path.join(result_dir, res_file_name)): # delete this line when entire_process_Task1_DM completes
            continue
        if index+".fa" in ignore_indices: # ground-truth does not exist in the training set, skip
            continue
        with open(os.path.join(result_dir, res_file_name)) as res_file:
            for line in res_file:
                total_count += 1
                pred = int(line.split()[0])
                conf = float(line.split()[1])
                if conf >= thres:
                    conf_count += 1
                    if check_correct(pred,int(row['Species label'])):
                        conf_correct_count += 1

    return conf_correct_count/conf_count, conf_correct_count/total_count,\
         (conf_correct_count+0.5*(total_count-conf_count))/total_count, (total_count-conf_count)/total_count


gt_path = os.path.join(config.MLDSP_path, "samples/Table_S2.csv")
thres_list = list(range(0,100,10))
thres = 50
CA, AA, WA, UCR= result(thres, gt_path, ignore_indices= ['MAG-GUT10417.fa', 'MAG-GUT15880.fa', 'MAG-GUT1743.fa', 'MAG-GUT21953.fa', 'MAG-GUT22878.fa', 'MAG-GUT28136.fa', 'MAG-GUT29051.fa', 'MAG-GUT29076.fa', 'MAG-GUT33914.fa', 'MAG-GUT36027.fa', 'MAG-GUT40857.fa', 'MAG-GUT41924.fa', 'MAG-GUT42485.fa', 'MAG-GUT42494.fa', 'MAG-GUT42584.fa', 'MAG-GUT43216.fa', 'MAG-GUT43894.fa', 'MAG-GUT44111.fa', 'MAG-GUT44851.fa', 'MAG-GUT45331.fa', 'MAG-GUT46923.fa', 'MAG-GUT47106.fa', 'MAG-GUT47179.fa', 'MAG-GUT4902.fa', 'MAG-GUT52094.fa', 'MAG-GUT52107.fa', 'MAG-GUT52138.fa', 'MAG-GUT53617.fa', 'MAG-GUT54931.fa', 'MAG-GUT56425.fa', 'MAG-GUT5727.fa', 'MAG-GUT58014.fa', 'MAG-GUT58077.fa', 'MAG-GUT59039.fa', 'MAG-GUT60365.fa', 'MAG-GUT61159.fa', 'MAG-GUT61176.fa', 'MAG-GUT61959.fa', 'MAG-GUT70200.fa', 'MAG-GUT7064.fa', 'MAG-GUT7066.fa', 'MAG-GUT7291.fa', 'MAG-GUT76426.fa', 'MAG-GUT77982.fa', 'MAG-GUT78879.fa', 'MAG-GUT78908.fa', 'MAG-GUT78923.fa', 'MAG-GUT81671.fa', 'MAG-GUT82176.fa', 'MAG-GUT82203.fa', 'MAG-GUT83501.fa', 'MAG-GUT83507.fa', 'MAG-GUT83946.fa', 'MAG-GUT8428.fa', 'MAG-GUT84696.fa', 'MAG-GUT84793.fa', 'MAG-GUT8521.fa', 'MAG-GUT86514.fa', 'MAG-GUT86868.fa', 'MAG-GUT87091.fa', 'MAG-GUT87486.fa', 'MAG-GUT87573.fa', 'MAG-GUT87828.fa', 'MAG-GUT88085.fa', 'MAG-GUT88218.fa', 'MAG-GUT88257.fa', 'MAG-GUT88679.fa', 'MAG-GUT88862.fa', 'MAG-GUT89291.fa', 'MAG-GUT89323.fa', 'MAG-GUT90190.fa', 'MAG-GUT90947.fa', 'MAG-GUT91328.fa'])

print("threshold:", thres, "CA:", CA, "AA:", AA, "WA:", WA, "UCR", UCR)