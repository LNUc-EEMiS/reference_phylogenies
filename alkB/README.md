### Methods

Draft, 2026-11-17, built with Claude Code (Daniel Lundin supervising); the tree has not yet been used for placement.
This replaces the 396-sequence tree of 2026-11-14 (in git history, commit 4fdf3cf).

**Reference set.**
934 prokaryotic proteins of the Pfam PF00487 superfamily (fatty acid desaturase, which includes AlkB): 29 seeds (Swiss-Prot "Alkane 1-monooxygenase" entries and full-length proteins from papers on cloned or characterised alkane hydroxylases, `seeds_literature.tsv`), representatives of the AlkB family found with the `alkB` HMM and clustered with MMseqs2, and representatives of the rest of PF00487 (desaturases and related enzymes) (`ref_pf00487.faa`).
The superfamily is much larger than the AlkB-like part, so the tree has many more desaturase-type sequences than the earlier one.
The tree is unrooted; "clan" is used for a group of tips that is monophyletic under some rooting (Wilkinson et al. 2007), not "clade".
The intermediate files (cluster tables, HMM search tables, earlier trees) are in `/data/users/dl/alkb_reference/pf00487/` on the annotation machine; the steps that built the reference set before the alignment are recorded there, not repeated here.

**Alignment and tree.**
`hmmalign` of the sequences to PF00487 (`PF00487.hmm`), trimmed with BMGE to 218 columns (`ref_pf00487.hmm.trim.alnfaa`).
IQ-TREE 3.1.4, `iqtree -s ref_pf00487.hmm.trim.alnfaa -m LG+F+R8 -t ref_pf00487.G4I.ml.treefile -B 1000 -nm 3000 -nt 16`, started from the ML tree of an LG+F+I+G4 run; the tree is `ref_pf00487.R8.iqtree.treefile` (copied to `../alkB.newick`), log-likelihood -362,030.8.
The LG+F+I+G4 and LG+F+R8 trees give the same clades in the tests below.
LG+F+R8 was chosen by BIC in ModelFinder on the same alignment (`-mset LG -mfreq F -mrate G,I+G,R -cmax 8`, so at most 8 FreeRate categories were tried); EPA-ng takes it only with the fitted values given explicitly (`alkB.models`), otherwise it uses equal weights and its own rates.

**Clans.**
The seeds define a clan of 205 tips (clans A to D, UFBoot 79) that holds all 29 seeds and no sequence without an AlkB annotation.
Within it there are three large clans with working names: `clanAB` (which holds `clanA` and `clanB`), `clanC` and `clanD`.
Next to it, and each separated from the rest by a supported edge, are `clanE` (87 tips) and `clanF` (70 tips) with no or one characterised sequence, and four clans of desaturase-type sequences, `clanG` to `clanJ`, that have characterised members of other functions.
The names are working labels and can change when the sequences are better known.
`alkB.classification.tsv` assigns every tip (levels separated by `;`), `alkB.clades.tsv` gives the clan names without the `clanAB` level, with the tag, and `alkB.taxonomy.tsv` has the UniProt organism, lineage and protein name of all 934 tips (UniProt lookup of 2026-11-17).
Classes of tips in no clan are `unresolved` (12 tips next to A to F) and `PF00487_other;superfamily` (52 tips in none of the clans above).

| Clan | Tips | UFBoot | Subclans | Taxa | Characterised members | Function |
|---|---|---|---|---|---|---|
| `clanAB` | 100 | 93 | `clanA` and `clanB` | Proteobacteria and Actinomycetes | those of A and B | AlkB-type alkane hydroxylases |
| `clanA` | 66 | 97 | A1 (45; A1a 24, A1b 21), A2 (8); 13 tips in none | Proteobacteria. A1a mostly Alphaproteobacteria (Hyphomicrobiales, Parvularculales, Rhodobacterales), A1b Gamma- and Betaproteobacteria (Oceanospirillales, *Marinobacter*, *Alloalcanivorax*), A2 *Acinetobacter* and relatives | GPo1 (*P. oleovorans*), *P. putida*, *Alcanivorax* AlkB1, *Acinetobacter* AlkM, *Fontimonas* AlkB, *Burkholderia* | AlkB-type alkane hydroxylases |
| `clanB` | 34 | 91 | B1 (21), B2 (13) | Actinomycetes: *Rhodococcus*, *Gordonia*, *Mycobacteriales* | *Rhodococcus* AlkB1 to 4 and AlkB7, *Gordonia* | AlkB-type alkane hydroxylases |
| `clanC` | 23 | 100 | C1 (9, UFBoot 99); 14 tips in none | Gammaproteobacteria (Oceanospirillales, Burkholderiales, *Alcanivorax*, *Thalassolituus*, *Pseudomonas*) | *Alcanivorax* AlkB2, *P. aeruginosa* AlkB1 and AlkB2 | likely alkane hydroxylases |
| `clanD` | 70 | 92 | D1 (56, UFBoot 95), D2 (14) | D1 Bacteroidota (Cytophagia 18, Flavobacteriia 15, Saprospiria 5) and Gammaproteobacteria (Methylococcales 8, *Vibrio*, *Microbulbifer*); D2 Cytophagia and *Leptospira* | none | likely alkane hydroxylases (no seeds; inferred from the tree position) |
| `clanE` | 87 | 90 | none | Alphaproteobacteria, 86 of 87, marine Roseobacter-type (*Aquimixticola*, *Ascidiaceihabitans*, *Seohaeicola*, *Actibacterium*, *Cereibacter*) | none | hypothetical alkane hydroxylases |
| `clanF` | 70 | 100 | none | Pseudomonadota, 66 of 70 (Gammaproteobacteria 42, Betaproteobacteria 13, Alphaproteobacteria 11; Burkholderiales, Alteromonadales, Chromatiales, Nevskiales); 40 annotated alkane 1-monooxygenase, 19 fatty acid desaturase | XylM (*P. putida*, xylene/toluene monooxygenase) | hypothetical alkane hydroxylases (anchored only by XylM, a methyl hydroxylase) |
| `clanG` | 115 | 95 | G1 (62, UFBoot 96), G2 (42, UFBoot 95); 11 tips in none | Pseudomonadota 37, Bacteroidota 23, Cyanobacteriota 20 | cyanobacterial acyl-lipid desaturases (G1 delta-6; G2 delta-12 and omega-3), *B. subtilis* delta-5 (G2), *M. tuberculosis* stearoyl-CoA delta-9 (G1) | fatty-acid desaturases |
| `clanH` | 63 | 100 | H1 (55, UFBoot 100), H2 (8, UFBoot 100) | Pseudomonadota 26, Myxococcota 9, Actinomycetota 7 | delta-9 desaturases (*Synechocystis*, *Anabaena*, *Nostoc*), acyl-carrier-protein acetylenases (*Moorena*, *Teredinibacter*) | fatty-acid desaturases and acetylenases |
| `clanI` | 312 | 92 | I1 (209, UFBoot 99), I2 (103, UFBoot 97) | Pseudomonadota 166, Actinomycetota 29, Myxococcota 25 | I1: ceramide hydroxylase (*Caulobacter*), dihydrorhizobitoxine desaturase (*Bradyrhizobium*); I2: none, five tips annotated beta-carotene hydroxylase | desaturases and lipid or carotenoid hydroxylases |
| `clanJ` | 30 | 97 | none | Pseudomonadota 12, Myxococcota 7, Actinomycetota 3; annotated fatty acid desaturase | none | unknown |
| `unresolved` | 12 | | | mixed (Neisseriales, Legionellales, Verrucomicrobiota, Acidobacteriota) | none | unknown |

Clans A and B are sister clans (`clanAB`, UFBoot 93); A (97) and B (91) are supported separately, and the loose tip A0ACE2LTZ7 joins them at UFBoot 100 (101 tips).
The 14 unlabelled C tips and the 13 A tips outside A1 and A2 do not form clans of their own.
A tip of the old `clanB` label (A0ACE2LTZ7) lies outside the 34-tip clan and is `unresolved`.
Clan E (UFBoot 90 for A to D plus three loose tips plus E) has no seed; all 87 tips are unreviewed and inferred from homology, 80 are annotated alkane 1-monooxygenase and 8 fatty acid desaturase by automatic annotation.
Clan F (UFBoot 100; the edge joining A to D, E and F has UFBoot 72) holds XylM (P21395), the only characterised member.
The clans G to I contain 19 sequences with reviewed or experimental entries (two beta-carotene ketolases of *Paracoccus* lie outside all clans); all have desaturase, acetylenase or hydroxylase functions on lipids or carotenoids, and none is an alkane hydroxylase.
Clan J has no characterised member.

### Cautions

- Clans C and D are called "likely" alkane hydroxylases because they sit in one supported series of clades with A and B (A+B, D, C, each at UFBoot above 90); D has no seed, and the two *P. aeruginosa* seeds of C have only title-level evidence.
- Clans E and F are called hypothetical alkane hydroxylases because of their position next to the seeded clans and the automatic annotation; E has no functional indication of its own, and F has one (XylM, a methyl hydroxylase), so activity on alkanes is not shown for either.
- The names refer to this tree; the tree is unrooted, and how A+B, C, D, E and F are related to each other is not resolved.
- The clans G to I are annotated by characterised members of other functions; a placement there is most likely not an alkane hydroxylase, but a few sequences of the clans are not characterised, and clan J has none.
- The edge around A to D has UFBoot 79, and the ultrafast bootstrap converged (correlation coefficient 0.994).
- Function is inferred from the seeds; a few seeds were never tested for activity.
- The family set came from PF00487 and so contains almost no archaea.

### Files

`ref_pf00487.faa`, `ref_pf00487.hmm.trim.alnfaa` (copied to `../alkB.alnfaa`), `PF00487.hmm`, `ref_pf00487.R8.iqtree.{treefile,contree,iqtree}`, `alkB.models`, `alkB.classification.tsv`, `alkB.clades.tsv`, `alkB.taxonomy.tsv`, `alkB.classified.newick` (the tree with the classification in the tip names), `seeds_literature.tsv`.
Copies of these files for phylogenetic placement are in the root of the repository (`alkB.{alnfaa,hmm,newick,models,classification.tsv}`) and must be updated when the files here change; `../phylosearch_targets.csv` points to them.
