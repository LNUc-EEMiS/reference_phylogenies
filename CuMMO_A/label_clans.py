"""Clan labels of CuMMO_A from the tree: every clan is a set of tips that forms one side of a split of the unrooted tree (the tree is drawn with the archaeal/bacterial split as the root only to define the sides; the true root is not known) with the UFBoot value given in the table.
Supports are read from the bipartitions of CuMMO_A.newick, not from node labels after rerooting.
Usage (from the repository root): python3 CuMMO_A/label_clans.py"""
import sys, collections, csv
sys.path.insert(0, "/data/users/dl/bmm_trees/pylib")
import dendropy
raw = dendropy.Tree.get(path="CuMMO_A.newick", schema="newick", preserve_underscores=True)
allt = frozenset(x.taxon.label for x in raw.leaf_node_iter())
canon = lambda S: (lambda S: min(S, allt - S, key=lambda z: (len(z), sorted(z))))(frozenset(S))
sup = {canon(x.taxon.label for x in nd.leaf_nodes()): nd.label for nd in raw.preorder_node_iter()
       if not nd.is_leaf() and nd.parent_node is not None and nd.label}
old = {}
for r in csv.DictReader(open("CuMMO_A/CuMMO_A.taxonomy.tsv"), delimiter="\t"):
    old[r["accession"]] = r["classification"].replace("CuMMO_A;", "")
arch = frozenset(a for a, c in old.items() if c.startswith("AMO_archaeal"))
t = dendropy.Tree.get(path="CuMMO_A.newick", schema="newick", preserve_underscores=True)
for n in t.preorder_node_iter():
    if n.is_leaf() or n.parent_node is None:
        continue
    s = frozenset(x.taxon.label for x in n.leaf_nodes())
    if s == arch or s == allt - arch:
        t.reroot_at_edge(n.edge, update_bipartitions=False)
        break
S = lambda nd: sup.get(canon(x.taxon.label for x in nd.leaf_nodes()), "NA")
leaves = lambda nd: frozenset(x.taxon.label for x in nd.leaf_nodes())
nodes = [n for n in t.postorder_node_iter() if not n.is_leaf()]
def find(n, kinds, outside=None):
    """The clan of size n whose tips have exactly the old labels in kinds (name -> count)."""
    out = []
    for nd in nodes:
        L = nd.leaf_nodes()
        if len(L) != n:
            continue
        c = collections.Counter(old[x.taxon.label] for x in L)
        if all(c.get(k, 0) == v for k, v in kinds.items()) and not (outside and leaves(nd) <= leaves(outside)):
            out.append(nd)
    assert len(out) == 1, (n, kinds, len(out))
    return out[0]
G = "AMO_bacterial;AOB_Gammaproteobacteria"
clans = [
 ("bacterial_CuMMO;betaproteobacterial_AOB_and_comammox_AMO", find(20, {"AMO_bacterial;AOB_Betaproteobacteria": 17, "AMO_bacterial;comammox_Nitrospira": 3})),
 ("bacterial_CuMMO;betaproteobacterial_AOB_and_comammox_AMO;betaproteobacterial_AOB", find(17, {"AMO_bacterial;AOB_Betaproteobacteria": 17})),
 ("bacterial_CuMMO;betaproteobacterial_AOB_and_comammox_AMO;comammox_Nitrospira", find(3, {"AMO_bacterial;comammox_Nitrospira": 3})),
 ("bacterial_CuMMO;gammaproteobacterial_AOB_AMO", find(6, {G: 6})),
 ("bacterial_CuMMO;Methylococcales_pMMO", find(30, {"pMMO;typeI_Methylococcales": 29, "other_PF02461;other": 1})),
 ("bacterial_CuMMO;Methylocystaceae_and_Beijerinckiaceae_pMMO", find(16, {"pMMO;typeII;Methylocystaceae": 14, "pMMO;typeII;Beijerinckiaceae": 2})),
 ("bacterial_CuMMO;pxmA_clan_pMMO_paralogs", find(19, {"pMMO;pxmA": 3, "pMMO;typeI_Methylococcales": 12, "pMMO;typeII;Methylocystaceae": 4})),
 ("bacterial_CuMMO;Verrucomicrobiota_pMMO", find(10, {"pMMO;Verrucomicrobiota": 10})),
 ("bacterial_CuMMO;Methylomirabilota_pMMO", find(2, {"pMMO;Methylomirabilota": 2})),
 ("bacterial_CuMMO;distant_family_members;Pseudomonadota_clan1", find(5, {"other_PF02461;Pseudomonadota": 5})),
 ("bacterial_CuMMO;distant_family_members;Pseudomonadota_clan2", find(3, {"other_PF02461;Pseudomonadota": 3}, outside=find(5, {"other_PF02461;Pseudomonadota": 5}))),
 ("bacterial_CuMMO;distant_family_members;environmental_clan", find(2, {"other_PF02461;other": 2})),
 ("bacterial_CuMMO;distant_family_members;Actinomycetota_and_Bacillota", find(6, {"other_PF02461;Actinomycetota": 4, "other_PF02461;Bacillota": 1, "hydrocarbon_MO;Actinomycetota": 1})),
]
new = {}
for a in arch:
    new[a] = "archaeal_AMO"
for path, nd in clans:           # general clans first, subclans later overwrite
    for x in leaves(nd):
        new[x] = path
for a in old:
    new.setdefault(a, "bacterial_CuMMO;unresolved")
with open("CuMMO_A.classification.tsv", "w") as f:
    for a in sorted(new, key=lambda a: list(old).index(a)):
        f.write(f"{a}\tCuMMO_A;{new[a]}\n")
with open("CuMMO_A/CuMMO_A.clans.tsv", "w") as f:
    f.write("clan\ttips\tUFBoot\n")
    f.write(f"archaeal_AMO\t{len(arch)}\t100\nbacterial_CuMMO\t{len(allt-arch)}\t100\n")
    for path, nd in clans:
        f.write(f"{path}\t{len(nd.leaf_nodes())}\t{S(nd)}\n")
print(collections.Counter(new.values()))
