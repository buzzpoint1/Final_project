#!/usr/bin/env python
# coding: utf-8

# In[208]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import csv


# In[209]:


df = pd.read_csv('monthly_SingleHome_family.csv')


# In[210]:


#missing value testing

df.isnull()


# In[211]:


#count total missing volues
pd.isnull(df).sum().sum()


# In[212]:


#detect a list of missing values

missing_Valus=[""]
missing=df.isin(missing_Valus)
missing.head


# In[219]:


df.head(15)


# In[214]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Median_Sale_Price'],
                y=df['Average_Sale_Price'])


# In[215]:


#missing values

missingValues = df[(df['Median_Sale_Price']=='')]
print(missingValues.head(10))


# In[216]:


#colums heading into list
list(df.columns)


# In[223]:


dfaapl = pd.read_csv('AAPL.csv')


# In[228]:


#checking to see values working
dfaapl.head()


# In[226]:


dfgoog = pd.read_csv('GOOG.csv')


# In[230]:



#checking goog 
dfgoog.head()


# In[233]:


#reading Data from Files using Import CSV loop and list
myAapl=open("AAPL.csv","r")
reader = csv.reader(myAapl)
headers=next(reader,None)
#column headers
print(headers)
count = 0
for x in reader:
    #date,open,close,volume
    print(x[0],x[1],x[4],x[6])
    count = count +1
print(count)
myAapl.close()


# In[234]:


dfaapl['Close'].plot()
plt.show()


# In[ ]:


dfaapl['Close'].plot(Label='Stocks At Closing', figsize=)

