#!/usr/bin/env python
# coding: utf-8

# In[1]:


t=(2,3,4,5,3,6)


# In[2]:


t.count(2)


# In[3]:


t=(2,3,4,5,3,6)


# In[4]:


t.count(3)


# In[5]:


t.count(4)


# In[8]:


t=(2,3,4,5,6)


# In[9]:


t.count(2)


# In[10]:


t.index(3)


# In[11]:


t.index(5)


# In[30]:


p=[2,3,4,5]
p


# In[31]:


p.append(10)
p


# In[28]:


c=0


# In[19]:


c+=1
c


# In[22]:


c=2


# In[26]:


c+=2
c


# In[32]:


P=[2,3,4,5,6]
P


# In[33]:


P.append(10)
P


# In[34]:


P.append(["a","b"])
P


# In[35]:


P[-1]


# In[37]:


P[5]


# In[39]:


P[6]


# In[40]:


P[6][0]


# In[41]:


P[6][1]


# In[52]:


q=["a","b" ,["c","d", ["e","f"]]]
q


# In[53]:


q[2]


# In[55]:


len(q)


# In[56]:


q[-1]


# In[57]:


q[-1][-1]


# In[58]:


q[-1][-1][-1]


# In[59]:


q[-1][-1][0]


# In[60]:


q[-3]


# In[61]:


q[0]


# In[62]:


q[1]


# In[65]:


l=[3,4]
l.extend("qwerty")
l


# In[66]:


p=[2,3,4,5]


# In[68]:


p.extend(["d","f"])
p


# In[69]:


p[-1]


# In[70]:


p[-4]


# In[72]:


p


# In[73]:


p.count(100)


# In[75]:


p.count(2)


# In[76]:


p.count("f")


# In[77]:


p


# In[78]:


p.index("d")


# In[81]:


p.index("f")


# In[82]:


p.index(2)


# In[84]:


p.index(3)


# In[85]:


s=['a','b','d','f']


# In[86]:


s


# In[91]:


s.insert(2,"c")
s


# In[92]:


s.insert(4,"e")
s


# In[93]:


s.insert(2,"c")
s


# In[98]:


w=[23,3,5]


# In[99]:


w


# In[100]:


w.insert(0,[3,5])
w


# In[101]:


w #Replacing by indexing


# In[104]:


w[0]="bb"
w


# In[105]:


t=[4,5] #5== -1
t


# In[106]:


t.insert(-1,3)
t


# In[ ]:




