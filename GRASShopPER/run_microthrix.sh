#!/bin/bash

grasshopper preprocess SRR576810.1_1.fastq SRR576810.1_2.fastq
grasshopper build SRR576810.1 -sli=13 -ws=500 -awa=TRUE -e=4
grasshopper traverse SRR576810.1 -ss=14
grasshopper correct SRR576810.1 -minconf=100 -maxrefs=0

