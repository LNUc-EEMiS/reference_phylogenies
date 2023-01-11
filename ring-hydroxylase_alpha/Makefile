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

CLUSTER_LEVELS = 0.90 0.80 0.70 0.60 0.50 0.40 0.30

problem_sequences.rare: $(wildcard trembl_pf00848_pf00355.uc0.30.cl[1-9])
	sed 's/.*|\([^ ]\+\).*/\1/' $^ > $@

final_sequences.faa: swissprot_pf00848_pf00355.faa trembl_pf00848_pf00355.uc0.80.correct.faa
	sed '/^>/s/ /_/g' $< | sed 's/>/>SW_/' > $@
	cat $(word 2,$^) >> $@

cl_files: $(subst .clusters,.small_clusters,$(wildcard *.clusters))

fix_cl_files: $(wildcard *.cl[0-9]*)
	sed -i.bak 's/.*|\([^ ]*\).*/\1/' $^
	touch $@

fix_faa_files: $(wildcard *.uc0.??.faa)
	for f in $^; do \
		make $$(basename $$f .faa).c.faa; mv $$(basename $$f .faa).c.faa $$f; \
	done
	touch $@

%.unique_annotations: %.alnfaa
	 grep '>' $< | sed 's/_OS=.*//' | sed 's/.*|[^_]*_[^_]*_//' | sort -u > $@
