### Methods

Draft, 2026-11-18, built with Claude Code (Daniel Lundin supervising); revised the same day (three long-branch tips removed, full ModelFinder run). The tree has been used for EPA-ng placement of the 29 CuMMO A ORFs of the antom_metaGT co-assembly as a test only.
The target is the A subunit of the copper membrane-bound monooxygenases (the 27 kDa subunit: `pmoA` of pMMO, `amoA` of bacterial and archaeal AMO, comammox *Nitrospira*, and relatives).
Beware the UniProt names: Swiss-Prot calls this subunit "alpha" for *N. europaea* AmoA (Q04507) and "beta" for *M. capsulatus* PmoA (Q607G3); the 45 kDa subunit (PmoB/AmoB, PF04744) is not part of this tree.

**Reference set.**
258 prokaryotic proteins from UniProt (queried 2026-11-18 over the REST API, 12,442 entries before filtering) that carry Pfam PF02461 (AMO, bacterial) or PF12942 (Archaeal_AmoA) in their UniProt cross-references.
Entries were removed if eukaryotic, viral or metagenome-derived, if bacterial and flagged fragment or shorter than 220 aa or longer than 310 aa, or if archaeal and outside 195 to 235 aa (archaeal AmoA is about 215 aa and almost all UniProt entries are flagged fragments of environmental amplicons, so the flag was not used for them).
Entries named "PmoA-like" (Pfam PF14100), "Ammonia monooxygenase gamma subunit" (PF02167, cytochrome c1 with a wrong name) and PmoC/AmoC (PF04896) were excluded because they lack PF02461 and PF12942; they are a distinct family (they get no hit from the profile at E = 1000).
The 2,985 entries left were clustered with MMseqs2 (`--min-seq-id` 0.95 for archaea, 0.9 for bacteria, 0.97 for the named, non-environmental entries of the target groups, `-c 0.8 --cov-mode 1`); the representative of a cluster is the member with the best evidence (Swiss-Prot, then a named source organism rather than an environmental sample, then protein or transcript evidence).
Swiss-Prot entries and the three entries with the gene name `pxmA` (F6K8L0, F6K8L1, K7SQA5; fragments of 179 to 197 aa, kept because they are the only pxmA-named proteins) are always kept.
Characterised seeds (Swiss-Prot or evidence at protein level): Q04507, A0A1H3PUN8, A0A1I5FI55 (*Nitrosomonas*/*Nitrosospira* AmoA), Q607G3, G4SZ63, Q50541 (PmoA of *Methylococcus*, *Methylotuvimicrobium*, *Methylosinus*).
No archaeal AmoA has protein-level evidence or a Swiss-Prot entry in UniProt; 121 of the 137 archaeal tips are environmental amplicon sequences ("uncultured crenarchaeote" and similar) with no lineage below Archaea or Nitrososphaerota.
Butane monooxygenases of *Thauera* and *Brachymonas* (BmoX, about 530 aa) are the soluble diiron type, not CuMMO, and are not in the set; the only tip named hydrocarbon monooxygenase is A0ABX2K470 (*Mycolicibacterium sphagni*, labelled `hydrocarbon_MO;Actinomycetota`), and the hydrocarbon-named entries from marine metagenomes were excluded as metagenome-derived.
No USC-alpha or USC-gamma sequence could be identified from UniProt names.
Files: `CuMMO_A.faa` (sequences), `CuMMO_A.taxonomy.tsv` (organism, lineage, protein name, evidence, cluster size, label of each tip).

**Alignment and tree.**
MAFFT 7 L-INS-i (`mafft --localpair --maxiterate 1000`; `CuMMO_A.linsi.untrimmed.alnfaa`, 335 columns), trimmed with BMGE (`-t AA -m BLOSUM30 -g 0.2`, the default entropy cut-off) to 196 columns (`CuMMO_A.alnfaa`, `CuMMO_A.bmge.log`).
Stricter gap rates were tried; BLOSUM30 and the default maximum gap rate of 0.2 keep columns that are almost gap free in all 258 sequences, so nearly every tip has residues in nearly all retained columns, and a 150 to 200 aa fragment that spans the core does too.
Removed from the first version of the set (258 left of 261): A0A7D5R6V2, A5HAX7 and A9Q6C9, the three longest branches of the 261-tip tree (branch lengths 2.25, 0.57 and 0.94; `CuMMO_A.removed.tsv`).
A0A7D5R6V2 (*Nitrosopumilus ureiphilus*) has a locus-tag gene name, the UniProt protein name is "HTH arsR-type domain-containing protein", and it is 29% identical to the *N. maritimus* amoA, so it is probably not an amoA; A9Q6C9 (*Methylacidiphilum fumariolicum* pmoA3, Verrucomicrobiota) and A5HAX7 (uncultured crenarchaeote) were removed only for branch length.
They are not in `CuMMO_A.faa` or the taxonomy table.
IQ-TREE 3.1.4 ModelFinder (`-mset LG,WAG,JTT,VT,Blosum62,Q.pfam,Q.yeast,Q.insect,rtREV,cpREV,mtREV,DCMut -mfreq ,F,FO -mrate E,I,G,I+G,R -cmax 10`; no mixture models; BIC with sample size 196; `modelfinder/CuMMO_A.modelfinder_bic.tsv`, 289 models) chose Q.YEAST+FO+G4 (BIC 43,149; ModelFinder tested R2 to R5 only, because R5 was worse than R4 for every matrix it reached, so R6 to R10 were never run and R9 and R10 did not compete; the best R model, Q.YEAST+FO+R4, has BIC 43,154, 5 above the best model).
EPA-ng has no Q.yeast matrix (`Invalid model name: Q.YEAST`), so the reference tree is the ML tree under the best model that EPA-ng can use, LG+FO+G4 (BIC 43,160, 11 above the best; gamma alpha 2.0043, log-likelihood -20,049.0; `iqtree -s CuMMO_A.alnfaa -m LG+FO+G4 -B 1000 -bnni`; `CuMMO_A.iqtree`, `CuMMO_A.iqtree.log`).
The tree under Q.YEAST+FO+G4 (log-likelihood -20,049.4) is kept in `modelfinder/`.
`CuMMO_A.newick` is the unrooted LG+FO+G4 tree with UFBoot support on the branches; `CuMMO_A.contree` is the 1000-replicate consensus tree; `CuMMO_A.classified.newick` has the tip names `accession|classification` with `;` replaced by `_`.
The model string for EPA-ng is in `CuMMO_A.models`: `LG+FU{<ML amino acid frequencies>}+G4m{2.0043}`, the IQ-TREE model written out (the frequencies are the +FO estimates; `LG+FO+G4` alone is also accepted and then EPA-ng estimates them itself).
Tested with EPA-ng 0.3.8 and gappa on the 29 CuMMO A ORFs of the antom_metaGT co-assembly (hits of the handmade profile, aligned with hmmalign to `CuMMO_A.hmm` with insert columns dropped): EPA-ng accepts the tree, alignment and model; `placement/` has the jplace file and the gappa per-query table.
All 29 ORFs place in the expected groups: 22 in `AMO_archaeal`, 1 in `AMO_bacterial;AOB_Betaproteobacteria`, 6 in `other_PF02461;Pseudomonadota` (gappa `examine assign`, accumulated normalised LWR at least 0.8); the archaeal ORFs are not resolved below `AMO_archaeal`.
The longest branch of this tree is A0A4Z0F839 (0.599; a tip of `other_PF02461`), then A0A1C3X0K8 (0.499) and A0A2M8R783 (0.435).

**Root.**
The archaeal tips form a clade separated from the bacterial tips by one edge of the ML tree (UFBoot 100), and `CuMMO_A.rooted.newick` is rooted on that edge.
That root is a choice (the bacterial and archaeal families have no outgroup here), not a result; use the unrooted tree for EPA-ng.
Support values on the nodes of the path between the original and the new root of the rooted copy are not reliable; read supports from `CuMMO_A.newick`.

**Labels and support.**
`CuMMO_A.classification.tsv` labels every tip from the NCBI lineage and the protein name in UniProt, nothing from memory: `CuMMO_A;AMO_archaeal;<order or genus>` (Nitrosopumilales, Nitrososphaerales, Nitrosotaleales, Nitrosocaldales, Cenarchaeales, Marine Group I, Nitrosotenuis), `CuMMO_A;AMO_bacterial;AOB_Betaproteobacteria` (Nitrosomonadaceae), `...;AOB_Gammaproteobacteria` (*Nitrosococcus*, *Nitrosoglobus*, *Nitrosacidicoccus*), `...;comammox_Nitrospira` (Nitrospiraceae; clade A and B are not separated because the three tips are all in one clade and no UniProt entry states the clade), `CuMMO_A;pMMO;typeI_Methylococcales`, `pMMO;typeII;Methylocystaceae` and `Beijerinckiaceae`, `pMMO;Verrucomicrobiota` (Methylacidiphilae), `pMMO;Methylomirabilota`, `CuMMO_A;hydrocarbon_MO;Actinomycetota` and `CuMMO_A;other_PF02461;<phylum>` for tips from other bacteria.
Archaeal tips without a lineage below Archaea or Nitrososphaerota are `AMO_archaeal;unspecified` or `AMO_archaeal;Nitrososphaerota_unspecified`; they are the majority of the archaea.
`pMMO;pxmA` are the three tips with the UniProt gene name `pxmA` (two Methylococcales, one environmental sequence); they fall among type I Methylococcales tips in a clade with UFBoot 35, so the pxmA label is not supported as a clade here.
The tree has a clade of Methylococcales and *Methylocystis* tips (6 tips, UFBoot 95) that mixes the type I and type II labels.

Monophyly (from `scripts/tree_check.py` on the tree rooted as above, full output `CuMMO_A.monophyly.tsv`; UFBoot of the clade edge):

| Label | Tips | Result |
|---|---|---|
| archaeal against bacterial tips | 135, 123 | split by one edge, UFBoot 100 |
| `AMO_archaeal;Nitrosocaldales` | 2 | not monophyletic (split by the basal bifurcation of the archaeal clade) |
| `AMO_archaeal;Nitrosotaleales` | 2 | not monophyletic: the clade also holds 2 environmental amplicons (UFBoot 86) |
| `AMO_archaeal;Nitrosopumilales` (4), `Nitrososphaerales` (3), the unspecified labels | | not monophyletic; the backbone of the archaeal tree is poorly supported (many UFBoot values below 50) |
| `AMO_bacterial;AOB_Betaproteobacteria` | 17 | monophyletic, UFBoot 97, sister to comammox Nitrospira (UFBoot 100 for the pair) |
| `AMO_bacterial;AOB_Gammaproteobacteria` | 6 | monophyletic, UFBoot 100, inside a 53-tip clade with the Methylococcales, Methylocystaceae and Beijerinckiaceae (UFBoot 94) |
| `comammox_Nitrospira` | 3 | monophyletic, UFBoot 100 |
| `pMMO;Verrucomicrobiota` | 10 | monophyletic, UFBoot 100 |
| `pMMO;Methylomirabilota` | 2 | monophyletic, UFBoot 100 |
| `pMMO;typeII;Methylocystaceae` and `Beijerinckiaceae` | 18, 2 | not separate clades: the type II tips are inside the 53-tip clade (UFBoot 94) together with Methylococcales and gamma AOB tips |
| `pMMO;typeI_Methylococcales` | 42 | not monophyletic (the gamma AOB and the type II tips are inside the same clade) |
| `pMMO;pxmA` | 3 | not monophyletic (UFBoot 34) |
| `other_PF02461` | 19 | not monophyletic |

Changes against the first tree (261 tips, LG+F+I+G4): the Verrucomicrobiota clade (10 tips) is 100 (was 99), beta AOB 97 (98), the Methylocystaceae and Beijerinckiaceae tips are no longer a separate clade but part of a 53-tip clade (UFBoot 94; the earlier 16-tip clade had 89), Nitrosocaldales are no longer a clade (was UFBoot 93), the 6 Actinomycetota and Bacillota tips moved from the base of the bacterial clade to a clade next to the Verrucomicrobiota (UFBoot 54), and the longest branch is A0A4Z0F839 (0.599, was A0A7D5R6V2 with 2.25).
The backbone between the large groups has UFBoot values of 27 to 62; trust the labels with supported clades and use the nearest-reference identity, not the deep topology, for the others.

**Search profiles.**
`CuMMO_A.hmm` (hmmbuild of `CuMMO_A.alnfaa`, 196 positions, so it matches the alignment hmmalign maps hits to); `CuMMO_A_archaeal.hmm` and `CuMMO_A_bacterial.hmm` are the same alignment split by domain, for searching only.
Over 7,374 UniProt PF02461/PF12942 proteins the combined profile gives a hit for all (the profile was built from 258 of them, so this is not an independent test); 900 proteins of PF14100, PF04896, PF04744 and PF02167 give no hit at E = 1000.

Re-run: `scripts/pool.R`, `select_reps.R`, `label_refs.R` (paths on the annotation machine, `/data/users/dl/cummo_trees/`) built the reference set; the sequences, alignment and tree are all here.
