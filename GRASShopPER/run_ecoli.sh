#!/bin/bash

grasshopper preprocess ERR022075_1.fastq ERR022075_2.fastq
grasshopper build ERR022075 -sli=25 -ws=500
grasshopper traverse ERR022075 -ss=14
grasshopper correct ERR022075 -minconf=3 -maxrefs=3

