#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/${1}.out
#SBATCH --error=logs/${1}.err


# 1 -- dataset name
# 2 -- INSERT_SIZE
# 3 -- INSERT_STD
# 4 -- COVERAGE

module load python/3.7.0

/usr/bin/time -v -o logs/${1}_velveth.log velveth ${1} 51 \
-short -separate -fastq \
/home/plgrid-groups/plggillumina/alga_tests/data/${1}/${1}_1.fastq \
/home/plgrid-groups/plggillumina/alga_tests/data/${1}/${1}_2.fastq

/usr/bin/time -v -o logs/${1}_velvetg.log velvetg ${1} -ins_length ${2} -ins_length_sd ${3} -exp_cov ${4} -scaffolding no -min_contig_lgth 250

