# reference_phylogenies

A repository of reference phylogenies for proteins and RNAs.

See subdirectories for working files, and copies of the files here for reference alignments, trees and model information for phylogenetic placement.

## Target sheet for nf-core/phyloplace

`phylosearch_targets.csv` is a target sheet for nf-core/phyloplace (`--phylosearch_input`, version 2.4.0 and later) with one row per reference phylogeny: `alkB`, `ring-hydroxylase_alpha`, `BMM_alpha` (alpha subunit of the soluble diiron monooxygenases) and `CuMMO_A` (A subunit of the copper membrane monooxygenases, archaeal and bacterial).
Each row has the profile for the search (`<name>.hmm`), the reference alignment (`<name>.alnfaa`, the alignment the tree was made from), the tree (`<name>.newick`), the model for EPA-ng and the classification (`<name>.classification.tsv`).
The profile is used both to search and to align the hits (`alignmethod` is `hmmer`), because the reference alignments are trimmed and Clustal Omega in profile mode put most hits in columns the reference lacks, which made EPA-ng stop with "does not appear to have any non-gap sites".
The paths are URLs to the files on the master branch, so a run needs no clone of this repository.

```bash
nextflow run nf-core/phyloplace -r dev -profile docker \
  --phylosearch_input https://raw.githubusercontent.com/LNUc-EEMiS/reference_phylogenies/master/phylosearch_targets.csv \
  --search_fasta [fasta file with the proteins to search] --outdir results
```

Several sheets are combined with a comma, for example with a sheet of your own profiles, and `--phylosearch_targets alkB` restricts the run to some of the targets.
Hits are ranked across all profiles that are searched for, so leaving a target out can change which sequences end up with another target.

The model for `alkB` is `LG+F+R8` with the fitted rates and weights written out (`LG+FC+R8{rates}{weights}`), because EPA-ng otherwise uses equal weights and its own rates for FreeRate models.
The model for `ring-hydroxylase_alpha` is `LG+G4`, the best model by corrected AIC that EPA-ng can use; the best by BIC was Q.pfam+I+I+R7.
The model for `BMM_alpha` is `LG+FO+R6`, the best model by BIC, with the fitted empirical frequencies and rates written out (`LG+FU{frequencies}+R6{rates}{weights}`).
The model for `CuMMO_A` is `LG+FO+G4` written as `LG+FU{frequencies}+G4m{alpha}`; ModelFinder preferred Q.yeast+FO+G4 (BIC 11 lower), which EPA-ng does not accept.

The classification files give each tip a path of clans separated by `;` (for example `BMM_alpha;alkane_monooxygenase;clan3_soluble_methane_and_butane_monooxygenase`), and the working directories hold a tree with the classification in the tip names (`<name>.classified.newick`) and a `README.md` with the methods.
"Clan" is used for a labelled set of tips that forms one side of a split of the unrooted tree; none of these trees is rooted.
