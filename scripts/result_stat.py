"""
Calculates the classified accuracy, absolute accuracy and adjusted accuracy, rejection rate for Task 1\
    (simulated/sparse) and Task 2 (real/dense) for DeepMicrobes

No command line arguments are required.
"""


import config
import os
import pandas as pd


paths = [os.path.join(config.MT_MAG_path, 'outputs-r202/MLDSP-prediction-full-path.csv'),\
    os.path.join(config.MT_MAG_path, 'outputs-HGR-r202/HGR-prediction-full-path.csv')]


def readin_dict(prof_path):
    file = open(prof_path, 'r')
    lines = file.readlines()
    
    # construct profile dictionary prof_dict
    prof_dict = {}
    for line in lines:
        pair = line.split('\t')
        prof_dict[pair[0]] = int(pair[1])
    return prof_dict



def calc_pr(df_path, res_path, ignore_indices = []):
    total = 0
    correct = 0
    rejected = 0
    df = pd.read_csv(df_path, index_col=0, header=0, dtype = str)

    for index, row in df.iterrows():
        label = df.loc[index]['gtdb-tk-species']
        if index not in ignore_indices and label != 's__':
            prof_dict = readin_dict(os.path.join(res_path, index.split('.')[0]+".profile.txt"))
            prof_0_dict = readin_dict(os.path.join(res_path, index.split('.')[0]+'.0_profile.txt'))
            total += sum(prof_0_dict.values())
            rejected += sum(prof_0_dict.values())-sum(prof_dict.values())
            if label in prof_0_dict:
                correct += prof_0_dict[label]

    classified_acc = 0
    if (total-rejected) != 0:
        classified_acc = correct/(total-rejected)
    absolute_acc = correct/total
    rejection_rate = rejected/total
    adjusted_acc = (correct+0.5*rejected)/total
    
    return classified_acc, absolute_acc, adjusted_acc, rejection_rate

path2 = os.path.join(config.MT_MAG_path, 'outputs-HGR-r202/HGR-r202-prediction-full-path.csv')
res_path2 = '/mnt/sda/DeepMicrobes-data/mag_reads_250bp_1w_200000_results'
ignore_indices2 = ['even_MAG-GUT10417.fa', 'even_MAG-GUT15880.fa', 'even_MAG-GUT1743.fa', 'even_MAG-GUT21953.fa', 'even_MAG-GUT22878.fa', 'even_MAG-GUT28136.fa', 'even_MAG-GUT29051.fa', 'even_MAG-GUT29076.fa', 'even_MAG-GUT33914.fa', 'even_MAG-GUT36027.fa', 'even_MAG-GUT40857.fa', 'even_MAG-GUT41924.fa', 'even_MAG-GUT42485.fa', 'even_MAG-GUT42494.fa', 'even_MAG-GUT42584.fa', 'even_MAG-GUT43216.fa', 'even_MAG-GUT43894.fa', 'even_MAG-GUT44111.fa', 'even_MAG-GUT44851.fa', 'even_MAG-GUT45331.fa', 'even_MAG-GUT46923.fa', 'even_MAG-GUT47106.fa', 'even_MAG-GUT47179.fa', 'even_MAG-GUT4902.fa', 'even_MAG-GUT52094.fa', 'even_MAG-GUT52107.fa', 'even_MAG-GUT52138.fa', 'even_MAG-GUT53617.fa', 'even_MAG-GUT54931.fa', 'even_MAG-GUT56425.fa', 'even_MAG-GUT5727.fa', 'even_MAG-GUT58014.fa', 'even_MAG-GUT58077.fa', 'even_MAG-GUT59039.fa', 'even_MAG-GUT60365.fa', 'even_MAG-GUT61159.fa', 'even_MAG-GUT61176.fa', 'even_MAG-GUT61959.fa', 'even_MAG-GUT70200.fa', 'even_MAG-GUT7064.fa', 'even_MAG-GUT7066.fa', 'even_MAG-GUT7291.fa', 'even_MAG-GUT76426.fa', 'even_MAG-GUT77982.fa', 'even_MAG-GUT78879.fa', 'even_MAG-GUT78908.fa', 'even_MAG-GUT78923.fa', 'even_MAG-GUT81671.fa', 'even_MAG-GUT82176.fa', 'even_MAG-GUT82203.fa', 'even_MAG-GUT83501.fa', 'even_MAG-GUT83507.fa', 'even_MAG-GUT83946.fa', 'even_MAG-GUT8428.fa', 'even_MAG-GUT84696.fa', 'even_MAG-GUT84793.fa', 'even_MAG-GUT8521.fa', 'even_MAG-GUT86514.fa', 'even_MAG-GUT86868.fa', 'even_MAG-GUT87091.fa', 'even_MAG-GUT87486.fa', 'even_MAG-GUT87573.fa', 'even_MAG-GUT87828.fa', 'even_MAG-GUT88085.fa', 'even_MAG-GUT88218.fa', 'even_MAG-GUT88257.fa', 'even_MAG-GUT88679.fa', 'even_MAG-GUT88862.fa', 'even_MAG-GUT89291.fa', 'even_MAG-GUT89323.fa', 'even_MAG-GUT90190.fa', 'even_MAG-GUT90947.fa', 'even_MAG-GUT91328.fa']

classified_acc, absolute_acc, adjusted_acc, rejection_rate = calc_pr(path2, res_path2, ignore_indices=ignore_indices2)
print("==== HGR result ====")
print("classified accuracy is:", classified_acc)
print("absolute accuracy is:", absolute_acc)
print("adjusted accuracy is:", adjusted_acc)
print("rejection rate is:", rejection_rate)

path1 = os.path.join(config.MT_MAG_path, 'outputs-GTDB-r202/GTDB-r202-prediction-full-path.csv')
res_path1 = '/mnt/sda/DeepMicrobes-data/rumen_mags'
ignore_indices1 =  ['RUG428.fasta', 'RUG635.fasta', 'RUG684.fasta', 'RUG687.fasta', 'RUG732.fasta', 'RUG752.fasta', 'RUG789.fasta', 'RUG820.fasta']

classified_acc, absolute_acc, adjusted_acc, rejection_rate = calc_pr(path1, res_path1, ignore_indices=ignore_indices1)
print("==== GTDB result ====")
print("classified accuracy is:", classified_acc)
print("absolute accuracy is:", absolute_acc)
print("adjusted accuracy is:", adjusted_acc)
print("rejection rate is:", rejection_rate)







