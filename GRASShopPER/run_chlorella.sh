#!/bin/bash

grasshopper preprocess 170113_I191_FCHFMF5BCXY_L2_CWHPEI16120009_1.fastq 170113_I191_FCHFMF5BCXY_L2_CWHPEI16120009_2.fastq -trimparams="ILLUMINACLIP:${TRIMMOMATIC_PATH}/adapters/TruSeq3-PE.fa:2:30:10 SLIDINGWINDOW:30:20 LEADING:15 TRAILING:15 MINLEN:85 CROP:210"
grasshopper build 170113_I191_FCHFMF5BCXY_L2_CWHPEI16120009 -ws=50 -sli=31 -sc=140 -ps=140
grasshopper traverse 170113_I191_FCHFMF5BCXY_L2_CWHPEI16120009 -ss=14 -fs=2
grasshopper correct 170113_I191_FCHFMF5BCXY_L2_CWHPEI16120009 -minconf=7 -maxrefs=7

