include ~/dev/biomakefiles/lib/make/makefile.hmmer
include ~/dev/biomakefiles/lib/make/makefile.probcons
include ~/dev/biomakefiles/lib/make/makefile.clustalo
include ~/dev/biomakefiles/lib/make/makefile.usearch
include ~/dev/biomakefiles/lib/make/makefile.mafft
include ~/dev/biomakefiles/lib/make/makefile.phylo
include ~/dev/biomakefiles/lib/make/makefile.bmge
include ~/dev/biomakefiles/lib/make/makefile.misc
include ~/dev/biomakefiles/lib/make/makefile.splitstree
include ~/dev/biomakefiles/lib/make/makefile.fasttree

CLUSTER_LEVELS = 0.90 0.85 0.80 0.75 0.70

final_sequences.faa: swissprot_pf00848_pf00355.faa trembl_pf00848_pf00355.uc0.80.correct.faa
	cat $^ >> $@

swissprot_pf00848_pf00355.faa: swissprot_pf00848_pf00355_prokaryotes.faa swissprot_pf00848_pf00355_eukaryotes.faa
	cat $^ > $@

trembl_pf00848_pf00355.faa: trembl_pf00848_pf00355_prokaryotes.faa trembl_pf00848_pf00355_eukaryotes.faa
	cat $^ > $@

final_sequences.names.tsv: final_sequences.faa
	grep '>' $< | sed 's/^\([^|]\+\)|.*/\1/'

problem_sequences.fragments: trembl_pf00848_pf00355.faa
	grep -i fragment $< | sed 's/>tr|\(.*\)|.*/\1/' > $@

cl_files: $(subst .clusters,.small_clusters,$(wildcard *.clusters))

fix_cl_files: $(wildcard *.cl[0-9]*)
	sed -i 's/.*|\([^ ]*\).*/\1/' $^
	touch $@

fix_faa_files: $(wildcard *.uc0.??.faa)
	for f in $^; do \
		make $$(basename $$f .faa).c.faa; mv $$(basename $$f .faa).c.faa $$f; \
	done
	touch $@

%.unique_annotations: %.alnfaa
	 grep '>' $< | sed 's/_OS=.*//' | sed 's/.*|[^_]*_[^_]*_//' | sort -u > $@
