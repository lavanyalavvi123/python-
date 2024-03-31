#!/usr/bin/env python
# coding: utf-8

# # seaborn plot Titanic Data

# Exploratoty data analysis  EDA

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as Plot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data=sns.load_dataset("Titanic")
data.head(5)


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.describe().T


# In[8]:


data.columns


# Checking balancing

# In[10]:


sns.get_dataset_names()


# In[ ]:




