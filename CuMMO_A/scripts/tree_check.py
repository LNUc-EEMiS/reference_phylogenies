import dendropy, sys, csv, pickle
T = dendropy.Tree.get(path="/data/users/dl/cummo_trees/tree/cummoA.treefile", schema="newick", preserve_underscores=True)
lab = {}
for row in csv.DictReader(open("/data/users/dl/cummo_trees/seqs/reps_labels.tsv"), delimiter="\t"):
    lab[row["acc"]] = row
leaves = {n.taxon.label: n for n in T.leaf_node_iter()}
allset = set(leaves)
arch = [a for a in leaves if lab[a]["archaeal"] == "TRUE"]
A = set(arch)
best = None
for nd in T.postorder_node_iter():
    if nd.parent_node is None: continue
    u = set(x.taxon.label for x in nd.leaf_iter())
    if u == A or (allset - u) == A:
        best = nd; break
if best is None:
    print("archaea not monophyletic on any edge"); sys.exit()
print("archaeal split found; support", best.label)
T.reroot_at_edge(best.edge, update_bipartitions=True)
T.write(path="/data/users/dl/cummo_trees/tree/cummoA.rooted.newick", schema="newick", suppress_rooting=True)
T.is_rooted = True
# monophyly of each label (at level 2 and 1)
groups = {}
for a, r in lab.items():
    parts = r["label"].split(";")
    for k in range(1, len(parts) + 1):
        groups.setdefault(";".join(parts[:k]), []).append(a)
print("label\tn\tn_under_mrca\tsupport\tpurity")
for g, m in sorted(groups.items()):
    if len(m) < 2:
        print(g, len(m), "-", "-", "single"); continue
    node = T.mrca(taxon_labels=m)
    u = [n.taxon.label for n in node.leaf_iter()]
    print(g, len(m), len(u), node.label, "monophyletic" if len(u) == len(m) else "not monophyletic (%d foreign)" % (len(u) - len(m)), sep="\t")
