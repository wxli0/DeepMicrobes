#!/usr/bin/bash

## get the first 1,000 reads 

while getopts “t:” OPTION
do
     case ${OPTION} in
         t)
             task=${OPTARG}
             ;;
         ?)
             usage
             exit
             ;;
     esac
done

dir=""

if [[ $task -eq 2 ]]; then
    dir="/mnt/sda/DeepMicrobes-data/rumen_mags_reads_Task2_small_all"
fi

new_dir=${dir}_kraken
mkdir $new_dir

if [[ $task -eq 2 ]]; then
    for file in ${dir}/*1_trimmed.fa ; do
        cat ${file} |head -2000 > ${new_dir}/${file}
    done
fi