import dendropy, sys
T = dendropy.Tree.get(path=sys.argv[1], schema="newick", preserve_underscores=True)
L = sorted(((n.edge_length or 0, n.taxon.label) for n in T.leaf_node_iter()), reverse=True)[:6]
for l, t in L: print(t, round(l, 3))
