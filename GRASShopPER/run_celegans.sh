#!/bin/bash

grasshopper preprocess DRR008444_1.fastq DRR008444_2.fastq
grasshopper build DRR008444
grasshopper traverse DRR008444 -ss=14 -fs=2
grasshopper correct DRR008444 -minconf=7 -maxrefs=7

