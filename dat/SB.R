library(lattice)

dat <- read.table("SBmat.dat")
dat_mat <- data.matrix(dat)
levelplot(dat_mat)
rgb.palette <- colorRampPalette(c("red", "green"), space = "rgb" )
rgb.palette <- colorRampPalette(c("white", "red", "blue", "green", "black"), space = "rgb" )       #more varied colour scheme
levelplot(dat_mat, xlab="Residue", ylab="Residue", scales = list(tck = c(1,0)), col.regions=rgb.palette(120), cuts=100, at=seq(0,100,1))

cat("Output file name:\n")
inp <- readLines(file("stdin"), n = 1L)
cat(paste("Creating", inp, "\n"))

bmpname <- paste(inp, ".bmp", sep="")
bmp(bmpname)

#dev.off()
#rerun the levelplot command above and it will write to the R-working direc
levelplot(dat_mat, xlab="Residue", ylab="Residue", scales = list(tck = c(1,0)), col.regions=rgb.palette(120), cuts=100, at=seq(0,100,1))
