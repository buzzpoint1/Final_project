#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("~/Desktop/Final_Projectt/monthly_SingleHome_family.csv")


# In[6]:


df.head()


# In[10]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Median Sale Price'],
                y=df['Average Sale Price'])


# In[ ]:




