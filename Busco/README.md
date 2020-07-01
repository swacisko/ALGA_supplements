You need to install some software to test your data with Busco software. To achieve results from the ALGA article, you need to perform the following commands.

```bash
	apt install docker.io 
	sudo usermode -a -G docker.io [username] 
	docker pull ezlabgva/busco:v4.0.5_cv1 
	docker build ezlabgva/busco:v4.0.5_cv1
```

To check whether busco is properly installed try:

```bash
	docker run -v $(pwd):/busco_wd ezlabgva/busco:v4.0.5_cv1 --list-datasets
```


Finally you need to run commands acording to the following command structure:

```bash
	docker run -v $(pwd):/busco\_wd ezlabgva/busco:v4.0.5\_cv1 busco -f -m genome -i /busco_wd/[Contig_file].fasta -o [busco_working_directory_for_given_dataset] --lineage_dataset [dataset_from_datasets_list]
```

Where: 
* [Contig\_file].fasta is a file containing contigs in proper FASTA format. 
* [busco\_working\_directory\_for\_given\_dataset] is an arbitrarily chosen name of a directory, where Busco performs all calculations and stores the results. 
* [dataset\_from\_datasets\_list] is a name from "--list-datasets" command. 

Lastly, we checked the results in [busco\_working\_directory\_for\_given\_dataset]/short\_summary.[\*\*\*].txt.
There should be only one file following that patter, the name of which depends on the specif command that you run.
