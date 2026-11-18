suppressMessages({library(readr);library(dplyr);library(stringr)})
setwd("/data/users/dl/cummo_trees/seqs")
f<-read_rds("pool.rds")
pick<-function(clf){
  cl<-read_tsv(clf,col_names=c("rep","acc"),show_col_types=FALSE)
  x<-cl %>% inner_join(f,by="acc") %>%
    mutate(prio=(rev=="reviewed")*100+(!env)*20+(pe=="Evidence at protein level")*10+(pe=="Evidence at transcript level")*5+(str_detect(gene,"amoA|pmoA|pxmA|bmoA|hmoA"))*3-abs(len-ifelse(archaeal,215,250))/100) %>%
    group_by(rep) %>% arrange(desc(prio),.by_group=TRUE) %>% mutate(csize=n()) %>% slice(1) %>% ungroup()
  x}
r<-bind_rows(pick("poolA0.95_cluster.tsv"),pick("poolB90_cluster.tsv"),pick("poolN97_cluster.tsv")) %>% distinct(acc,.keep_all=TRUE)
# always keep reviewed
rv<-f %>% filter(rev=="reviewed",!acc %in% r$acc) %>% mutate(csize=1L)
rv<-bind_rows(rv,f %>% filter(str_detect(gene,"pxmA"),!acc %in% r$acc) %>% mutate(csize=1L))
r<-bind_rows(r,rv) %>% distinct(acc,.keep_all=TRUE)
r$lin<-str_remove_all(r$lineage," \\([a-z ]+\\)")
r$taxpath<-sapply(str_split(r$lin,", "),function(x) paste(x[-1:-2],collapse="|"))
write_rds(r,"reps.rds"); print(nrow(r)); print(table(r$archaeal,r$env))
options(width=250)
print(r %>% filter(!archaeal) %>% count(taxpath=str_replace(taxpath,"^Pseudomonadati\\|Pseudomonadota\\|",""),sort=TRUE) %>% mutate(taxpath=str_sub(taxpath,1,130)),n=130)
