### Methods

Draft, 2026-11-18, built with Claude Code (Daniel Lundin supervising); the tree has been used for placement of metagenomic ORFs, not yet for anything else.
Target: the alpha subunit (hydroxylase large subunit) of the bacterial multicomponent soluble diiron monooxygenases (SDIMO, BMM): soluble methane monooxygenase, phenol hydroxylases, toluene/benzene/o-xylene monooxygenases, alkene monooxygenases, propane and tetrahydrofuran monooxygenases.
The intermediate files are in `/data/users/dl/bmm_trees/` on the annotation machine.

**Reference set.**
UniProt proteins of Pfam PF02332 (Phenol_Hydrox, which covers alpha and beta subunits) of 440 to 620 aa, downloaded 2026-11-18 (1379 entries, 10 of them Swiss-Prot).
Removed: fragments, entries named beta or small subunit, entries without two E-x-x-H motifs, lengths outside 470 to 600 aa (1368 left).
MMseqs2 `easy-cluster --min-seq-id 0.8 -c 0.8 --cov-mode 1` gave 165 representatives.
Added: all Swiss-Prot alpha subunits and 30 characterised or gene-named proteins that were not representatives (for example EtnC, ThmA of *Pseudonocardia tetrahydrofuranoxydans*, BmoX of *Thauera butanivorans*, TouA, TomA3, PhyC, PheN, several MmoX).
The result is 204 sequences (`ref_alpha.faa`; `ref_cluster_info.tsv` gives the cluster size and the gene names in each cluster; `tips.tsv` the UniProt name and organism of every tip).
All 204 have the six diiron ligands of MmoX of *Methylococcus capsulatus* (P22869: Glu114, Glu144, His147, Glu209, Glu243, His246, taken from the UniProt binding-site features) in the aligned columns.
Not found as sequences: the isoprene monooxygenase IsoA of *Rhodococcus* AD45, AmoC of *R. ruber* B-276, and group 7 (see below); the gene named `isoA` of *Mycolicibacterium gadium* (A0ABT6GKQ4) is in the reference by UniProt gene name only.

**Alignment and tree.**
MAFFT L-INS-i (`--localpair --maxiterate 1000`), 791 columns (`ref_alpha.linsi.alnfaa`).
BMGE 1.12 `-m BLOSUM30 -h 0.5 -g 0.2`, 325 columns (`../BMM_alpha.alnfaa`).
All six ligand columns are kept (checked on the hits, which carry the ligands in the trimmed profile too).
IQ-TREE 3.1.4, `-m MFP -mset LG,WAG,Q.pfam,JTT -mfreq F,FO -mrate G,R -cmax 6 -B 1000 -T 6`; best model by BIC `LG+FO+R6`, log-likelihood -51770.1, 1000 UFBoot replicates (`bmm.iqtree`, `bmm.log`, `bmm.contree`).
`../BMM_alpha.newick` is the ML tree with UFBoot values, unrooted (trifurcation at the root).
A first run that included the `LG+C20` mixture chose that model by BIC but was stopped after 13 iterations of the tree search as too slow, and EPA-ng cannot use a mixture; the tree here is from the single-matrix model.
`../BMM_alpha.models` is the model in EPA-ng syntax with the fitted frequencies (`FU`) and rates, because EPA-ng otherwise uses its own values for FreeRate models.
EPA-ng accepted the file and the tree and placed 20 ORFs (checked).

**Root.**
Alpha and beta subunits are paralogs that arose from an ancient duplication of a carboxylate-bridged diiron protein (Leahy et al. 2003).
Ten Swiss-Prot beta subunits (`beta_ref.faa`: TmoE, MmoY of two species, XamoE, small subunits MimC and PrmC of propane monooxygenases, DmpL, MhpL) were aligned with the 204 alpha subunits the same way (`rooting_alpha_beta.*`, LG+G4, 302 columns).
The beta subunits form one clade (UFBoot 100).
Rooted on that clade the alpha tree is rooted next to three sequences (`A0A1X0BAZ0`, `A0A2R4K2J8`, `A0ABV7L1W5`) with UFBoot 52 to 56, so the root is weakly supported; the tree is used unrooted for placement.
Alpha and beta are so divergent (about 20 to 25% identity) that the alignment between them is unreliable, and a long branch to the outgroup can pull the root to a wrong place; the root should not be relied on.
Distant ferritin-like proteins (ribonucleotide reductase R2, desaturase, rubrerythrin) were not included.

**Groups.**
The labels follow the seven groups of Yang, Kertesz and Coleman (2025, Environmental Microbiology 27:e70050, PMC11825192), which use the alpha-subunit phylogeny and the numbering of Holmes and Coleman (2008) (groups 1 and 2 are swapped relative to Notomista et al. 2003), and Leahy, Batchelor and Morcomb (2003, FEMS Microbiol Rev 27:449-479), who describe four groups (soluble methane monooxygenases, the Amo alkene monooxygenase, phenol hydroxylases, four-component alkene/aromatic monooxygenases).
I read the abstracts and the text of the open-access article by Yang et al.; Table S3 (accessions of their sequences) was not available, so the exemplars are chosen by the organisms and gene names the text gives and by the UniProt names.
Notomista et al. (2003, J Mol Evol 56:435-445) was not readable (paywall).
A label is given to the clade (the smallest clade in the rooted tree) that contains the exemplars of one group; tips outside every such clade are `unassigned`.

| Group in the file | Group of Yang et al. | Exemplars in the tree (accession) | Clade UFBoot | Tips |
|---|---|---|---|---|
| `group1_TMO` | 1, toluene MOs | TmoA *P. mendocina* KR1 (Q00456), Tbu *R. pickettii* (Q51939), TouA *P. stutzeri* OX1 (Q6IV66, O87798), XamoA *Xanthobacter* (O87082) | 91 | 55 |
| `group1_TMO;tmo_tbu_tou` | | Q00456, Q51939, Q6IV66 | 89 | 24 |
| `group1_TMO;xamo_iso` | 1, subgroup with propene and isoprene | O87082, XamoA of *Paraburkholderia hiiakae* | 97 | 11 |
| `group2_PhMO` | 2, phenol MOs | DmpN *Pseudomonas* CF600 (P19732), TomA3 *B. cepacia* G4 (Q8VSV8), PhyC *C. metallidurans* (Q1LMG3), PheN (Q84AQ2), PhcN and AphN *Comamonas* (Q9S147, Q9ZNP4) | 68 | 63 |
| `group3_sMMO_BMO` | 3, sMMO and relatives | MmoX of *M. capsulatus* and *M. trichosporium* (P22869, P27353), BmoX of *T. butanivorans* and *B. petroleovorans* (Q8KQF0, Q5VJ90) | 100 | 15 |
| `group4_alkene` | 4, alkene MOs | EtnC (Q6XBI6), AmoC of Halieaceae PE-TB08W (A0A3G9E9D5) | 96 | 6 |
| `group5_Pr2MO_THF` | 5, propane-2-MO and THF MO | PrmA of *Gordonia* TY-5 and *R. jostii* RHA1 (Q768T5, Q0SJK9), MimA (A0QTU8, E9RFS9), ThmA of *Pseudonocardia tetrahydrofuranoxydans* (Q9F3V6) | 100 | 18 |
| `group6_Pr1MO` | 6, propane-1-MO | *M. gadium* (A0ABT6GKR4) and *Mycobacterium* TY-6 (Q08KF2), organism-level assignment only | 99 | 7 |
| `unassigned` | | | | 40 |

Every group is monophyletic by construction (the clade is the smallest that holds its exemplars), and no exemplar of another group falls inside any of them.
Support is high for groups 3 to 6 and the two subgroups of group 1, and weak for group 2 (UFBoot 68).
Group 1 is a clade of 55 tips with UFBoot 91, but it also holds uncharacterised clades (13 actinobacterial tips annotated propane 2-monooxygenase, and tips of Sneathiella, Zavarzinia, Emcibacter and others that carry no characterised member), so the label says that they lie between the exemplars, not that they are toluene monooxygenases.
The 40 unassigned tips include a large clade (about 80 tips, many annotated propane 2-monooxygenase or YHS-domain protein, from Actinomycetota, Bacillota and Pseudomonadota) with no characterised member, and a clade of four sequences next to group 3 (three Mycobacteriaceae, including *Candidatus* Mycobacterium methanotrophicum, and *Oleomonas*); Yang et al. list an Smo of *Mycobacterium* NBB4 in group 3, but I have no accession for it, so I did not label this clade.
Group 7 (a new group defined in Yang et al. 2024) has no sequence in the reference: I did not find its definition or accessions.
The group 4 clade has only two exemplars, both from Yang et al.'s list, and group 6 rests on organism names; treat the groups 4 and 6 labels as provisional.

`BMM_alpha.classification.tsv` has the path for every tip (levels separated by `;`, as in the other targets), made with `label_groups.py` (a copy of the script; it reads `/data/users/dl/bmm_trees`).

**Profile and cut-offs.**
`../BMM_alpha.hmm` is `hmmbuild` of the trimmed alignment (325 match states, used both to search and to align hits to the reference, `alignmethod` hmmer); `BMM_alpha_full.hmm` is built from the untrimmed alignment (510 states) and is more sensitive for fragments that fall in the trimmed-away columns.
Self-search of the 204 references with the trimmed profile: lowest score 191.8 bits.
The ten Swiss-Prot beta subunits: nine do not reach E 1e-3 and one (TmoE, Q00460) scores 27.7 bits, so the beta subunits are not separated from distant members by a score but by identity: a hit is called an alpha subunit when it is at least 50% identical to a reference alpha subunit over at least 60 aa (BLASTP against the references).
Distant family members found by the profile score 30 to 36 bits and are 27 to 30% identical to the nearest reference alpha subunit; short true fragments of alpha subunits can score as low (32 to 42 bits for fragments of 108 to 191 aa), so scores below 100 bits need the identity check.
