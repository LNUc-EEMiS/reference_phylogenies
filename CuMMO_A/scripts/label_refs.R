suppressMessages({library(readr); library(dplyr); library(stringr)})
setwd("/data/users/dl/cummo_trees")
r <- read_rds("seqs/reps.rds")
L <- function(pat) str_detect(r$lineage, pat)
r$label <- case_when(
  r$archaeal & L("Nitrosopumilales") ~ "AMO_archaeal;Nitrosopumilales",
  r$archaeal & L("Nitrososphaerales") ~ "AMO_archaeal;Nitrososphaerales",
  r$archaeal & L("Nitrosotaleales") ~ "AMO_archaeal;Nitrosotaleales",
  r$archaeal & L("Nitrosocaldales") ~ "AMO_archaeal;Nitrosocaldales",
  r$archaeal & L("Cenarchaeales") ~ "AMO_archaeal;Cenarchaeales",
  r$archaeal & L("Marine Group I") ~ "AMO_archaeal;MarineGroupI",
  r$archaeal & L("Nitrosotenuis") ~ "AMO_archaeal;Nitrosotenuis",
  r$archaeal & L("Nitrososphaerota") ~ "AMO_archaeal;Nitrososphaerota_unspecified",
  r$archaeal ~ "AMO_archaeal;unspecified",
  str_detect(r$gene, "pxmA") ~ "pMMO;pxmA",
  L("Nitrospiraceae") ~ "AMO_bacterial;comammox_Nitrospira",
  L("Nitrosomonadaceae") ~ "AMO_bacterial;AOB_Betaproteobacteria",
  L("Nitrosococcus|Nitrosoglobus|Nitrosacidicoccus") ~ "AMO_bacterial;AOB_Gammaproteobacteria",
  L("Methylococcales") ~ "pMMO;typeI_Methylococcales",
  L("Methylocystaceae") ~ "pMMO;typeII;Methylocystaceae",
  L("Beijerinckiaceae") ~ "pMMO;typeII;Beijerinckiaceae",
  L("Methylacidiphilae|Methylacidiphilales|Methylacidimicrobium") ~ "pMMO;Verrucomicrobiota",
  L("Methylomirabilota") ~ "pMMO;Methylomirabilota",
  str_detect(r$pname, regex("hydrocarbon", TRUE)) ~ "hydrocarbon_MO;Actinomycetota",
  TRUE ~ paste0("other_PF02461;", coalesce(str_extract(r$lin, "(Actinomycetota|Pseudomonadota|Bacteroidota|Bacillota|Verrucomicrobiota|Armatimonadota|Campylobacterota)"), "other"))
)
r$label_basis <- if_else(r$archaeal | r$label != "x", paste0("UniProt ", r$acc, " source-organism lineage (NCBI taxonomy): ", r$org), "")
write_rds(r, "seqs/reps_labelled.rds")
print(r %>% count(label, env), n = 60)
