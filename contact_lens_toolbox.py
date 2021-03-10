#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[15]:


abbr_df=pd.read_csv("./tools/abbreviation.csv");


# In[16]:


def tellmeWTFis(abbr_word,abbr_df=abbr_df):
    
    print(abbr_df.where(abbr_df["abbreviation"]==abbr_word).dropna())
    




