#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.DataFrame({'age' : [23,25,26,27,28,29,22,25], 'height' : [5.2,4.5,5,5.5,4,5.3,5.1,6]})
print(data)


# In[5]:


x = data['age'].values
x


# In[7]:


y = data['height'].values
y


# In[8]:


x = data['age'].values.reshape(-1,1) #### in single array
x


# In[9]:


y = data['height'].values.reshape(-1,1)
y


# In[10]:


from sklearn.linear_model import LinearRegression


# In[11]:


lr = LinearRegression()
lr.fit(x,y)


# In[12]:


pred = lr.predict(x)
pred


# In[ ]:




