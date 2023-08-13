#Calling library
library(geomorph)

#Reading data and computing GPA
lm <- readland.tps("NEW-DS-LM-38-2.tps", specID = "ID")
nas_lm <- gpagen(lm, print.progress = FALSE)
new_coords <- nas_lm$coords

#Calling supporting components

new_ind_data = read.csv("ind_data.csv")# read csv file
new_pair_data = read.csv("pair_data.csv")
new_rep_data = read.csv("rep_data.csv")

#could be saved for import later to reduce lines of code
#save(new_coords, new_ind_data, new_pair_data, new_rep_data, file="downsymm.rda")

ind=new_ind_data$x
rep=new_rep_data$x

#Computing Bilateral symmetry and asymmetry
gdf <- geomorph.data.frame(shape = new_coords, ind = new_ind_data$x, replicate = new_rep_data$x)
new.sym <- bilat.symmetry(A = shape, ind = ind, rep = rep, object.sym = TRUE,land.pairs = new_pair_data, data = gdf, RRPP = TRUE, iter = 999, print.progress = FALSE)

#Print results
summary(new.sym)
new.sym$shape.anova # display single anova result

plot(new.sym, warpgrids = TRUE, mesh = NULL) #plotting the warp deformation

