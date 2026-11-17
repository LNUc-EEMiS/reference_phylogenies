### Methods

Draft, 2026-11-17, built with Claude Code (Daniel Lundin supervising); the tree has not yet been used for placement.
This replaces the 396-sequence tree of 2026-11-14 (in git history, commit 4fdf3cf).

**Reference set.**
934 prokaryotic proteins of the Pfam PF00487 superfamily (fatty acid desaturase, which includes AlkB): 29 seeds (Swiss-Prot "Alkane 1-monooxygenase" entries and full-length proteins from papers on cloned or characterised alkane hydroxylases, `seeds_literature.tsv`), representatives of the AlkB family found with the `alkB` HMM and clustered with MMseqs2, and representatives of the rest of PF00487 as the outgroup (`ref_pf00487.faa`).
The superfamily is much larger than the family, so the family root is placed by the outgroup instead of by a few desaturases as in the earlier tree.
The intermediate files (cluster tables, HMM search tables, earlier trees) are in `/data/users/dl/alkb_reference/pf00487/` on the annotation machine; the steps that built the reference set before the alignment are recorded there, not repeated here.

**Alignment and tree.**
`hmmalign` of the sequences to PF00487 (`PF00487.hmm`), trimmed with BMGE to 218 columns (`ref_pf00487.hmm.trim.alnfaa`).
IQ-TREE 3.1.4, `iqtree -s ref_pf00487.hmm.trim.alnfaa -m LG+F+R8 -t ref_pf00487.G4I.ml.treefile -B 1000 -nm 3000 -nt 16`, started from the ML tree of an LG+F+I+G4 run; the tree is `ref_pf00487.R8.iqtree.treefile` (root symlink `alkB.newick`), log-likelihood -362,030.8.
The LG+F+I+G4 and LG+F+R8 trees give the same clades in the tests below.
LG+F+R8 was chosen by BIC in ModelFinder on the same alignment (`-mset LG -mfreq F -mrate G,I+G,R -cmax 8`, so at most 8 FreeRate categories were tried); EPA-ng takes it only with the fitted values given explicitly (`alkB.models`), otherwise it uses equal weights and its own rates.

**Clades.**
The AlkB family is the clade of 205 tips that holds all 29 seeds and no outgroup sequence (UFBoot 79 at the family edge).
With the tree rooted at that edge, the family falls into three large clades, each with a working name (`clanAB`, which holds `clanA` and `clanB`, `clanC` and `clanD`).
Outside the family, the next clade out, 87 tips, is `clanE`.
The names are working labels and can change when the sequences are better known.
`alkB.classification.tsv` assigns every tip (levels separated by `;`), `alkB.clades.tsv` gives the clade names without the `clanAB` level, with the tag, and `alkB.family_taxonomy.tsv` has the UniProt organism, lineage and protein name of the 205 family members and the 87 of clan E (UniProt lookup of 2026-11-17).

| Clan | Tips | UFBoot | Subclans | Taxa | Seeds | Function |
|---|---|---|---|---|---|---|
| `clanAB` | 100 | 93 | `clanA` and `clanB` | Proteobacteria and Actinomycetes | those of A and B | AlkB-type alkane hydroxylases |
| `clanA` | 66 | 97 | A1 (45; A1a 24, A1b 21), A2 (8); 13 tips in none | Proteobacteria. A1a mostly Alphaproteobacteria (Hyphomicrobiales, Parvularculales, Rhodobacterales), A1b Gamma- and Betaproteobacteria (Oceanospirillales, *Marinobacter*, *Alloalcanivorax*), A2 *Acinetobacter* and relatives | GPo1 (*P. oleovorans*), *P. putida*, *Alcanivorax* AlkB1, *Acinetobacter* AlkM, *Fontimonas* AlkB, *Burkholderia* | AlkB-type alkane hydroxylases |
| `clanB` | 34 | 91 | B1 (21), B2 (13) | Actinomycetes: *Rhodococcus*, *Gordonia*, *Mycobacteriales* | *Rhodococcus* AlkB1 to 4 and AlkB7, *Gordonia* | AlkB-type alkane hydroxylases |
| `clanC` | 23 | 100 | C1 (9, UFBoot 99); 14 tips in none | Gammaproteobacteria (Oceanospirillales, Burkholderiales, *Alcanivorax*, *Thalassolituus*, *Pseudomonas*) | *Alcanivorax* AlkB2, *P. aeruginosa* AlkB1 and AlkB2 | likely alkane hydroxylases |
| `clanD` | 70 | 92 | D1 (56, UFBoot 95), D2 (14) | D1 Bacteroidota (Cytophagia 18, Flavobacteriia 15, Saprospiria 5) and Gammaproteobacteria (Methylococcales 8, *Vibrio*, *Microbulbifer*); D2 Cytophagia and *Leptospira* | none | likely alkane hydroxylases (no seeds; inferred from the tree position) |
| `clanE` | 87 | 90 | none | Alphaproteobacteria, 86 of 87, marine Roseobacter-type (*Aquimixticola*, *Ascidiaceihabitans*, *Seohaeicola*, *Actibacterium*, *Cereibacter*) | none | AlkB-like, function unknown |
| `unresolved` | 12 | | | mixed (Neisseriales, Legionellales, Verrucomicrobiota, Acidobacteriota) | none | unknown |

Clans A and B are sister clades (`clanAB`, UFBoot 93); A (97) and B (91) are supported separately, and the loose tip A0ACE2LTZ7 joins them at UFBoot 100 (101 tips).
The 14 unlabelled C tips and the 13 A tips outside A1 and A2 do not form clades of their own.
A tip of the old `clanB` label (A0ACE2LTZ7) lies outside the 34-tip clade and is `unresolved`.
Clan E (UFBoot 90 for family plus three loose tips plus E) has no seed; all 87 tips are unreviewed and inferred from homology, 80 are annotated alkane 1-monooxygenase and 8 fatty acid desaturase by automatic annotation.
The next clades out (70 `ref` tips at UFBoot 72) also pass the `alkB` profile filter, so the profile does not mark the end of the family.
The remaining 641 tips are `PF00487_other;superfamily` and XylM (P21395) is `PF00487_other;XylM`.

### Cautions

- Clans C and D are called "likely" alkane hydroxylases because they sit in one supported series of clades with A and B (A+B, D, C, each at UFBoot above 90); D has no seed, and the two *P. aeruginosa* seeds of C have only title-level evidence.
- Clan E has no functional indication of its own.
- The clade names refer to this tree and this root; the relationship between A+B, C and D is not resolved.
- The family edge has UFBoot 79 and the ultrafast bootstrap converged (correlation coefficient 0.994).
- Function is inferred from the seeds; a few seeds were never tested for activity.
- The family set came from PF00487 and so contains almost no archaea.
- XylM is placed outside the family.

### Files

`ref_pf00487.faa`, `ref_pf00487.hmm.trim.alnfaa` (root symlink `alkB.alnfaa`), `PF00487.hmm`, `ref_pf00487.R8.iqtree.{treefile,contree,iqtree}`, `alkB.models`, `alkB.classification.tsv`, `alkB.clades.tsv`, `alkB.family_taxonomy.tsv`, `seeds_literature.tsv`.
