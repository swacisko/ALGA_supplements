import os

data_sets ={
    'ara': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_2.fastq',
            'insert': 250,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/ARA/{}.fasta'},
    'ara_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_musket_2.fastq',
                   'insert': 250,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/ARA/{}_musket.fasta'},
    'ara_racer': { 'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_racer_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ARA/ara_racer_2.fastq',
                   'insert': 250,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/ARA/{}_racer.fasta'},
    'cel': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_2.fastq',
            'insert': 225,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/CEL/{}.fasta'},
    'cel_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_musket_2.fastq',
                   'insert': 225,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/CEL/{}_musket.fasta'},
    'cel_racer': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_racer_1.fastq',
                  'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CEL/cel_racer_2.fastq',
                  'insert': 225,
                  'results': '/home/users-groups/grant_452/plg/alga_tests/results/CEL/{}_racer.fasta'},
    'chl': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_2.fastq',
            'insert': 500,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/CHL/{}.fasta'},
    'chl_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_musket_2.fastq',
                   'insert': 500,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/CHL/{}_musket.fasta'},
    'chl_racer': { 'f1': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_racer_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/CHL/chl_racer_2.fastq',
                   'insert': 500,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/CHL/{}_racer.fasta'},
    'eco': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_2.fastq',
            'insert': 500,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/ECO/{}.fasta'},
    'eco_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_musket_2.fastq',
                   'insert': 500,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/ECO/{}_musket.fasta'},
    'eco_racer': { 'f1': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_racer_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/ECO/eco_racer_2.fastq',
                   'insert': 500,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/ECO/{}_racer.fasta'},
    'h14': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_2.fastq',
            'insert': 158,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/H14/{}.fasta'},
    'h14_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_musket_2.fastq',
                   'insert': 158,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/H14/{}_musket.fasta'},
    'h14_racer': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_racer_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/H14/h14_racer_2.fastq',
                   'insert': 158,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/H14/{}_racer.fasta'},
    'lux': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_1.fastq',
            'f2': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_2.fastq',
            'insert': 315,
            'results': '/home/users-groups/grant_452/plg/alga_tests/results/LUX/{}.fasta'},
    'lux_musket': {'f1': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_musket_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_musket_2.fastq',
                   'insert': 315,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/LUX/{}_musket.fasta'},
    'lux_racer': { 'f1': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_racer_1.fastq',
                   'f2': '/home/users-groups/grant_452/plg/alga_tests/data/LUX/lux_racer_2.fastq',
                   'insert': 315,
                   'results': '/home/users-groups/grant_452/plg/alga_tests/results/LUX/{}_racer.fasta'}
}
algos = {
    'spades': {
        'clean': ['corrected'],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/SPADES/SPAdes-3.14.0-Linux/results/{}/contigs.fasta',
        'scaffolds': '/home/users-groups/grant_452/plg/alga_tests/algos/SPADES/SPAdes-3.14.0-Linux/results/{}/scaffolds.fasta',
        'path': '/home/users-groups/grant_452/plg/alga_tests/algos/SPADES/SPAdes-3.14.0-Linux/',
        'script':
            '''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task        
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err


module load python/3.7.0

/usr/bin/time -v -o times/{0}.log bin/spades.py -k 21,33,55,77{3} --careful \\
  --pe1-1  {1} \\
  --pe1-2  {2} \\
  -o results/{0}
'''
    },
    'megahit': {
        'clean': ['intermediate_contigs'],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/MEGAHIT/MEGAHIT-1.2.9-Linux-x86_64-static/results/{}/final.contigs.fa',
        'scaffolds': '',
        'path': '/home/users-groups/grant_452/plg/alga_tests/algos/MEGAHIT/MEGAHIT-1.2.9-Linux-x86_64-static/',
        'script':
            '''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task	
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err


module load python/3.7.0

/usr/bin/time -v -o times/{0}.log bin/megahit \\
  -1 {1} \\
  -2 {2} \\
  -t 16 \\
  -o results/{0}
'''
    },
    'sage': {
        'clean': ['*.graph*', '*.reads'],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/SAGE/SAGE2/results/{0}/{0}_contig.fasta',
        'scaffolds': '/home/users-groups/grant_452/plg/alga_tests/algos/SAGE/SAGE2/results/{0}/{0}_scaffold.fasta',
        'path': '/home/users-groups/grant_452/plg/alga_tests/algos/SAGE/SAGE2/',
        'script':
            '''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task	
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err

/usr/bin/time -v -o times/{0}.log ./SAGE2 \\
  -l {1} \\
  -o results/{0} \\
  -p {0} -k 50 -d -s
'''
    },
    'readjoiner': {
        'clean': [],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/READJOINER/genometools-1.6.1/results/{}.contigs.fas',
        'scaffolds': '',
        'path': '/home/users-groups/grant_452/plg/alga_tests/algos/READJOINER/genometools-1.6.1/',
        'script':
            '''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task        
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err

/usr/bin/time -v -o times/{0}.1.log bin/gt readjoiner prefilter \\
  -readset results/{0} \\
  -db {1}:{2}:{3}

/usr/bin/time -v -o times/{0}.2.log bin/gt -j 8 readjoiner overlap \\
  -readset results/{0} \\
  -l 60

/usr/bin/time -v -o times/{0}.3.log bin/gt readjoiner assembly -spmfiles 8 -readset results/{0} -l 60
'''
    },
    'sga': {
        'clean': ['tmp*', 'read*', 'merged*'],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{}/assemble.m75-contigs.fa',
        'scaffolds': '',
        'path': '/home/users-groups/grant_452/plg/alga_tests/algos/SGA/',
        'script':'''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task        
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err

PATH=/home/users/jbadura/udocker:$PATH

/usr/bin/time -v -o times/{0}.1.log \\
udocker run \\
 -v {1}:/data \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga preprocess --pe-mode 1 \\
  -o /res/tmp.fastq \\
  /data/{2} \\
  /data/{3}

/usr/bin/time -v -o times/{0}.2.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga index \\
  -a ropebwt -t 16 --no-reverse \\
  -p /res/tmp \\
  /res/tmp.fastq

/usr/bin/time -v -o times/{0}.3.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga correct -k 41 --discard --learn -t 16 \\
  -o /res/reads.ec.k41.fastq \\
  -p /res/tmp \\
  /res/tmp.fastq

/usr/bin/time -v -o times/{0}.4.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga index \\
  -a ropebwt -t 16 \\
  -p /res/reads.ec.k41 \\
  /res/reads.ec.k41.fastq

/usr/bin/time -v -o times/{0}.5.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga filter \\
  -x 2 -t 16 \\
  --homopolymer-check \\
  --low-complexity-check \\
  -p /res/reads.ec.k41 \\
  -o /res/reads.ec.k41.fastq.filter.pass.fa \\
  /res/reads.ec.k41.fastq

/usr/bin/time -v -o times/{0}.6.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga fm-merge -m 55 -t 16 \\
  -o /res/merged.k41.fa \\
  -p /res/reads.ec.k41.fastq.filter.pass \\
  /res/reads.ec.k41.fastq.filter.pass.fa

/usr/bin/time -v -o times/{0}.7.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga index \\
  -d 1000000 -t 16 \\
  -p /res/merged.k41 \\
  /res/merged.k41.fa

/usr/bin/time -v -o times/{0}.8.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga rmdup \\
  -t 16 \\
  -p /res/merged.k41 \\
  -o /res/merged.k41.fa.rmdup.fa \\
  /res/merged.k41.fa

/usr/bin/time -v -o times/{0}.9.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 -w /res \\
 sga overlap \\
  -m 55 \\
  -t 16 -v \\
  -p /res/merged.k41.fa.rmdup \\
  /res/merged.k41.fa.rmdup.fa

/usr/bin/time -v -o times/{0}.10.log \\
udocker run \\
 -v /home/users-groups/grant_452/plg/alga_tests/algos/SGA/results/{0}:/res \\
 sga assemble \\
  -m 75 -g 0 -r 10 \\
  -o /res/assemble.m75 \\
  /res/merged.k41.fa.rmdup.asqg.gz
'''
    },
    'soap' : {
        'clean': ['res.path'],
        'contigs': '/home/users-groups/grant_452/plg/alga_tests/algos/SOAP2/SOAPdenovo2/results/{}/res.contig',
        'scaffolds': '/home/users-groups/grant_452/plg/alga_tests/algos/SOAP2/SOAPdenovo2/results/{}/res.scafSeq',
        'path':'/home/users-groups/grant_452/plg/alga_tests/algos/SOAP2/SOAPdenovo2/',
        'script': '''#!/bin/bash

#SBATCH -p bigmem
# SBATCH --mem=200000

#SBATCH --ntasks=1                   # Run a single task        
#SBATCH --cpus-per-task=18            # Number of CPU cores per task


#SBATCH --get-user-env

#SBATCH --output=logs/{0}.out
#SBATCH --error=logs/{0}.err

/usr/bin/time -v -o times/{0}.log ./SOAPdenovo-63mer all -s sbatch_scripts/{0}.conf -K 63 -R -o results/{0}/res
''',
        'config':'''#maximal read length
max_rd_len=300
[LIB]
#average insert size
avg_ins={0}
#if sequence needs to be reversed
reverse_seq=0
#in which part(s) the reads are used
asm_flags=3
#use only first 100 bps of each read
rd_len_cutoff=300
#in which order the reads are used while scaffolding
rank=1
# cutoff of pair number for a reliable connection (at least 3 for short insert size)
pair_num_cutoff=3
#minimum aligned length to contigs for a reliable read location (at least 32 for short insert size)
map_len=32
#a pair of fastq file, read 1 file should always be followed by read 2 file
q1={1}
q2={2}
'''
    }
}

run_all = '''sbatch sbatch_scripts/cel
sbatch sbatch_scripts/cel_musket

sbatch sbatch_scripts/chl
sbatch sbatch_scripts/chl_musket

sbatch sbatch_scripts/eco
sbatch sbatch_scripts/eco_musket

sbatch sbatch_scripts/h14
sbatch sbatch_scripts/h14_musket

sbatch sbatch_scripts/lux
sbatch sbatch_scripts/lux_musket

sbatch sbatch_scripts/ara
sbatch sbatch_scripts/ara_musket
'''


def create_dirs(path):
    try:
        os.mkdir(path + 'logs')
    except:
        pass
    try:
        os.mkdir(path + 'results')
    except:
        pass
    try:
        os.mkdir(path + 'times')
    except:
        pass
    try:
        os.mkdir(path + 'sbatch_scripts')
    except:
        pass
    f = open(path + 'run_all', 'w')
    f.write(run_all)
    f.close()


# SAPDES
alg = algos['spades']
path = alg['path']
#path = 'spades/'
create_dirs(path)

for data in data_sets:
    name = data
    f1 = data_sets[data]['f1']
    f2 = data_sets[data]['f2']
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name, 'w')
    if name[0:3] == 'chl':
        f.write(alg['script'].format(name, f1, f2, ',99,127'))
    else:
        f.write(alg['script'].format(name, f1, f2, ''))
    f.close()

# MEGAHIT
alg = algos['megahit']
path = alg['path']
#path = 'megahit/'
create_dirs(path)

for data in data_sets:
    name = data
    f1 = data_sets[data]['f1']
    f2 = data_sets[data]['f2']
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name, 'w')
    f.write(alg['script'].format(name, f1, f2))
    f.close()

# SAGE
alg = algos['sage']
path = alg['path']
#path = 'sage/'
create_dirs(path)

for data in data_sets:
    name = data
    f1 = data_sets[data]['f1']
    f2 = data_sets[data]['f2']
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name + '.list', 'w')
    f.write('f1={}\nf2={}\n'.format(f1, f2))
    f.close()
    f = open(path + 'sbatch_scripts/' + name, 'w')
    f.write(alg['script'].format(name, path + 'sbatch_scripts/' + name + '.list'))
    f.close()

# READJOINER
alg = algos['readjoiner']
path = alg['path']
#path = 'readjoiner/'
create_dirs(path)

for data in data_sets:
    name = data
    f1 = data_sets[data]['f1']
    f2 = data_sets[data]['f2']
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name, 'w')
    f.write(alg['script'].format(name, f1, f2, ins))
    f.close()

# SGA (in udocker)
alg = algos['sga']
path = alg['path']
#path = 'sga/'
create_dirs(path)

for data in data_sets:
    try:
        os.mkdir(path + 'results/' + data)
    except:
        pass
    name = data
    f1 = data_sets[data]['f1'].split('/')[-1]
    f2 = data_sets[data]['f2'].split('/')[-1]
    dataset_path = '/'.join(data_sets[data]['f1'].split('/')[:-1])
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name, 'w')
    f.write(alg['script'].format(name, dataset_path, f1, f2))
    f.close()

# SOAP2
alg = algos['soap']
path = alg['path']
#path = 'soap/'
create_dirs(path)

for data in data_sets:
    try:
        os.mkdir(path + 'results/' + name)
    except:
        pass
    name = data
    f1 = data_sets[data]['f1']
    f2 = data_sets[data]['f2']
    ins = data_sets[data]['insert']
    f = open(path + 'sbatch_scripts/' + name + '.conf', 'w')
    f.write(alg['config'].format(ins, f1, f2))
    f.close()
    f = open(path + 'sbatch_scripts/' + name, 'w')
    f.write(alg['script'].format(name))
    f.close()

# CREATE link results
f = open('link_results.sh', 'w')
f2 = open('link_scaffols.sh', 'w')
for a in algos:
    for data in data_sets:
        if a != 'sage' and 'racer' in data: continue
        if a == 'spades' and 'musket' in data: continue
        file_name = algos[a]['contigs'].format(data)
        link = data_sets[data]['results'].format(a)
        f.write('ln -s {} {}\n'.format(file_name, link))
        if algos[a]['scaffolds'] != '':
            file_name = algos[a]['scaffolds'].format(data)
            link = data_sets[data]['results'].format('scaffolds/' + a)
            f2.write('ln -s {} {}\n'.format(file_name, link))
f.close()
f2.close()

# CREATE cleanup
f = open('cleanup.sh', 'w')
for a in algos:
    for data in data_sets:
        for tmp in algos[a]['clean']:
            f.write('rm -r {}results/{}/{}\n'.format(algos[a]['path'], data, tmp))
f.close()
