#!/usr/bin/env python
# coding: utf-8

# In[1]:


# compute


# In[3]:


import numpy as np

def avg_value(*n):
    #l1=len(n)
    avegerage=np.mean(n) #sum(n)/l1
    return avegerage


# In[5]:


avg_value(10,20,30,40,50,60)


# In[7]:


import numpy as np

def median_value(*n):
    md=np.median(n)
    return md


# In[13]:


median_value(10,20,30,40,50,60)
# logic if middle values is two then add both and divide them with 2


# In[15]:


median_value(10,20,30,40,50,60,70)
# if it consist only one in middle that is final median value


# In[ ]:




