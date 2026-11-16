### Methods

Draft, 2026-11-14, built with Claude Code (Daniel Lundin supervising); the tree has not yet been used for placement.

**Collection.**
All 36,143 prokaryotic UniProtKB proteins annotated with Pfam PF00487 (fatty acid desaturase; taxonomy 2 and 2157; UniProt release of 2026-11-13) were searched with the `alkB` HMM profile of the antom metatdenovo run (`hmmsearch`, HMMER 3.3.2).
That profile was built in 2019 from three sequences, so it is narrow.
4,086 proteins scored E < 1e-20; 3,524 of them are 330 to 470 aa long and make up the AlkB-family set (329 shorter and 233 longer proteins were dropped as fragments or proteins with inserts or extra domains).

**Reduction.**
The family set was clustered with MMseqs2 (`easy-cluster`, `--min-seq-id 0.6 -c 0.8 --cov-mode 0`, release 18.8cc5c) into 360 clusters, and the representatives were kept.
At 0.6 the family is not redundant: 172 of the 360 clusters are singletons.

**Seeds.**
The 7 Swiss-Prot "Alkane 1-monooxygenase" entries and XylM (P21395) were added, together with 22 more full-length (370 to 440 aa) proteins from papers on cloned or characterised alkane hydroxylases and the AlkB structure paper (`seeds_literature.tsv`; the evidence column is the first journal title in UniProt, so it is title-level evidence and has not been checked paper by paper).
Amplicon-length entries (80 to 215 aa) from PCR screening papers were left out.
Six desaturase representatives (the largest clusters of PF00487 proteins outside the family set, clustered at 0.3) were added as outgroup.
Final set: 396 sequences (`final_sequences.faa`, roles in `final_sequences.tags.tsv`).

**Alignment and tree.**
Clustal Omega 1.2.4 alignment (931 columns), 205 columns kept with BMGE (BLOSUM30; median sequence has residues in all of them, the outgroups in 76 to 90%).
IQ-TREE 3.1.4, `iqtree -s final_sequences.co.BLOSUM30.bmge.alnfaa -B 1000 -nt 8 -m MFP -mset LG,WAG,JTT,VT,Dayhoff,DCMut,JTTDCMut,BLOSUM62,RTREV,CPREV -mrate G,I+G`.
The model set was restricted to standard empirical matrices (those EPA-ng can use) because the full ModelFinder set did not finish in two hours on a loaded machine.
Best model by BIC: LG+F+I+G4.
The ultrafast bootstrap ran its 1000 replicates without meeting the convergence criterion (correlation coefficient 0.988), so the support values are approximate; rerun with `-nm` higher before relying on them.

**Clans.**
`alkB.classification.tsv` assigns tips to clans from the seeds: the smallest split of the tree that holds a set of seeds and none of the outgroup side.

| Clan | Tips | UFBoot | Seeds |
|---|---|---|---|
| `clanA` GPo1-like (mostly Proteobacteria) | 65 | 91 | *P. oleovorans* GPo1 and *P. putida* AlkB, *Acinetobacter* AlkM, *Alcanivorax* AlkB1, *A. dieselolei*, *Burkholderia* RR10, *P. fluorescens*, *Fontimonas* AlkB (structure) |
| `clanB` Actinobacterial | 33 | 94 | *Rhodococcus* AlkB1 to 4 (Q15 and *R. erythropolis*), *R. ruber*, *R. aetherivorans*, *Gordonia* |
| `clanC` AlkB2-like | 6 | 90 | *Alcanivorax* AlkB2, *P. aeruginosa* AlkB1 and AlkB2 |
| `xylM` | 1 | | XylM |
| `unassigned` | 285 | | none |

### Cautions

- Only about a quarter of the AlkB-family sequences are in a seeded clan; 285 of 376 have no characterised sequence close by, so most placed queries will be "AlkB family, function not known".
- The outgroup does not form a clean clade: the smallest split holding the six desaturases also holds 14 AlkB-family sequences (UFBoot 76), so the position of the root is uncertain.
- XylM is at the periphery of the family (it scored E = 8e-30 against the profile) and its position in the tree is not supported.
- Function is inferred from the seeds; most are named alkane hydroxylases from cloning or expression papers, and a few were never tested for activity.
- The family set came from PF00487 and so contains almost no archaea (2 proteins).
- Sequences identical to a seed were removed from the representatives.
- The model for placement is LG+F+I+G4; check that EPA-ng accepts it as written, otherwise use LG+G4.

### Files

`final_sequences.faa`, `final_sequences.co.alnfaa` (Clustal Omega), `final_sequences.co.BLOSUM30.bmge.alnfaa` (masked, root symlink `alkB.alnfaa`), `final_sequences.co.BLOSUM30.bmge.iqtree.treefile` (root symlink `alkB.newick`), `alkB.classification.tsv`, `alkB.models`, `seeds_literature.tsv`, `clans.json`.
Intermediate files (the cluster tables, the HMM search table, the discarded full ModelFinder run) are in `/data/users/dl/alkb_reference/` on the annotation machine.
