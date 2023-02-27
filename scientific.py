#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from scipy.optimize import curve_fit


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import matplotlib.pyplot as plt


# In[7]:


(x,y)=np.loadtxt('datetemp.txt', dtype='U', delimiter=',', usecols=(0,1), unpack=True)


# In[8]:


print(x)


# In[9]:


print(y)


# In[17]:


plt.scatter(x,y)


# In[23]:


def line(x, a, b, c):
    return(a*np.cos(x*(2*3.142*x +b)) +c)


# In[ ]:


popt, pcov=curve_fit(line, x, y) 

