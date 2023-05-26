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
df_il6_nt_kd = df_il6_ifn_nt_kd[['n_0', 'n_1', 'n_2', 'n_4', 'n_6', 'n_8', 'n_12', 'n_24', 'k_0', 'k_1', 'k_2', 'k_4', 'k_6', 'k_8', 'k_12', 'k_24']]
df_ifn_nt_kd = df_il6_ifn_nt_kd[['ng_0', 'ng_1', 'ng_2','ng_4', 'ng_6', 'ng_8', 'ng_12', 'ng_24', 'kg_0', 'kg_1', 'kg_2','kg_4', 'kg_6', 'kg_8', 'kg_12', 'kg_24']]

print(df_il6_nt_kd.shape)
# (25218, 16)

print(df_ifn_nt_kd.shape)
# (25218, 16)
# %%
### Save il6 and ifn, nt and kd before replaing NaN
#df_il6_ifn_nt_kd.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/il6_ifn_nt+kd_NaN.csv')
# %%
### Replace non-existent values with 0
df_il6_nt_kd = df_il6_nt_kd.fillna(0)
df_ifn_nt_kd = df_ifn_nt_kd.fillna(0)
### Save il6 and ifn nt and kd file
#df_il6_ifn_nt_kd.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/il6_ifn_nt+kd.csv')
df_il6_nt_kd.to_csv('il6_nt_kd.csv')
df_ifn_nt_kd.to_csv('ifn_nt_kd.csv')
# %%
### Remove 0 across all times and NT/KD
df_il6_nt_kd_minus0 = df_il6_nt_kd.loc[~(df_il6_nt_kd==0).all(axis=1)]
print(df_il6_nt_kd_minus0.shape)
# (23091, 16)
df_ifn_nt_kd_minus0 = df_ifn_nt_kd.loc[~(df_ifn_nt_kd==0).all(axis=1)]
print(df_ifn_nt_kd_minus0.shape)
# (23555, 16)

df_il6_nt_kd_minus0.to_csv('il6_nt_kd_minus0.csv')
df_ifn_nt_kd_minus0.to_csv('ifn_nt_kd_minus0.csv')
# %%
import pandas as pd
### Create df for noiseq
df_il6 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/il6_nt_kd_minus0.csv',index_col=0)
df_ifn = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/ifn_nt_kd_minus0.csv',index_col=0)
# %%
df_il6_0 = df_il6[['n_0','k_0']]
df_il6_1 = df_il6[['n_1','k_1']]
df_il6_2 = df_il6[['n_2','k_2']]
df_il6_4 = df_il6[['n_4','k_4']]
df_il6_6 = df_il6[['n_6','k_6']]
df_il6_8 = df_il6[['n_8','k_8']]
df_il6_12 = df_il6[['n_12','k_12']]
df_il6_24 = df_il6[['n_24','k_24']]


# %%
df_il6_0.to_csv('il6_0hr.txt')
df_il6_1.to_csv('il6_1hr.txt')
df_il6_2.to_csv('il6_2hr.txt')
df_il6_4.to_csv('il6_4hr.txt')
df_il6_6.to_csv('il6_6hr.txt')
df_il6_8.to_csv('il6_8hr.txt')
df_il6_12.to_csv('il6_12hr.txt')
df_il6_24.to_csv('il6_24hr.txt')

# %%

df_ifn_0 = df_ifn[['ng_0','kg_0']]
df_ifn_1 = df_ifn[['ng_1','kg_1']]
df_ifn_2 = df_ifn[['ng_2','kg_2']]
df_ifn_4 = df_ifn[['ng_4','kg_4']]
df_ifn_6 = df_ifn[['ng_6','kg_6']]
df_ifn_8 = df_ifn[['ng_8','kg_8']]
df_ifn_12 = df_ifn[['ng_12','kg_12']]
df_ifn_24 = df_ifn[['ng_24','kg_24']]

# %%
df_ifn_0.to_csv('ifn_0hr.txt')
df_ifn_1.to_csv('ifn_1hr.txt')
df_ifn_2.to_csv('ifn_2hr.txt')
df_ifn_4.to_csv('ifn_4hr.txt')
df_ifn_6.to_csv('ifn_6hr.txt')
df_ifn_8.to_csv('ifn_8hr.txt')
df_ifn_12.to_csv('ifn_12hr.txt')
df_ifn_24.to_csv('ifn_24hr.txt')



# %%
import pandas as pd

df_il6= pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Graphia graphs/il6_nt_FPKM+1_stdev0.8-attributes.csv',index_col=0)
df_ifn = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Graphia graphs/ifn_nt_FPKM+1_stdev0.8-attributes.csv',index_col=0)

df_il6_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/Data/il6_nt_kd.csv',index_col=0)
df_ifn_2 = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/Data/ifn_nt_kd.csv',index_col=0)
# %%
df_il6_kd = pd.merge(df_il6, df_il6_2, left_index=True, right_index=True)
df_ifn_kd = pd.merge(df_ifn, df_ifn_2, left_index=True, right_index=True)
# %%
df_il6_kd.to_csv('il6_nt_kd_FPKM+1_minus0_stdev.csv')
df_ifn_kd.to_csv('ifn_nt_kd_FPKM+1_minus0_stdev.csv')
# %%
import pandas as pd
df = pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IL6/Data/il6_nt_kd_FPKM+1.csv',index_col=0)

max = df.to_numpy().max()
min = df.to_numpy().min()
print("1")
print(min,max)
# %%
dfa = df.loc[['Cluster nt 1', 'Cluster kd 1']]
max = dfa.to_numpy().max()
min = dfa.to_numpy().min()
print("1")
print(min,max)
# %%
import pandas as pd

df1=pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/Data/ifn_log2(FC)_KDvsNT_stdev0.8-attributes.csv', index_col=0)
df2=pd.read_csv(r'/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/Data/ifn_logFC_KDvsNT.csv', index_col=0)

df_il6_Fc = pd.merge(df1, df2, left_index=True, right_index=True)
df_il6_Fc.to_csv('/Users/hawacoulibaly/Documents/TIME COURSE/CURRENT/Prcessed data/IFNg/Data/IFN_fc.csv')
# %%
