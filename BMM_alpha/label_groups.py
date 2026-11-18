import sys; sys.path.insert(0,'/data/users/dl/bmm_trees/pylib')
import dendropy,csv,collections
t=dendropy.Tree.get(path='tree/bmm.contree',schema='newick',preserve_underscores=True)
ex={'G1':'Q00456 Q51939 Q6IV66 O87798 O87082','G2':'P19732 Q8VSV8 Q1LMG3 Q84AQ2 Q9S147 Q9ZNP4',
'G3':'P22869 P27353 Q8KQF0 Q5VJ90','G4':'Q6XBI6 A0A3G9E9D5','G5':'Q768T5 Q0SJK9 A0QTU8 E9RFS9 Q9F3V6','G6':'A0ABT6GKR4 Q08KF2'}
exg={a:g for g,v in ex.items() for a in v.split()}
# root on the edge of the clade {A0A1X0BAZ0,A0A2R4K2J8,A0ABV7L1W5}
tri={'A0A1X0BAZ0','A0A2R4K2J8','A0ABV7L1W5'}
n=t.mrca(taxon_labels=list(tri)); print('root clade size',len(n.leaf_nodes()))
t.reroot_at_edge(n.edge,update_bipartitions=False)
def sup(n):
    try: return float(n.label)
    except: return 100.0 if n.is_leaf() else 0.0
res={}
for g,v in ex.items():
    ids=v.split(); m=t.mrca(taxon_labels=ids)
    L=[x.taxon.label for x in m.leaf_nodes()]
    foreign=sorted({exg[x] for x in L if x in exg and exg[x]!=g})
    print(g,'mrca size',len(L),'support',m.label,'foreign exemplar groups inside:',foreign)
# smallest supported pure clade assignment
tip={}
for nd in t.preorder_node_iter():   # large to small
    if nd.is_leaf(): continue
    L=[x.taxon.label for x in nd.leaf_nodes()]
    gs={exg[x] for x in L if x in exg}
    if len(gs)==1 and sup(nd)>=70:
        g=next(iter(gs))
        for x in L:
            if x not in tip: tip[x]=(g,nd.label,len(L))
print(len(tip),'of',len(t.leaf_nodes()),'tips assigned')
print(collections.Counter(v[0] for v in tip.values()))
import json; json.dump(tip,open('tip_groups.json','w'))
# restrict to MRCA of exemplars; also 'Xamo/Iso-like' subgroup of G1
meta={r['Entry']:r for r in csv.DictReader(open('ref/alpha_meta.tsv'),delimiter='\t')}
final={}
inside={}
for g,v in ex.items():
    m=t.mrca(taxon_labels=v.split())
    for x in m.leaf_nodes(): inside[x.taxon.label]=g
xi=t.mrca(taxon_labels=['O87082','A0ABT6GKQ4'])
xil={x.taxon.label for x in xi.leaf_nodes()}
print('xamo/iso node',len(xil),xi.label, 'groups in it',collections.Counter(inside.get(x,'-') for x in xil))
for a in [x.taxon.label for x in t.leaf_nodes()]:
    if a in inside: final[a]=inside[a]
    else: final[a]='unassigned'
print(collections.Counter(final.values()))
for a,g in final.items():
    if g=='unassigned':
        print(a,meta[a]['Gene Names'].split()[:1],meta[a]['Organism'][:30],tip.get(a))
json.dump(final,open('tip_groups_mrca.json','w'))
