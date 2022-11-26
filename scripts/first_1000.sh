#!/usr/bin/bash

# get the first 1,000 reads for kraken 2
# bash first_1000.sh 1 (for Task 1)
# bash first_1000.sh 2 (for Task 2)

task=$1

dir=""

if [[ $task -eq 2 ]]; then
    dir="/mnt/sda/DeepMicrobes-data/rumen_mags_reads_Task2_small_all"
fi

new_dir=${dir}_kraken

if [ -d "$new_dir" ]; 
    then rm -r $new_dir; 
fi

mkdir $new_dir

if [[ $task -eq 2 ]]; then
    for file in ${dir}/*1_trimmed.fa ; do
        cat ${file} |head -2000 > ${new_dir}/`basename "$file"`
    done
fi