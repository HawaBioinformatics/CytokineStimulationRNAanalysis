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
# Save IL6 genes with all 0
import pandas as pd 
df_il6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6_raw/il6_nt.csv',index_col=0)
df_il6 = df_il6[df_il6.eq(0).all(1)]
print(df_il6.shape)
# (3642, 8)
df_il6.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6_raw/il6_non_expressed_genes.csv')
# %%
# Save IL6 genes with all 0

df_ifn = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg_raw/ifn_nt.csv',index_col=0)
df_ifn = df_ifn[df_ifn.eq(0).all(1)]
print(df_ifn.shape)
# (3704, 8)
df_ifn.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg_raw/ifng_non_expressed_genes.csv')

# %%