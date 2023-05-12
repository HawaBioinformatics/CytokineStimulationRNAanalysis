# %%
import pandas as pd 
# %%
### process 0,1,2,4,6,8,12,24 hrs for IL6 non-target

il6_nt_0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N0_sorted.csv',index_col=0)
il6_nt_1 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N1_sorted.csv',index_col=0)
il6_nt_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N2_sorted.csv',index_col=0)
il6_nt_4 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N4_sorted.csv',index_col=0)
il6_nt_6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N6_sorted.csv',index_col=0)
il6_nt_8 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N8_sorted.csv',index_col=0)
il6_nt_12 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N12_sorted.csv',index_col=0)
il6_nt_24 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/NT/6N24_sorted.csv',index_col=0)

print(il6_nt_0.shape,il6_nt_1.shape,il6_nt_2.shape,il6_nt_4.shape,il6_nt_6.shape,il6_nt_8.shape,il6_nt_12.shape,il6_nt_24.shape)
# (39503, 1) (39810, 1) (38217, 1) (36649, 1) (37281, 1) (36901, 1) (38486, 1) (38984, 1)
# %%
### aggregate data
il6_nt_0 = il6_nt_0.groupby(level=0).sum()
il6_nt_1 = il6_nt_1.groupby(level=0).sum()
il6_nt_2 = il6_nt_2.groupby(level=0).sum()
il6_nt_4 = il6_nt_4.groupby(level=0).sum()
il6_nt_6 = il6_nt_6.groupby(level=0).sum()
il6_nt_8 = il6_nt_8.groupby(level=0).sum()
il6_nt_12 = il6_nt_12.groupby(level=0).sum()
il6_nt_24 = il6_nt_24.groupby(level=0).sum()

print(il6_nt_0.shape,il6_nt_1.shape,il6_nt_2.shape,il6_nt_4.shape,il6_nt_6.shape,il6_nt_8.shape,il6_nt_12.shape,il6_nt_24.shape)
# (16479, 1) (16546, 1) (16184, 1) (15730, 1) (15963, 1) (15860, 1) (16388, 1) (16184, 1)

# %%
### process 0,1,2,4,6,8,12,24 hrs for IL6 knockdown
il6_kd_0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K0_sorted.csv',index_col=0)
il6_kd_1 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K1_sorted.csv',index_col=0)
il6_kd_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K2_sorted.csv',index_col=0)
il6_kd_4 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K4_sorted.csv',index_col=0)
il6_kd_6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K6_sorted.csv',index_col=0)
il6_kd_8 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K8_sorted.csv',index_col=0)
il6_kd_12 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K12_sorted.csv',index_col=0)
il6_kd_24 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IL6_raw/KD/6K24_sorted.csv',index_col=0)

print(il6_kd_0.shape,il6_kd_1.shape,il6_kd_2.shape,il6_kd_4.shape,il6_kd_6.shape,il6_kd_8.shape,il6_kd_12.shape,il6_kd_24.shape)
# (35853, 1) (36628, 1) (37949, 1) (37142, 1) (16173, 1) (38525, 1) (37081, 1) (37076, 1)

# %%
### aggregate data
il6_kd_0 = il6_kd_0.groupby(level=0).sum()
il6_kd_1 = il6_kd_1.groupby(level=0).sum()
il6_kd_2 = il6_kd_2.groupby(level=0).sum()
il6_kd_4 = il6_kd_4.groupby(level=0).sum()
il6_kd_6 = il6_kd_6.groupby(level=0).sum()
il6_kd_8 = il6_kd_8.groupby(level=0).sum()
il6_kd_12 = il6_kd_12.groupby(level=0).sum()
il6_kd_24 = il6_kd_24.groupby(level=0).sum()

print(il6_kd_0.shape,il6_kd_1.shape,il6_kd_2.shape,il6_kd_4.shape,il6_kd_6.shape,il6_kd_8.shape,il6_kd_12.shape,il6_kd_24.shape)
# (15562, 1) (15695, 1) (15912, 1) (15741, 1) (9382, 1) (16191, 1) (15675, 1) (15605, 1)
# %%
### process 0,1,2,4,6,8,12,24 hrs for IFNg non-target
ifn_nt_0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG0_sorted.csv',index_col=0)
ifn_nt_1 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG1_sorted.csv',index_col=0)
ifn_nt_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG2_sorted.csv',index_col=0)
ifn_nt_4 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG4_sorted.csv',index_col=0)
ifn_nt_6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG6_sorted.csv',index_col=0)
ifn_nt_8 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG8_sorted.csv',index_col=0)
ifn_nt_12 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG12_sorted.csv',index_col=0)
ifn_nt_24 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/NT/NG24_sorted.csv',index_col=0)

print(ifn_nt_0.shape,ifn_nt_1.shape,ifn_nt_2.shape,ifn_nt_4.shape,ifn_nt_6.shape,ifn_nt_8.shape,ifn_nt_12.shape,ifn_nt_24.shape)
# (37116, 1) (38591, 1) (37195, 1) (37094, 1) (38104, 1) (37980, 1) (40284, 1) (36485, 1)

# %%
### aggregate data
ifn_nt_0 = ifn_nt_0.groupby(level=0).sum()
ifn_nt_1 = ifn_nt_1.groupby(level=0).sum()
ifn_nt_2 = ifn_nt_2.groupby(level=0).sum()
ifn_nt_4 = ifn_nt_4.groupby(level=0).sum()
ifn_nt_6 = ifn_nt_6.groupby(level=0).sum()
ifn_nt_8 = ifn_nt_8.groupby(level=0).sum()
ifn_nt_12 = ifn_nt_12.groupby(level=0).sum()
ifn_nt_24 = ifn_nt_24.groupby(level=0).sum()

print(ifn_nt_0.shape,ifn_nt_1.shape,ifn_nt_2.shape,ifn_nt_4.shape,ifn_nt_6.shape,ifn_nt_8.shape,ifn_nt_12.shape,ifn_nt_24.shape)
# (15738, 1) (16272, 1) (15887, 1) (15813, 1) (16070, 1) (15990, 1) (16735, 1) (15862, 1)
# %%
### process 0,1,2,4,6,8,12,24 hrs for IFNg knockdown

ifn_kd_0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG0_sorted.csv',index_col=0)
ifn_kd_1 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG1_sorted.csv',index_col=0)
ifn_kd_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG2_sorted.csv',index_col=0)
ifn_kd_4 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG4_sorted.csv',index_col=0)
ifn_kd_6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG6_sorted.csv',index_col=0)
ifn_kd_8 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG8_sorted.csv',index_col=0)
ifn_kd_12 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG12_sorted.csv',index_col=0)
ifn_kd_24 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/IFNG_raw/KD/KG24_sorted.csv',index_col=0)

print(ifn_kd_0.shape,ifn_kd_1.shape,ifn_kd_2.shape,ifn_kd_4.shape,ifn_kd_6.shape,ifn_kd_8.shape,ifn_kd_12.shape,ifn_kd_24.shape)
# (39499, 1) (37023, 1) (37986, 1) (39300, 1) (40587, 1) (40212, 1) (36125, 1) (41578, 1)
# %%
### aggregate data
ifn_kd_0 = ifn_kd_0.groupby(level=0).sum()
ifn_kd_1 = ifn_kd_1.groupby(level=0).sum()
ifn_kd_2 = ifn_kd_2.groupby(level=0).sum()
ifn_kd_4 = ifn_kd_4.groupby(level=0).sum()
ifn_kd_6 = ifn_kd_6.groupby(level=0).sum()
ifn_kd_8 = ifn_kd_8.groupby(level=0).sum()
ifn_kd_12 = ifn_kd_12.groupby(level=0).sum()
ifn_kd_24 = ifn_kd_24.groupby(level=0).sum()

print(ifn_kd_0.shape,ifn_kd_1.shape,ifn_kd_2.shape,ifn_kd_4.shape,ifn_kd_6.shape,ifn_kd_8.shape,ifn_kd_12.shape,ifn_kd_24.shape)
# (16305, 1) (15715, 1) (16175, 1) (16430, 1) (16636, 1) (16484, 1) (15621, 1) (17001, 1)

# %%
### combine il6 nt and knockdown and il6 nt and knockdown

### il6 nt size # (16479, 1) (16546, 1) (16184, 1) (15730, 1) (15963, 1) (15860, 1) (16388, 1) (16184, 1)
### il6 kd size # (15562, 1) (15695, 1) (15912, 1) (15741, 1) (9382, 1) (16191, 1) (15675, 1) (15605, 1)

### ifn nt size (15738, 1) (16272, 1) (15887, 1) (15813, 1) (16070, 1) (15990, 1) (16735, 1) (15862, 1)
### ifn kd size (16305, 1) (15715, 1) (16175, 1) (16430, 1) (16636, 1) (16484, 1) (15621, 1) (17001, 1)


### expected size = 16546

df_il6_ifn_nt_kd = pd.concat([il6_nt_0,il6_nt_1,il6_nt_2,il6_nt_4,il6_nt_6,il6_nt_8,il6_nt_12,il6_nt_24,il6_kd_0,il6_kd_1,il6_kd_2,il6_kd_4,il6_kd_6,il6_kd_8,il6_kd_12,il6_kd_24,ifn_nt_0,ifn_nt_1,ifn_nt_2,ifn_nt_4,ifn_nt_6,ifn_nt_8,ifn_nt_12,ifn_nt_24,ifn_kd_0,ifn_kd_1,ifn_kd_2,ifn_kd_4,ifn_kd_6,ifn_kd_8,ifn_kd_12,ifn_kd_24], axis=1)
print(df_il6_ifn_nt_kd.shape)
# (25218, 32)
# %%
### Save il6 and ifn, nt and kd before replaing NaN
#df_il6_ifn_nt_kd.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/il6_ifn_nt+kd_NaN.csv')
# %%
### Replace non-existent values with 0
df_il6_ifn_nt_kd = df_il6_ifn_nt_kd.fillna(0)
### Save il6 and ifn nt and kd file
#df_il6_ifn_nt_kd.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/il6_ifn_nt+kd.csv')
# %%
### combine il6 nt and knockdown
### nt size # (16479, 1) (16546, 1) (16184, 1) (15730, 1) (15963, 1) (15860, 1) (16388, 1) (16184, 1)
### kd size # (15562, 1) (15695, 1) (15912, 1) (15741, 1) (9382, 1) (16191, 1) (15675, 1) (15605, 1)
### expected size = 16546

df_il6_ifn_nt_kd = pd.concat([il6_nt_0, il6_nt_1,il6_nt_2,il6_nt_4,il6_nt_6,il6_nt_8,il6_nt_12,il6_nt_24,il6_kd_0,il6_kd_1,il6_kd_2,il6_kd_4,il6_kd_6,il6_kd_8,il6_kd_12,il6_kd_24], axis=1)
print(df_il6_ifn_nt_kd.shape)
# (23114, 16)
df_il6_ifn_nt_kd.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/il6 nt+kd.csv')
df_il6_ifn_nt_kd = df_il6_ifn_nt_kd.fillna(0)
# %%
import pandas as pd
### Removes genes with all O in IL6 nt
il6_nt = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/il6_nt.csv',index_col=0)
print(il6_nt.shape)
# (25218, 8)
# %%
il6_nt = il6_nt.loc[~(il6_nt==0).all(axis=1)]
print(il6_nt.shape)
# (21576, 8)
il6_nt.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/il6_nt_minus0.csv')
# %%
### Removes genes with all O in IFNg nt
ifn_nt = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/ifn_nt.csv',index_col=0)
print(ifn_nt.shape)
# (25218, 8)
# %%
ifn_nt = ifn_nt.loc[~(ifn_nt==0).all(axis=1)]
print(ifn_nt.shape)
# (21514, 8)
ifn_nt.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/ifn_nt_minus0.csv')
# %%
import pandas as pd
# %%
### Merge IL6 nt minus 0 and kd
il6_nt_minus0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/il6_nt_minus0.csv',index_col=0)
print(il6_nt_minus0.shape)
# (21576, 8)
# %%
il6_kd = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6_raw/il6_kd.csv',index_col=0)
print(il6_kd.shape)
# (25218, 8)
# %%
df_il6 = pd.merge(il6_nt_minus0, il6_kd, left_index=True, right_index=True)
print(df_il6.shape)
# (21576, 16)
# %%
df_il6.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/il6_nt_minus0_kd.csv')
# %%
### Merge IFNg nt minus 0 and kd
ifn_nt_minus0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/ifn_nt_minus0.csv',index_col=0)
print(ifn_nt_minus0.shape)
# (21514, 8)
# %%
ifn_kd = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNG_raw/ifn_kd.csv',index_col=0)
print(ifn_kd.shape)
# (25218, 8)
# %%
df_ifn = pd.merge(ifn_nt_minus0, ifn_kd, left_index=True, right_index=True)
print(df_ifn.shape)
# (21514, 16)
# %%
df_ifn.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/ifn_nt_minus0_kd.csv')

# %%
df_il6.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/il6_corresponding_kd')
df_ifn.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/ifn_corresponding_kd')
# %%
### Merge il6 clusters with kd

il6_nt_minus0_stdev_graphia = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/Graphia graphs/il6_nt_minus0_stdev_log-attributes.csv',index_col=0)
print(il6_nt_minus0_stdev_graphia.shape)
# (15097, 12)

il6_minus0_kd = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6_raw/il6_minus0_kd.csv',index_col=0)
print(il6_minus0_kd.shape)
# (21576, 8)

df_il6 = pd.merge(il6_nt_minus0_stdev_graphia, il6_minus0_kd, left_index=True, right_index=True)
print(df_il6.shape)
# (15097, 20)
df_il6.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6_raw/il6_minus0_stdev_kd_clustered.csv')
# %%
### Merge ifng clusters with kd

ifn_nt_minus0_stdev_graphia = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/Graphia graphs/ifn_nt_minus0_stdev_log-attributes.csv',index_col=0)
print(ifn_nt_minus0_stdev_graphia.shape)
# (15181, 12)

ifn_minus0_kd = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg_raw/ifn_minus0_kd.csv',index_col=0)
print(ifn_minus0_kd.shape)
# (21514, 8)

df_ifn = pd.merge(ifn_nt_minus0_stdev_graphia, ifn_minus0_kd, left_index=True, right_index=True)
print(df_ifn.shape)
# (15181, 20)
df_ifn.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg_raw/ifn_minus0_stdev_kd_clustered.csv')
# %%

# %%
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from bioinfokit.analys import get_data
import numpy as np
# Normalize 
df =pd.read_csv(r'/Volumes/Untitled/Gene level feature count/DE/condition_FT_M1vsV_M0_dge.csv',index_col=0)
# %%
df_st =  StandardScaler().fit_transform(df)  
pd.DataFrame(df_st, columns=df.columns).head(2)
# %%
pca_out = PCA().fit(df_st)

# get the component variance
# Proportion of Variance (from PC1 to PC6)
pca_out.explained_variance_ratio_
# %%
np.cumsum(pca_out.explained_variance_ratio_)
# %%
loadings = pca_out.components_
num_pc = pca_out.n_features_
pc_list = ["PC"+str(i) for i in list(range(1, num_pc+1))]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = df.columns.values
loadings_df = loadings_df.set_index('variable')
loadings_df

# %%
# get correlation matrix plot for loadings
import seaborn as sns
import matplotlib.pyplot as plt
ax = sns.heatmap(loadings_df, annot=True, cmap='Spectral')
plt.show()
# %%
# get eigenvalues (variance explained by each PC)  
pca_out.explained_variance_
# get scree plot (for scree or elbow test)
from bioinfokit.visuz import cluster
cluster.screeplot(obj=[pc_list, pca_out.explained_variance_ratio_])
# %%
# get PCA loadings plots (2D and 3D)
# 2D
cluster.pcaplot(x=loadings[0], y=loadings[1], labels=df.columns.values, 
    var1=round(pca_out.explained_variance_ratio_[0]*100, 2),
    var2=round(pca_out.explained_variance_ratio_[1]*100, 2))

# 3D
cluster.pcaplot(x=loadings[0], y=loadings[1], z=loadings[2],  labels=df.columns.values, 
    var1=round(pca_out.explained_variance_ratio_[0]*100, 2), var2=round(pca_out.explained_variance_ratio_[1]*100, 2), 
    var3=round(pca_out.explained_variance_ratio_[2]*100, 2))
# %%
merged = merged.fillna(0)

merged.to_csv('v_na_mo.csv')
# %%
# import packages
import pandas as pd
from bioinfokit import visuz

# import the DGE table (condition_infected_vs_control_dge.csv)
df = pd.read_csv(r'/Volumes/Untitled/Gene level feature count/DE/condition_HD11_M2vsV_M0_dge.csv')
# drop NA values
df=df.dropna()
# df['pval']= df["padj"] + 0.00000001
# %%
# create volcano plot
visuz.GeneExpression.volcano(df=df, lfc="log2FoldChange", pv="padj", geneid="Unnamed: 0",gstyle=2, sign_line=True, r = 500)
# genenames=("Cd68", "Cd163","Cd80", "Irf5", "Il15", "Il18","IL6","Ccl2","Ccl8")
# genenames=("Cxcl10", "Nos2", "Ccl24", "Il1b","Il6") ,"Cd86","Il6","Stat1","Ccl8","Cxcl5","Nos2"
# genenames=("Pcp4","Filip1" "Il1b", 'Il6',"Ccl8","Arg1", "Il10")
#  genenames=("Cd80", "Cd68", "Cd163","Irf5" ,"Il6", "Il15", "Il18", "Ccl2", "Ccl8","Cxcl5", "Ccl20", "Cx3cl1")
# # geneid= 'Unnamed: 0', genenames=('Nos2', 'Ccr7', 'Il12b', 'Il6', 'Il1b', 'Cd86')
#     genenames=("Cd80", "Cd68", "Cd163","Irf5" ,"Il6", "Il15", "Il18", "Ccl2", "Ccl8","Cxcl5", "Ccl20", "Cx3cl1"), sign_line=True)
# %%
import pandas as pd 
df = pd.read_csv(r'/Users/hawacoulibaly/Desktop/SM1 combination study/SM1_ENSEMBL_Genes.csv')
df.head(2)
# %% 
### df1 = df(['Unnamed: 0', 'ENSEMBL', 'Unnamed: 2', 'Unnamed: 3', 'GeneID'])

df1 = df.set_index('GeneID')
# %%
df2 = df1.groupby(level=0).sum()
print(df2.shape)
# %%
df2.to_csv('SM1_ENSEMBL_Genes_processed.csv')
# %%
# import packages
import pandas as pd
from bioinfokit import visuz

# import the DGE table (condition_infected_vs_control_dge.csv)
df = pd.read_csv(r'/Volumes/Untitled/Gene level feature count/DE/condition_M2_vs_M0_dge.csv')
# drop NA values
df=df.dropna()
# %%
# create volcano plot
visuz.GeneExpression.volcano(df=df, lfc="log2FoldChange", pv="padj", geneid="Unnamed: 0",
    genenames=("Clec10a","Cxcr1", "Arg1", "Irf4", "Pparg",  "Ccl2",  "Ccl22",  "Irf4",  "Cxcl16"), gstyle=2, sign_line=True, r = 500)
# geneid= 'Unnamed: 0', genenames=('Nos2', 'Ccr7', 'Il12b', 'Il6', 'Il1b', 'Cd86')
#     genenames=("Cd80", "Cd68", "Cd163","Irf5" ,"Il6", "Il15", "Il18", "Ccl2", "Ccl8","Cxcl5", "Ccl20", "Cx3cl1"), sign_line=True)

# %%
import pandas as pd
df1 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/M1 markers.csv", index_col=0)
df2 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/M2 markers.csv", index_col=0)

v0=pd.read_csv(r"/Users/hawacoulibaly/Desktop/EDGER/NextA/DEG_results_NA_M0 vs. NA_M2.csv", index_col=0)


v_1= pd.merge(v0, df1, left_index=True, right_index=True)
v_2 = pd.merge(v0, df2, left_index=True, right_index=True)

v_1.to_csv('1DEG_results_NA_M0 vs. NA_M2.csv')
v_2.to_csv('2DEG_results_NA_M0 vs. NA_M2.csv')

# %%
import pandas as pd
chemo =pd.read_csv(r"/Users/hawacoulibaly/Desktop/Chemokines copy.csv", index_col=0)
v0=pd.read_csv(r"/Users/hawacoulibaly/Desktop/EDGER/NextA/DEG_results_V_M2 vs. NA_M2.csv", index_col=0)

v_chemo= pd.merge(v0, chemo, left_index=True, right_index=True)
v_chemo.to_csv('chemoDEG_results_V_M2 vs. NA_M2.csv')


# %%
import pandas as pd
df1 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/m1_m2_final_markers.csv",  index_col=0)
df2 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/all_genes_all_conditions.csv", index_col=0)

# %%
df= pd.merge(df1, df2, left_index=True, right_index=True)
df.to_csv('m1_m2_all.csv')

# %%
import pandas as pd
df1 =pd.read_csv(r"/Users/hawacoulibaly/Documents/TIME COURSE/kd_il6_allclusters.csv",  index_col=0)
df2 =pd.read_csv(r"/Users/hawacoulibaly/Documents/TIME COURSE/kd_ifn_allclusters.csv", index_col=0)

df3 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/il6_nt_kd_all.csv",  index_col=0)
df4 =pd.read_csv(r"/Users/hawacoulibaly/Desktop/ifn_nt_kd_all.csv", index_col=0)

# %%
dfx= pd.merge(df1, df3, left_index=True, right_index=True)
dfx.to_csv('nt_kd_il6_all_clusters_raw.csv')

dfxx= pd.merge(df2, df4, left_index=True, right_index=True)
dfxx.to_csv('nt_kd_ifn_all_clusters_raw.csv')

# %%
import pandas as pd

user = pd.read_csv(r"/Users/hawacoulibaly/Documents/TIME COURSE/KD_vs_NT_NOISeq_results/IFNg/NT vs KD analysis/ifn_log_cluster_merged_kd_log.csv", index_col=0)
# %%
for u in user['MCL Cluster'].unique():
    file_name = 'IFNg_Cluster_kd_log_{0}.csv'.format(u) 
    user[user['MCL Cluster'] == u].to_csv(file_name, sep=',') 
# %%
### Lollipop chart marker 
import pandas as pd

# Prepare Data
df_raw = pd.read_csv(r"/Users/hawacoulibaly/Desktop/il6_cluster2_prism.csv")
# %%
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', inplace=True)
df.reset_index(inplace=True)

# Draw plot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
ax.vlines(x=df.index, ymin=0, ymax=df.cty, color='firebrick', alpha=0.7, linewidth=2)
ax.scatter(x=df.index, y=df.cty, s=75, color='firebrick', alpha=0.7)

# Title, Label, Ticks and Ylim
ax.set_title('Lollipop Chart for Highway Mileage', fontdict={'size':22})
ax.set_ylabel('Miles Per Gallon')
ax.set_xticks(df.index)
ax.set_xticklabels(df.manufacturer.str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
ax.set_ylim(0, 30)

# Annotate
for row in df.itertuples():
    ax.text(row.Index, row.cty+.5, s=round(row.cty, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=14)

plt.show()
# %%
import pandas as pd
import matplotlib.pyplot as plt
# Prepare Data
df = pd.read_csv(r"/Users/hawacoulibaly/Documents/TIME COURSE/il6_DEG_div_bar.csv")
x = df.loc[:, ['Log2FC']]
# %%

df['Log2FC_z'] = (x - x.mean())/x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['Log2FC_z']]
df.sort_values('Log2FC_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(14,10), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.Log2FC_z, color=df.colors, alpha=0.4, linewidth=5)

# Decorations
plt.gca().set(ylabel='$Genes$', xlabel='$Log2FC$')
plt.yticks(df.index, df.Genes, fontsize=12)
plt.title('Diverging Bars of Genes Fold Changes', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.show()
plt.savefig('il6.pdf')  
# %%
import pandas as pd

v0 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/KD_vs_NT_NOISeq_results/IFNg/NT vs KD analysis/ifn_merged.csv', index_col=0)
v1 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/KD_vs_NT_NOISeq_results/IFNg/NT vs KD analysis/ifn_nt_vs_kd_clusters.csv', index_col=0)
# %%
merged = pd.merge(v0, v1, left_index=True, right_index=True)

# %%
merged.to_csv('ifn_raw_cluster_merged.csv')
# %%
import pandas as pd 
df = pd.read_csv(r'/Users/hawacoulibaly/Desktop/SM1 combination study/SM1_TPM_all.csv', index_col=0)
# %%
df1 = df.loc[~(df==0).all(axis=1)]
# %%
df1.to_csv('SM1_all_filtered.csv')
# %%
