#!/usr/bin/env python
# coding: utf-8

# # # pop

# In[1]:


p=[2,3,4,'a','b','c','d']
p


# In[2]:


p.pop()


# In[3]:


p


# In[4]:


p.pop(4)


# In[5]:


p.pop(3)


# In[6]:


p


# In[7]:


var=p.pop(2)
print(p)
var


# In[8]:


var


# # remove

# In[9]:


p


# In[10]:


p.remove("c")
p


# In[14]:


q=[[3,4,5],5]


# In[15]:


q.remove([3,4,5])
q


# # reverse

# In[16]:


p


# In[17]:


p.reverse()


# In[18]:


p


# # sort

# In[19]:


#p.sort()


# In[21]:


q=[4,2,6,3]
q.sort()
q


# In[22]:


q=list("qwert")
q.sort()
q


# # clear

# In[23]:


q.clear() # it's delete everything in the list
q


# # set

# In[24]:


# unique values #it won't allow the duplicates


# In[25]:


g=[2,3,4,5,6,2,2,6,9]


# In[26]:


g


# In[27]:


set(g) #no duplicacy


# In[28]:


s={2,3,4,4,4,4}
print(type(s))
print(s)


# In[29]:


a={"a","b","a"}


# In[30]:


a


# In[39]:


sa={1,2,3,4}
sb={3,4,5,6}
z={9,8,9}


# In[34]:


sa.issubset({1,2,3,4,5,6})


# In[43]:


z.issubset({1,2,3,4,5,6,7,9})


# # dictionary

# In[44]:


q={} # no value in {} that become the dictionary
type(q)


# In[46]:


q={2} #single value in {} that become the set
type(q)


# In[47]:


d={"k":100}


# In[48]:


d


# In[49]:


d["k"] #key to featch value


# In[50]:


d[100] #only looks for key-it won't read the value


# In[51]:


d


# In[52]:


d["k2"] #key is not there


# In[53]:


d["k2"]=200 #add a new value
d


# In[54]:


del(d["k"])
d


# In[77]:


di={"key":[2,3]}


# In[76]:


di


# In[80]:


di["key"].append(6) #it added the value at the end


# In[81]:


di


# In[83]:


#another syntax for dict
dd=dict(z=100,x=200,y=500)
dd


# In[84]:


dd.keys() #fetch me only keys


# In[85]:


dd.values() #fetch me only values


# In[86]:


dd.items() # fetch me only keys & value pair


# In[87]:


type(dd.items())


# In[88]:


dd["z"]


# In[89]:


dd["z"]=10000
dd


# In[100]:


data=dict(Name=["steeve","Sam","Toney"],Age=[34,36,42],EXP=[7,9,11])
data


# In[95]:


import pandas as pd


# In[96]:


pd.DataFrame(data)


# In[101]:


data["Name"].append("jane")
data["Age"].append(38)
data["EXP"].append(10)
data


# In[102]:


print(data["Name"][2])
print(data["EXP"][2])
data["EXP"][2]=12
data


# In[105]:


del(data["Name"][1])
del(data["Age"][1])
del(data["EXP"][1])
data


# In[111]:


data["salary"]=[300000]
data

