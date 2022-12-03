#!/usr/bin/env python
# coding: utf-8

# # 1. Create a null vector of size 10 but the fifth value which is 1.

# In[1]:


import numpy as np


# In[2]:


x = np.zeros(10); x[4] = 1
print(x)


# # 2. Create a vector with values ranging from 10 to 49.

# In[3]:


x = np.array(range(10,50))
print(x)


# # 3. Create a 3x3 matrix with values ranging from 0 to 8.
# 

# In[4]:


x = np.array(range(0,9)).reshape(3,3)
print(x)


# # 4. Find indices of non-zero elements from [1,2,0,0,4,0].

# In[5]:


x = np.array([1,2,0,0,4,0])
print("Indices of non-zero element are :")
for i in range(len(x)):
    if x[i] != 0:
        print(i)


# # 5. Create a 10x10 array with random values and find the minimum and maximum values.

# In[6]:


import random
x = np.random.randint(0,100,size=(10,10))
print("Array:",x)
max1 = x.max()
min1 = x.min()
print("Minimum value is :",min1)
print("Maximum value is :",max1)


# # 6. Create a random vector of size 30 and find the mean value.

# In[7]:


x = np.random.randint(0,100,size=(30))
print("Vector",x)
y = x.mean()
print("Mean",y)

