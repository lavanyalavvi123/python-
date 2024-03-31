#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Importing Libraries---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


sns.get_dataset_names()


# In[3]:


df = pd.read_csv("D:/python practice notes/05-11-2023/mpg.csv")
print(df.head(3))


# In[6]:


### create a copy of your actual data  (step-1)
mpg_df = df.copy()
print(mpg_df.head(2))


# In[7]:


#### checking the basic information of your data- step-2
print(mpg_df.shape)


# In[8]:


print(mpg_df.dtypes)


# In[9]:


print(mpg_df.info())


# In[13]:


#### Fill the null values step-3
print(mpg_df.columns)


# In[10]:


#### try to fill the null values with 0
mpg_df['horsepower'] = mpg_df['horsepower'].fillna(0)


# In[16]:


print(mpg_df.isnull().sum())


# In[17]:


print(mpg_df.isnull())  true means 1 & false means 0


# In[18]:


print(df.isnull().sum())


# # EDA-----Process

# In[19]:


### importing of libraries
### inserting/importing og your data
### data preprocessing
### Exploratory data analysis
### model plannig & Building
### Evaluation the performance of th model
### saving the best model
### use for production/deployment


# #### simple Linear regression model

# In[20]:


#### q: i want to create a predictive model for prediction of mpg(milage per gallon) based on weight 


# In[22]:


y = mpg_df['mpg']
print(y)


# In[24]:


x = mpg_df['weight']
print(x)


# In[25]:


mpg_df.shape


# process---1

# In[27]:


from sklearn.model_selection import train_test_split


# In[26]:


398*0.8


# In[31]:


training, testing = train_test_split(mpg_df,test_size=0.2)


# In[32]:


training.shape


# In[33]:


testing.shape


# In[34]:


training.head()


# In[35]:


testing.head()


# #### process-2

# In[36]:


from sklearn.model_selection import train_test_split


# In[37]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


# In[38]:


x_train.shape, y_train.shape


# In[40]:


x_test.shape, y_test.shape


# In[ ]:




