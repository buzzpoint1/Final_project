#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import csv


# In[147]:


df = pd.read_csv('monthly_SingleHome_family.csv')


# In[148]:


df.head(10)


# In[141]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Median_Sale_Price'],
                y=df['Average_Sale_Price'])


# In[143]:


#missing values

missingValues = df[(df['Median_Sale_Price']=='0.00')]
print(missingValues.head(10))


# In[136]:


#colums heading into list
list(df.columns)


# In[ ]:





# In[ ]:





# In[ ]:




