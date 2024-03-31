#!/usr/bin/env python
# coding: utf-8

# In[10]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


sns.countplot(x=data.survived,data=data)
plt.show


# In[12]:


data=sns.load_dataset("titanic")
data.head(3)


# # exploratary

# In[13]:


data.info()


# In[14]:


sns.countplot(x=data.alive,data=data)
plt.show


# In[15]:


data.describe().T


# # Exploratoty data analysis(EDA)

# In[16]:


data


# In[17]:


sns.countplot(x=data.who,data=data)
plt.show()


# In[18]:


data.who.value_counts()


# In[19]:


sns.countplot(x=data.alive,hue=data.who,data=data)
plt.show()


# In[20]:


pd.crosstab(data.who,data.survived)


# In[21]:


sns.countplot(x=data.who,hue=data.alive,data=data)
plt.show()


# In[22]:


data.head(1)


# In[23]:


sns.countplot(x=data.pclass,data=data)
plt.show()


# In[24]:


sns.countplot(x=data.pclass,hue=data.alive,data=data)
plt.show()


# In[25]:


pd.crosstab(data.pclass,data.alive)


# In[26]:


sns.countplot(x=data.pclass,hue=data.who,data=data)
plt.show()


# In[27]:


sns.countplot(x=data.pclass,hue=data.sex,data=data)
plt.show()


# In[28]:


data.head(1)


# In[29]:


sns.displot(x=data.age,data=data)
plt.show()


# In[30]:


sns.displot(x=data.age,data=data,kde=True) #KDE=kernal density,hue=particalar shade or colour
plt.show()


# In[31]:


sns.scatterplot(x=data.fare,y=data.age,data=data)
plt.show()


# In[32]:


sns.scatterplot(x=data.fare,y=data.age,hue=data.alive,data=data)
plt.show()


# In[33]:


sns.countplot(x=data.sibsp,hue=data.alive,data=data)
plt.show()


# In[34]:


sns.countplot(x=data.sibsp+data.parch,hue=data.alive,data=data)
plt.show()


# In[35]:


#embark_town
sns.countplot(x=data.embark_town,data=data)
plt.show()


# In[36]:


#embark_town
sns.countplot(x=data.embark_town,hue=data.alive,data=data)
plt.show()


# In[37]:


#embark_town
sns.countplot(x=data.embark_town,hue=data.pclass,data=data)
plt.show()


# In[38]:


#embark_town
sns.countplot(x=data.embark_town,hue=data.alive,data=data)
plt.show()


# #### take away from this EDA
# 1.Female has more chance to survive
# 2.child has more chance to survive
# 3. if family is 1,2 and 3 members then more chance to survive
# 4.class 1st people has more chance to survive
# 5.more fare amount=1st class people

# In[9]:


#corelation
sns.heatmap(data.corr())
plt.show()


# In[39]:


sns.heatmap(data.corr(),vmin=1)
plt.show()


# In[40]:


sns.heatmap(data.corr(),vmin=1,annot=True)
plt.show()


# In[42]:


sns.heatmap(data.corr()[data.corr()<-.5],vmin=1,annot=True)
plt.show()


# In[ ]:




