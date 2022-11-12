#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt
import matplotlib.axes as axes
import matplotlib.font_manager
import matplotlib.axis as axis
from matplotlib import rc, rcParams


# Task 1

# In[2]:


def read_gff(filename):
    return pd.read_csv(filename, sep = "\t", comment="#", names=[
                "chromosome",
                "source",
                "type",
                "start",
                "end",
                "score",
                "strand",
                "phase",
                "attributes"])



# In[3]:


#reading gff
df = read_gff("/Users/ekaterinagrigorieva/Downloads/rrna_annotation.gff")
df


# In[4]:


#removing unwanted info from attributes
df['attributes'] = df['attributes'].map(lambda x: x.lstrip('Name=').rstrip('ribosomal RNA').replace("_rRNA;product=", ""))
df['attributes'] = df['attributes'].map(lambda x: x[:len(x)//2])
df


# In[5]:


#creating df for barplot
df_types = pd.DataFrame(data = np.array(list(df['chromosome'].unique())*3), columns=["sequence"])
df_types["RNA type"] =  ["16S"]*26 + ["23S"]*26 + ["5S"]*26
df_types["count"] = 0
df_types = df_types.sort_values("sequence").reset_index(drop = True)
for i in range(len(df_types['sequence'])):
    df_types.iloc[i, 2] += len(df[(df["attributes"] == df_types.iloc[i, 1])&(df["chromosome"] == df_types.iloc[i, 0])])
df_types 
    


# In[6]:


#barplot
plt.figure(figsize = (15, 9))
sns.barplot(data=df_types, x = "sequence", y = "count", hue = "RNA type")
plt.xticks(rotation=90)
plt.show()


# In[7]:


def read_bed6(filename):
    return pd.read_csv(filename, sep = "\t", names=[
                "chromosome",
                "start",
                "end",
                "name",
                "score",
                "strand"])



# In[8]:


df_contigs = read_bed6("/Users/ekaterinagrigorieva/Downloads/alignment.bed")
df_contigs


# In[9]:


#changed names of columns
df.rename(columns={'start': 'start_x', 'end': 'end_x', 'score': 'score_x', 'strand': 'strand_x'}, inplace=True)
df


# In[10]:


#changed names of columns
df_contigs.rename(columns={'start': 'start_y', 'end': 'end_y', 'score': 'score_y', 'strand': 'strand_y', 'name': 'contigs'}, inplace=True)
df_contigs


# In[11]:


#merging tables gives us all possible variants
df_intersect = df.merge(df_contigs, left_on='chromosome', right_on='chromosome')
df_intersect


# In[12]:


#sorting
df_intersect = df_intersect.query('start_x > start_y and end_x < end_y').drop_duplicates("start_x")
df_intersect


# Task 2

# In[13]:


df_diff = pd.read_csv("/Users/ekaterinagrigorieva/Downloads/diffexpr_data.tsv.gz", sep = '\t')


# In[14]:


df_diff


# In[15]:


print(min(df_diff["logFC"]), max(df_diff["logFC"]), min(df_diff["log_pval"]), max(df_diff["log_pval"]))


# In[16]:


df_diff.loc[(df_diff['logFC'] > 0) & (df_diff['log_pval'] < -np.log10(0.05)), 'DEG'] = 'Non-significally upregulated'
df_diff.loc[(df_diff['logFC'] < 0) & (df_diff['log_pval'] < -np.log10(0.05)), 'DEG'] = 'Non-significally downregulated'
df_diff.loc[(df_diff['logFC'] > 0) & (df_diff['log_pval'] > -np.log10(0.05)), 'DEG'] = 'Significally upregulated'
df_diff.loc[(df_diff['logFC'] < 0) & (df_diff['log_pval'] > -np.log10(0.05)), 'DEG'] = 'Significally downregulated'
df_diff = df_diff.sort_values("log_pval", ascending=False)


# In[17]:


top2_up = df_diff.loc[(df_diff['DEG'] == 'Significally upregulated')].sort_values('logFC', ascending=False)[0:2]
top2_up


# In[18]:


top2_down = df_diff.loc[(df_diff['DEG'] == 'Significally downregulated')].sort_values('logFC', ascending=True)[0:2]
top2_down


# In[107]:


plt.figure(figsize=(13,8), dpi = 300, linewidth = 0)
sns.set(font="Verdana", style = 'ticks')
rc('font', weight='bold')
matplotlib.font_manager.FontManager(weight='bold')
plt.axvline(0, 0,200, lw = 1.5, linestyle = "dashed", c = "grey")
plt.axhline(-np.log10(0.05), -20,20, lw = 1.5, linestyle = "dashed", c = "dimgrey")
plt.text(8, -np.log10(0.05)+0.5, "p value = 0.05", weight = 'bold', c = 'dimgrey', size = 11.5)
plt.xlabel(r'$\bf{log_{2}}$' + '(fold change)', weight = 'bold', style = 'italic', c = 'black', size = 15)
plt.ylabel(r'$\bf{-log_{10}}$' + '(p value corrected)', weight = 'bold', style = 'italic', size = 15, c = 'black')
plt.title('Volcano plot', weight = 'bold', style = 'italic', size = 20, c = 'black')
plt.xlim(min(df_diff["logFC"])-1, min(df_diff["logFC"])*(-1)+1)
fig = sns.scatterplot(data=df_diff, x="logFC", y="log_pval", hue = "DEG", s = 13, linewidth=0, palette = "tab10")
fig.axes.minorticks_on()
fig.axes.tick_params(axis='both', which = 'major', width = 2)
fig.axes.spines['bottom'].set_linewidth(2)
fig.axes.spines['left'].set_linewidth(2)
fig.axes.spines['right'].set_linewidth(2)
fig.axes.spines['top'].set_linewidth(2)
fig.axes.annotate('UMOD', (-10.661093, 53.117378), xycoords='data',
            xytext=(-11, 65), arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='top')
fig.axes.annotate('ZIC2', (4.571915, 4.075183), xycoords='data',
            xytext=(5, 15), arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='top')
fig.axes.annotate('MUC7', (-9.196481, 3.171498), xycoords='data',
            xytext=(-10, 15), arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='top')
fig.axes.annotate('ZIC5', (4.2767451, 5.121027), xycoords='data',
            xytext=(4.5, 15), arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
handles, labels = fig.axes.get_legend_handles_labels()
fig.axes.legend(handles=handles[0:], labels=labels[0:], shadow = True, markerscale=1.5, prop = {'weight':'bold'})


# In[ ]:




