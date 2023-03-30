#!/usr/bin/env python
# coding: utf-8

# In[405]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import csv
import datetime as dt
import matplotlib.dates as dates


# In[406]:


df = pd.read_csv('monthly_SingleHome_family.csv')


# In[407]:


#missing value testing

df.isnull()


# In[408]:


#count total missing volues
pd.isnull(df).sum().sum()


# In[409]:


#detect a list of missing values

missing_Valus=[""]
missing=df.isin(missing_Valus)
missing.head


# In[410]:


df.head(15)


# In[443]:


#Get the mean for Average Sale Price column

df['Average_Sale_Price'].mean()



# In[444]:


#Sum for Average Sale Price Column

df['Average_Sale_Price'].sum()


# In[445]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Median_Sale_Price'],
                y=df['Average_Sale_Price'])


# In[446]:


#missing values

missingValues = df[(df['Median_Sale_Price']=='')]
print(missingValues.head(10))


# In[447]:


#colums heading into list
list(df.columns)


# In[448]:


# Aapple with dates
dfaapl = pd.read_csv('AAPL.csv',index_col='Date',parse_dates= True)


# In[449]:


#checking to see values working
dfaapl.head()


# In[450]:


dfgoog = pd.read_csv('GOOG.csv',index_col='Date',parse_dates= True)


# In[451]:



#checking goog 
dfgoog.head()


# In[452]:


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


# In[453]:


dfaapl['Close'].plot()
plt.show()


# In[454]:


#Stock graph 
dfaapl['Close'].plot(label='Stocks At Closing', figsize=(16,5))
dfaapl['Open'].plot(label='Stock Prices at Open')
dfaapl['High'].plot(label='Stock Prices at High')
dfaapl['Low'].plot(label='Stock Prices at Low')
plt.legend()
plt.title('Apple Stock Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[455]:


#Comparing Apple and Google at Close to see how we can pridict one stock by another stock
dfaapl['Close'].plot(label='Apple at Close', figsize=(16,5))
dfgoog['Close'].plot(label='Google at Close')
plt.legend()
plt.title(' Stocks Close Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[456]:


#Comparing Apple and Google at Open to see how we can pridict one stock by another stock
dfaapl['Open'].plot(label='Apple at Open', figsize=(16,5))
dfgoog['Open'].plot(label='Google at Open')

plt.legend()
plt.title(' Stocks Open Prices')
plt.ylabel('Stock Prices')
plt.show()


# In[457]:


#Comparing Apple and Google Volume to see how we can pridict one stock by another stock
dfaapl['Volume'].plot(label='Apple Volume', figsize=(16,5))
dfgoog['Volume'].plot(label='Google Volume')

plt.legend()
plt.title(' Stocks Volume')
plt.ylabel('Stock Prices')
plt.show()


# In[460]:


#Analyzing the Market Gap. First add Column 'Total Traded Aapleinto CSV'
dfaapl['Total Traded']= dfaapl['Open']*dfaapl['Volume']

# Check to see if Column was added
dfaapl


# In[462]:


#Now add Total Traded Column into Google Stock
dfgoog['Total Traded']= dfgoog['Open']*dfgoog['Volume']

# Check to see if Column was added
dfgoog


# In[469]:


#plotting Total traded for my stocks 
dfaapl['Total Traded'].plot(label='Apple Total Price Traded', figsize=(16,5))
dfgoog['Total Traded'].plot(label='Google Total Price Traded')

plt.legend()
plt.title(' Total Stokcs Traded')
plt.ylabel('Total Stock Traded')
plt.show()
#


# In[467]:


#Apple maximum Open price

print(dfaapl.Open.max())


# In[468]:


#what Row has the maximum open price

print(dfaapl[dfaapl.Open == dfaapl.Open.max()])


# In[472]:


# I would like to know when the peak of total traded happened for Apple Stock
# first where where exactly in data is the highest point

dfaapl['Total Traded'].argmax()

# when happened
dfaapl.iloc[[dfaapl['Total Traded'].argmax()]]


# In[473]:


#Now Same  peak for Google Stock
dfgoog['Total Traded'].argmax()

# when happened
dfgoog.iloc[[dfgoog['Total Traded'].argmax()]]


# In[ ]:




