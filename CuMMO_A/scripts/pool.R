suppressMessages({library(readr);library(dplyr);library(stringr)})
setwd("/data/users/dl/cummo_trees/seqs")
d<-read_rds("all_cands.rds")
d$archaeal<-str_detect(d$lineage,"Archaea")
nm <- str_detect(d$pname,regex("methane monooxygenase|ammonia monooxygenase|butane|hydrocarbon monooxygenase",TRUE)) &
  !str_detect(d$pname,regex("subunit (B|C|beta|gamma)|PmoB|PmoC|AmoB|AmoC|soluble|hydroxylase|component|methanesulfonate",TRUE))
gn <- str_detect(d$gene,regex("pxmA|bmoA|hmoA|pBmoA",TRUE))
f<-d %>% filter(str_detect(pfam,"PF02461|PF12942"), !is.na(seq), !str_detect(pname,regex("molybdopterin",TRUE)),
 !str_detect(lineage,"Eukaryota|Viruses|Duplodnaviria|metagenomes"),
 (archaeal & len>=195 & len<=235)|(!archaeal & len>=220 & len<=310 & (is.na(frag)|frag!="fragment"))|(!archaeal & str_detect(gene,"pxmA") & len>=150))
f$env<-str_detect(f$lineage,"environmental samples|unclassified|metagenomes")|str_detect(f$org,regex("uncultured|environmental|unidentified|metagenome",TRUE))
print(table(f$archaeal,f$env)); print(nrow(f))
write_rds(f,"pool.rds")
writeLines(c(rbind(paste0(">",f$acc),f$seq)),"pool.faa")
