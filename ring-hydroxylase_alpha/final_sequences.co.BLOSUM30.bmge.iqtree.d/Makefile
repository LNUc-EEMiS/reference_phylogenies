include ~/dev/biomakefiles/lib/make/makefile.iqtree

IQTREE_OPTS = -B 1000 -nt AUTO

final_sequences.co.BLOSUM30.bmge.iqtree.MFP.short_names.newick: long2short.sed final_sequences.co.BLOSUM30.bmge.iqtree.MFP.treefile
	sed -f $^ > $@

long2short.sed: long2short.tsv
	grep -v '^db' $< | sed 's:/:\\/:g' | sed 's:.*\t\(.*\)\t\(.*\):s/\1/\2/:' > $@

iriarte_et_al_2024.nexml: sp_label_translate.sed final_sequences.co.BLOSUM30.bmge.iqtree.MFP.nexml
	sed -f $^ > $@
