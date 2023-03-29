#!/usr/bin/env python
# coding: utf-8

# In[341]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import csv
import datetime


# In[342]:


df = pd.read_csv('monthly_SingleHome_family.csv')


# In[343]:


#missing value testing

df.isnull()


# In[344]:


#count total missing volues
pd.isnull(df).sum().sum()


# In[345]:


#detect a list of missing values

missing_Valus=[""]
missing=df.isin(missing_Valus)
missing.head


# In[346]:


df.head(15)


# In[347]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Median_Sale_Price'],
                y=df['Average_Sale_Price'])


# In[348]:


#missing values

missingValues = df[(df['Median_Sale_Price']=='')]
print(missingValues.head(10))


# In[349]:


#colums heading into list
list(df.columns)


# In[350]:


dfaapl = pd.read_csv('AAPL.csv')


# In[351]:


#checking to see values working
dfaapl.head()


# In[352]:


dfgoog = pd.read_csv('GOOG.csv')


# In[353]:



#checking goog 
dfgoog.head()


# In[354]:


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


# In[355]:


dfaapl['Close'].plot()
plt.show()


# In[361]:


#Stock graph 
dfaapl['Close'].plot(label='Stocks At Closing', figsize=(16,5))
dfaapl['Open'].plot(label='Stock Prices at Open')
dfaapl['High'].plot(label='Stock Prices at High')
dfaapl['Low'].plot(label='Stock Prices at Low')
plt.legend()
plt.title('Apple Stock Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[363]:


#Comparing Apple and Google at Close to see how we can pridict one stock by another stock
dfaapl['Close'].plot(label='Apple at Close', figsize=(16,5))
dfgoog['Close'].plot(label='Google at Close')

plt.legend()
plt.title(' Stocks Close Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[364]:


#Comparing Apple and Google at Open to see how we can pridict one stock by another stock
dfaapl['Open'].plot(label='Apple at Open', figsize=(16,5))
dfgoog['Open'].plot(label='Google at Open')

plt.legend()
plt.title(' Stocks Open Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[366]:


#Comparing Apple and Google Volume to see how we can pridict one stock by another stock
dfaapl['Volume'].plot(label='Apple Volume', figsize=(16,5))
dfgoog['Volume'].plot(label='Google Volume')

plt.legend()
plt.title(' Stocks Volume')
plt.ylabel('Stock Prices')
plt.show()


# In[ ]:




