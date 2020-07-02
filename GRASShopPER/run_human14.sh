#!/bin/bash

grasshopper preprocess frag_1.fastq frag_2.fastq -trimparams="ILLUMINACLIP:${TRIMMOMATIC_PATH}/adapters/TruSeq3-PE.fa:2:30:10 SLIDINGWINDOW:30:20 LEADING:15 TRAILING:15 MINLEN:85"
grasshopper build frag
grasshopper traverse frag -ss=14 -fs=100
grasshopper correct frag -minconf=1 -maxrefs=1

