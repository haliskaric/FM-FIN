#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
get_ipython().run_line_magic('matplotlib', 'inline')
import yfinance as yf  
from scipy import stats
import quandl
import pandas as pd
from matplotlib.pyplot import figure
from scipy.stats import probplot
from scipy.stats import pearsonr
from scipy.stats import kurtosis
from scipy.stats import skew
import statistics


# In[2]:


# Stock price plotted against time
# Variables to start 
start = '2017-01-01'
end = '2022-01-01'

S1 = 'AMD'
S2 = 'KO'

#Calls the ticker symbol
stock1 = yf.Ticker(S1)
stock2 = yf.Ticker(S2)

#Calls the dataset shows date, close, open, volume etc.
stock1df = stock1.history(period='5y', method ='ffill')
stock2df = stock2.history(period='5y', method = 'ffill')

#assigns stock1Close the value of close values for stock1
stock1Close = stock1df['Close'].dropna()
stock2Close = stock2df['Close'].dropna()

#plots the values
stock1Close.plot(label = S1, figsize = (15,7))
stock2Close.plot(label = S2)


plt.legend()
plt.plot()


# In[3]:


stock1.info


# In[4]:


stock1.actions


# In[5]:


stock1.cashflow


# In[6]:


print(stock1Close)


# In[7]:


# Basic Daily returns plot based on %
daily_changes = stock1Close.pct_change(periods=1).dropna()

plt.figure(figsize=(20,13))
plt.xlabel('Date', size=24)
plt.ylabel('% returns', size=24)
plt.title('Dailey % Returns', size=24)
plt.plot(daily_changes)


# In[8]:


m = statistics.median(daily_changes)
daily_changes.describe()
s = statistics.stdev(daily_changes)
mean = statistics.mean(daily_changes)
s1 = s * 2
s2 = s * 3
s0 = -(s)
s_1 = s0 * 2
s_2 = s0 * 3


# In[10]:


plt.figure(figsize=(30,8),facecolor='#add8e6' ,edgecolor='blue')

bin_values = np.arange(start=-0.4, stop=0.4, step=0.01)

n, bins, patches = plt.hist(x=daily_changes, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=1)

plt.grid(axis='y')
plt.xlabel('% Value')
plt.ylabel('Frequency')
plt.title('HISP')
plt.axvline(s, color='#ff0000')
plt.axvline(s1, color='#ff0000')
plt.axvline(s2, color='#ff0000')
plt.axvline(mean, color='#00ff00')
plt.axvline(s0, color='#ff0000')
plt.axvline(s_1, color='#ff0000')
plt.axvline(s_2, color='#ff0000')



# In[116]:


for x in daily_changes:
    if x>0.1057116734239931:
        print(x)
        


# In[ ]:





# In[105]:


len(daily_changes)


# In[117]:


16/1258


# In[98]:


daily_changes.kurtosis()


# In[ ]:





# In[25]:


daily_changes.skew()


# In[ ]:


# This needs to be worked on/ modified for ease of use


time_period = 10
df_stock = yf.download(tickers = 'INTC', period = '10y', interval = '1d', group_by = 'ticker')

intc = df_stock['INTC'][['Close']].dropna()

max_index = len(intc['Close'])


intc_cagr = np.power((intc['Close'].iloc[max_index -1]/intc['Close'].iloc[0]), (1/time_period)) - 1
print(intc_cagr)


# In[26]:


figure = plt.figure(figsize=(8, 8))

ax = figure.add_subplot(111)

stats.probplot(daily_changes, dist='norm', plot=ax)

plt.show();


# In[ ]:


print(tslaClose)

corr = pearsonr(dailey_changes, another stock)
print(corr)


# In[ ]:





# In[ ]:





# In[ ]:




