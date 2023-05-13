# Location of packages download
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("NOISeq")
# Download packages
biocLite("NOISeq")
# %%
#Use packages in R
library("NOISeq")

# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_1hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("n_1","k_1"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_1","k_1"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_1hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%

# %%
library("NOISeq")

# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_2hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("n_2","k_2"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_2","k_2"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_2hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%

# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_4hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("n_4","k_4"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_4","k_4"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_4hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%

# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_6hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("n_6","k_6"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_6","k_6"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_6hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_8hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("n_8","k_8"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_8","k_8"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_8hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%
# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_12hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

mfactors <- matrix(c("n_12","k_12"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_12","k_12"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_12hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/NOISeq input/il6_nt_kd_minus0_24hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName
# %%
# NOISeq analysis

mfactors <- matrix(c("n_24","k_24"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("n_24","k_24"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="il6_24hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%

# %%
########################             IFNg               ########################

library("NOISeq")

# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_0hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_0","kg_0"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_0","kg_0"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_0hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_1hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_1","kg_1"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_1","kg_1"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_1hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_1hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_1","kg_1"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_1","kg_1"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_1hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
# read data
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_2hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_2","kg_2"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_2","kg_2"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_2hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_4hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_4","kg_4"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_4","kg_4"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_4hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
#%%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_6hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_6","kg_6"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_6","kg_6"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_6hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_8hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_8","kg_8"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_8","kg_8"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_8hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
#%%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_12hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_12","kg_12"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_12","kg_12"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_12hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)
# %%
# %%
getData <- read.table("/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/NOISeq input/ifn_nt_kd_minus0_24hr.txt",header=T)
seqName <- getData[,1]
getData <- getData[2:3]
rownames(getData) <- seqName

# NOISeq analysis

mfactors <- matrix(c("ng_24","kg_24"),nrow = 2, ncol = 1, byrow = TRUE, dimnames = list(c("ng_24","kg_24"),c("transcript")))

mydata <- readData(data=getData, factors=mfactors)
getNOIseqRes <- noiseq(mydata, k = 0.1, norm = "rpkm", replicates = "no", factor="transcript", pnr = 0.2, nss = 10)

write.table(getNOIseqRes@results[[1]], file="ifn_24hr_afterNoiseq2.txt", sep="\t", row.names=T, col.names=T, quote=F)

# %%

