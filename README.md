# DeepMicrobes

DeepMicrobes: taxonomic classification for metagenomics with deep learning <br>
Supplementary data for the paper is available at https://github.com/MicrobeLab/DeepMicrobes-data <br>
<b>IMPORTANT: The new DeepMicrobes (beta version) is available now. Please feel free to contact us if you have any suggestions or encounter any errors.</b>

## Usage

* [Getting start with DeepMicrobes](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/example.md)
* [How to install](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/install.md)
* [How to convert fastq/fasta sequences to TFRecord](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/tfrecord.md)
* [How to make predictions on a metagenome dataset](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/prediction.md)
* [How to generate taxonomic profiles](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/profile.md)
* [How to choose the confidence threshold](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/confidence.md)
* [How to train the DNN model of DeepMicrobes](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/train.md)
* [How to submit to GPUs](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/gpu.md)
* [Suggestions on training a custom model (for advanced users)](https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/custom.md)



## Contact

Any issues with the DeepMicrobes framework can be filed with [GitHub issue tracker](https://github.com/MicrobeLab/DeepMicrobes/issues).
We are committed to maintain this repository to assist users and tackle errors. 

<b>Email</b>
* liangqx7@mail2.sysu.edu.cn (Qiaoxing Liang)



## Citation

Qiaoxing Liang, Paul W Bible, Yu Liu, Bin Zou, Lai Wei, [DeepMicrobes: taxonomic classification for metagenomics with deep learning](https://doi.org/10.1093/nargab/lqaa009), NAR Genomics and Bioinformatics, Volume 2, Issue 1, March 2020, lqaa009, https://doi.org/10.1093/nargab/lqaa009

## Dataset information

Original DeepMicrobes's Task 1: 2505 classes, simulated reads location: /mnt/sda/DeepMicrobes-data/labeled_genome_train_species_reads

Task 1 (sparse) training: 2298 classes, simuated reads location: :/mnt/sda/DeepMicrobes-data/labeled_genome_train_species_reads_author/author_train.tfrec

Task 1 (sparse) test: provided by DeepMicrobes

Task 2 (dense) training: 601 classes, simulated reads locatoin /mnt/sda/MLDSP-samples-r202/GTDB_small_representative_label_reads/Task2_small.tfrec

Task 2 (dense) test: /mnt/sda/DeepMicrobes-data/rumen_mags_reads_Task2_small_all