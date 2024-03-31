#!/usr/bin/env python
# coding: utf-8

# Array Numpy starts

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


fixed_salary = [100,200,300]
variable_salary = [10,20,30]
total_salary = fixed_salary + variable_salary
print(total_salary)


# In[3]:


type(fixed_salary)


# # Numpy for the solution

# In[4]:


import numpy as np


# In[5]:


fixed = np.array(fixed_salary)
variable = np.array(variable_salary)
total = fixed + variable
print(total)


# In[6]:


type(fixed)


# In[7]:


fixed


# In[8]:


variable


# In[9]:


total+10  #Broadcasting /element wise


# In[10]:


total>200


# In[11]:


total[total>200]


# In[12]:


total[total>200][1]


# filter all even value and find the sq of each

# In[13]:


ps = [2,3,4,5,6,7,8,9]
ps = np.array(ps)
ps_eve=ps[ps%2==0]
print(ps_eve)
print(ps_eve**2)


# In[14]:


print(ps)
ps[ps%2==0]**2


# In[15]:


list("abcde")


# In[16]:


data=pd.DataFrame((list("abcde"),[1,2,3,4,5],list("qwert"),[6,7,8,9,10]),
index=list("asdf"),
columns=list("mnxyz"))
data


# In[17]:


data=pd.DataFrame((list("abcde"),
                  [1,2,3,4,5],
                  list("qwert"),
                  [6,7,8,9,10]),
                 index=list("asdf"),
                 columns=list("mnxyz"))
data


# In[18]:


d={"k":[12,23,34],"k2":[17,34,55]}  #passing list
pd.DataFrame(d,index=list("abc"))


# In[19]:


d={"k":[12,23,34],"k2":[17,34,55]}
pd.DataFrame(d)


# In[20]:


a=['abc','xyz','pqr']
b=['q','w','r']
d={"k":a,"k2":b}
pd.DataFrame(d)


# In[21]:


a=['abc','xyz','pqr']
b="qwert"
d={"k":a,"k2":b}
pd.DataFrame(d)


# creating new DF variable

# In[22]:


import pandas as pd


# In[23]:


a=['abc','xyz','pqr']
b="qwert"
d={"k":a,"k2":b}
df=pd.DataFrame(d)
df


# In[24]:


df.info()


# In[25]:


df.describe()


# In[26]:


df.columns


# In[27]:


df.columns=["key1","key2"]
df


# In[28]:


df.rename(columns = {"key2" : "Names"},
inplace = True)


# In[29]:


df


# In[30]:


list(df.index)


# In[31]:


###3 columns does not exist


# In[32]:


df["key1"]


# In[33]:


df[["key1"]]


# In[34]:


dd={"k":[2,3,4,5,6],
    "k2":[22,23,24,25,26],
    "k3":[32,33,34,35,36],
    "k4":[42,43,44,45,46]}
df1=pd.DataFrame(dd)
df1


# In[35]:


df1[0:2]


# In[36]:


df1[2:]


# In[37]:


df1[:3]


# In[38]:


df1[:2]


# In[39]:


df1[["k2"]]


# In[40]:


df1[["k2","k3"]]


# In[41]:


df1[["k2","k3"]][:2]


# In[42]:


df1[["k2","k3"]][:3]


# Loc and Iloc

# In[43]:


df1.iloc[2]


# In[44]:


df1.iloc[[2]]


# In[45]:


df1.loc[[2]]


# In[47]:


df1.index=list("abcde") ###making index as str['a','b','c'......]
df1


# In[48]:


df1.iloc[[2]]


# In[51]:


df1.loc[['c']]


# loc take index name and iloc take index number

# In[52]:


df1


# In[53]:


df1.loc[['c'],['k2']]


# In[54]:


df1.loc[['c'],['k2','k3']]


# In[55]:


df1.loc[['c','d'],['k2','k3']]


# In[56]:


df1.loc[:,['k2']]


# In[57]:


df1.iloc[[1,2],[0,1]]  # row,col


# In[58]:


df1.info()


# In[59]:


df1.describe()


# In[60]:


df1.columns


# In[61]:


df.index


# In[62]:


df1["k2"].mean()


# In[64]:


df1.mean()


# In[65]:


np.percentile(df1["k"],25)


# In[66]:


np.percentile(df1["k2"],25)


# apply

# In[68]:


def x(a):
    return a**2


# In[69]:


x(3)


# In[70]:


x(9)


# In[71]:


df1.k


# In[73]:


df1.k.apply(x)


# In[75]:


x=lambda x:x**2
df1[["k","k2"]].apply(x)


# In[77]:


df1.k


# In[79]:


df1.k=df1.k.apply(x)
df1


# plot

# In[81]:


import pandas as pd
import numpy as np
#### from numpy.random import random as rm


# In[82]:


np.random.randint(1,100,10)


# In[83]:


np.random.random(10)


# In[85]:


data={"sales_1":np.random.randint(1,100,10),
     "sales_2":np.random.randint(1,100,10),
     "sales_3":np.random.randint(1,100,10),
     "sales_4":np.random.randint(1,100,10),}
mon=['jan','feb','march','april','may','jun','july','aug','sep','oct']
data=pd.DataFrame(data,index=mon)
data


# In[86]:


data.sales_1.plot()


# In[87]:


data[["sales_1","sales_2"]].plot(legend=True)


# In[90]:


data.sales_1.plot(kind="bar",legend=True)


# In[91]:


data[["sales_1","sales_2"]].plot(kind="bar",legend=True)


# In[94]:


data[["sales_1","sales_2"]].plot(kind="bar",legend=True,subplots=True)


# In[95]:


data.sales_1.plot(kind="pie")


# In[96]:


data[["sales_1","sales_2"]].plot(kind="pie",legend=True,subplots=True)


# In[97]:


data[["sales_1","sales_2"]].plot(kind="pie",legend=False,subplots=True)


# In[99]:


data.sales_3.plot(kind="barh",legend=True)


# In[100]:


data.plot(kind="area",legend=True)


# In[104]:


data.plot(title="month",
         legend=True,
         style=["r","b","g","k"],
         grid=True,
         fontsize=10,
         ylabel="Total",
          xlabel="Month wise",
         figsize=(15,8),
         subplots=True) #colormap=["r","b","g","k"]


# In[105]:


data.plot(kind="box")


# In[107]:


data.plot(kind="density")


# In[108]:


data.plot(kind="kde")


# In[109]:


data.plot(x="sales_1",y="sales_2",kind="scatter",s=500)


# In[110]:


data.plot(x="sales_1",y="sales_2",kind="hexbin",gridsize=10)


# In[ ]:




