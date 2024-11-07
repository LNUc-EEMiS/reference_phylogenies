### Methods

We downloaded all sequences from Uniprot/TrEMBL (The Uniprot Consortium 2021; 2023-01-12) annotated as containing both the PF00848 (Ring hydroxylating alpha subunit (catalytic domain)) and PF00355 (Rieske [2Fe-2S] domain) Pfam (Finn et al. 2008) profiles, in total 39092 sequences.
Sequences were subsequently clustered with Usearch (v11.0.667_i86linux32; Edgar 2010) with an `id` parameter of 0.80 resulting in 9791 sequences.
Clusters with 10 sequences or fewer were removed as rare sequence types often are highly divergent and typically provide little insight into the main phylogenetic history of proteins.
After also removing sequences marked "Fragment" in Uniprot 549 sequences remained.
To this set of sequences, all PF00848-PF0355 sequences from Uniprot/Swiss-Prot (2023-01-12) were added to give a total of 591 sequences for phylogenetic analysis.

The sequences were aligned with Clustal Omega (Sievers et al. 2011) and 94 trustworthy positions were identified with BMGE (Criscuolo and Gribaldo 2010) using the BLOSUM30 matrix.
A maximum likelihood phylogeny was estimated with IQ-TREE (Nguyen et al. 2015) in "extended model selection followed by tree inference" (`-m MFP`) mode, 1000 ultrafast bootstrap replicates (`-B 1000`), 900 of which were performed before convergence.
Command line for IQ-TREE: `iqtree -s final_sequences.co.BLOSUM30.bmge.alnfaa -B 1000 -nt AUTO -m MFP --prefix final_sequences.co.BLOSUM30.bmge.iqtree.MFP`.
The best fitting model according to Akaike and Bayesian Information Criterion was Q.pfam+I+I+R7 and LG+G4 according to Corrected Akaike Information Criterion.

Functional groups in clans _sensu_ Wilkinson et al. (2007) were identified based on manually curated SwissProt sequences (see `ring-hydroxylase_alpha.classification.tsv.

The phylogeny can be used to identify e.g. poly-aromatic hydrocarbon-dioxygenases using [nf-core/phyloplace](https://nf-co.re/phyloplace) with the following command:

```bash
nextflow run nf-core/phyloplace -r 1.0.0 -profile <docker>/<singularity>/<other opts> \
  --outdir results --queryseqfile your_sequences.faa \
  --refseqfile https://raw.githubusercontent.com/LNUc-EEMiS/reference_phylogenies/refs/heads/master/ring-hydroxylase_alpha.alnfaa \
  --refphylogeny https://raw.githubusercontent.com/LNUc-EEMiS/reference_phylogenies/refs/heads/master/ring-hydroxylase_alpha.newick \
  --taxonomy https://raw.githubusercontent.com/LNUc-EEMiS/reference_phylogenies/v1.0/ring-hydroxylase_alpha.classification.tsv \
  --model LG+G4 --max_memory 24.GB
```

In the above command, the file `your_sequences.faa` should contain protein sequences to place, possibly the result of running
`hmmsearch` from the HMMER software package (Eddy 2011) with the Pfam PF00848 hmm profile (Finn et al. 2008).
The `--max_memory` parameter can be set to higher or smaller values, depending on your hardware.
Results will be written to subdirectories of `results/`, primarily `results/gappa`.
The classification can be found in `results/gappa/placement.taxonomy.per_query.tsv`.
_Note_ that the classification file often contains multiple alternative assignments, choose the one with maxiumum `LWR`.

### References

Criscuolo, Alexis, and Simonetta Gribaldo. “BMGE (Block Mapping and Gathering with Entropy): A New Software for Selection of Phylogenetic Informative Regions from Multiple Sequence Alignments.” BMC Evolutionary Biology 10 (2010): 210. https://doi.org/10.1186/1471-2148-10-210.

Eddy, Sean R. 2011. “Accelerated Profile HMM Searches.” PLoS Comput Biol 7 (10): e1002195. https://doi.org/10.1371/journal.pcbi.1002195.

Edgar, Robert C. “Search and Clustering Orders of Magnitude Faster than BLAST.” Bioinformatics 26, no. 19 (October 1, 2010): 2460–61. https://doi.org/10.1093/bioinformatics/btq461.

Finn, R. D, J. Tate, J. Mistry, P. C Coggill, S. J Sammut, H. R Hotz, G. Ceric, et al. “The Pfam Protein Families Database.” Nucleic Acids Res 36, no. Database issue (January 2008): D281-8.

Nguyen, Lam-Tung, Heiko A. Schmidt, Arndt von Haeseler, and Bui Quang Minh. “IQ-TREE: A Fast and Effective Stochastic Algorithm for Estimating Maximum-Likelihood Phylogenies.” Molecular Biology and Evolution 32, no. 1 (January 2015): 268–74. https://doi.org/10.1093/molbev/msu300.

Sievers, F., A. Wilm, D. Dineen, T. J. Gibson, K. Karplus, W. Li, R. Lopez, et al. “Fast, Scalable Generation of High-Quality Protein Multiple Sequence Alignments Using Clustal Omega.” Molecular Systems Biology 7, no. 1 (October 11, 2011): 539–539. https://doi.org/10.1038/msb.2011.75.

The UniProt Consortium, Alex Bateman, Maria-Jesus Martin, Sandra Orchard, Michele Magrane, Rahat Agivetova, Shadab Ahmad, et al. “UniProt: The Universal Protein Knowledgebase in 2021.” Nucleic Acids Research 49, no. D1 (January 8, 2021): D480–89. https://doi.org/10.1093/nar/gkaa1100.

Wilkinson M, McInerney JO, Hirt RP, Foster PG, Embley TM. Of clades and clans: terms for phylogenetic relationships in unrooted trees. Trends Ecol Evol (Amst). 2007 Mar;22(3):114–5. 
