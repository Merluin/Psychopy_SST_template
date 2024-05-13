###########################################################################
#
#  Programmer:  QUETTIER THOMAS
#  Date:        01/05/2024
#  Description: computation of SSRT
#
#  Update:      09/05/2024
###########################################################################

# Clear the Workspace
rm(list=ls()) # Remove all objects from the workspace

# Load Required Functions and Libraries
devtools::load_all() # Load necessary packages and functions

# find nb of file
folder_dir<-c("data/")

#concatenate all file and apply preprocessing
dataset<-list.files(path=folder_dir,pattern="\\.csv$", full.names = TRUE) %>%
  lapply(.,function(x) read.csv(x, sep=",", header=TRUE,stringsAsFactors = FALSE ))%>%
  bind_rows(.id = "SubjectName") %>% 
  preprocessing()

dataset # explore dataset table
  

