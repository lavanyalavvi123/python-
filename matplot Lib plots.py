#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# generate random numbers (total 10)
randomNumber = np.random.rand(10)
randomNumber


# In[3]:


plt.plot(randomNumber, 'g', label='ABC', linewidth=6)
plt.xlabel("Num")
plt.ylabel('Ration 123')
plt.title('ratio trend over the years 2020')
plt.legend()#
plt.show()


# In[5]:


# website traffic data
web_customers = [123,645, 950, 1290,163, 1455, 1334,465, 205,80]

# time distribution (hourly)
time_hrs = [7,8,9,10,11,12,13,14,15,16]


# In[6]:


# select the style of the plot
#style.use('ggplot')

#plot the random numner
plt.plot(time_hrs, web_customers,label="WEB ANALYSIS",
        color='r', linestyle='--', linewidth=2.5)

plt.xlabel('Hours')
plt.ylabel('No of users')
plt.title('web site traffic')
plt.legend()
plt.show()


# In[19]:


#plot the random numner
plt.plot(time_hrs, web_customers,label="WEB ANALYSIS",
        color='r', linestyle='--', linewidth=2.5)

plt.xlim(6,20)
plt.ylim(70,1700)
plt.xlabel('Hours')
plt.ylabel('No of users')
plt.title('web site traffic')
plt.legend()
plt.show()


# In[7]:


#plot the random numner
plt.plot(time_hrs, web_customers,
         label="WEB ANALYSIS",
        color='r',
         linestyle='--',
         linewidth=2.5,
        alpha=0.5)
#new: alpha range 0-1
#alpha 0---transperent and 1 visible
plt.axis([4, 20, 0, 2000])
plt.xlim(6,20)
plt.ylim(70,1700)
plt.xlabel('Hours')
plt.ylabel('No of users')
plt.title('web site traffic')
plt.legend()
plt.show()


# In[10]:


#select the style of the plot
#style.use('seaborn')
print(time_hrs)
print(web_customers)

# plot the random number
plt.plot(time_hrs, web_customers, linestyle='--', linewidth=2.5, alpha=.5)
plt.axis([4,20, 0, 1600])

plt.annotate('Maximum',
            xy=(11,1600),
             xytext=(914,1600),
             arrowprops={'facecolor' : 'blue'})

plt.xlabel('Hours')
plt.ylabel('No of users')
plt.title('web site traffic')
plt.show()


# In[12]:


import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y =[5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='scatter plot', color='r', marker="*", s=500)

plt.xlabel('x')
plt.ylabel('y')
plt.tittle('intresting grapgh')


# In[ ]:


plt.figure(figsize=(16,5))

x = range(10)
y = range(10)

plt.subplot(3,2,1)
plt.plot(x,y, 'r-p',ms=15)
# plt.plot(a,c,"g")

plt.subplot(3,2,2)
plt.plot(x,y, 'b:^',ms=15)

plt.subplot(3,2,3)
plt.plot(x,y, 'g--o',ms=15)

plt.subplot(3,2,4)
plt.plot(x,y, 'c-*',ms=15)

plt.subplot(3,2,5)
plt.subplot(3,2,6)


# In[17]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

friends = [70, 65, 72, 63, 62, 70, 78, 50, 65]
minutes = [120, 165, 130, 122, 143, 158, 160, 123, 100]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list(zip(labels,friends,minutes)))
plt.scatter(friends, minutes)

#label each point
for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
    xy=(friend_count,minute_count),
    xytext=(4,5),
    textcoords='offset points')
plt.title("Daily Minutes vs.Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()


# In[9]:


import matplotlib.pyplot as plt


# In[11]:


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='scatter plot', color='r',marker="*",s=500)

plt.xlabel('x')
plt.ylabel('y')
plt.title("intresting Graph\ncheck is out")
plt.legend


# bar chart

# In[ ]:




