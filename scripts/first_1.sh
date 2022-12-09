#!/usr/bin/bash

# get the first 1 contig for kraken 2 (Task 2 rumen mags)


dir="/mnt/sda/MLDSP-samples-r202/rumen_mags/root"


new_dir=${dir}_kraken

if [ -d "$new_dir" ]; 
    then rm -r $new_dir; 
fi

mkdir $new_dir

for file in ${dir}/*.fasta ; do
    cat ${file} |head -2 > ${new_dir}/`basename "$file"`
done
