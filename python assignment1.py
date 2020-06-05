#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.define a dictionary named population that contains data

dict={'shanghai':17.8,'Isatnbul':13.3,'karachi':13.0,'Munmbai':12.5}


# In[2]:


dict


# In[ ]:





# In[3]:


# 2.consider below dictionary
animals={'dogs':[20,10,15,8,32,15],'cats':[3,4,2,8,2,4],'rabbits':[2,3,3],'fish':[0.3,0.5,0.8,0.3,1]}


# In[14]:


#find resulof the following
animals


# In[5]:


animals['dogs']


# In[6]:


animals['dogs'][3]


# In[11]:


animals[3]


# In[13]:


animals['fish']


# In[ ]:





# In[15]:


# 3.what is output of the following

a=[1,2,2,3,3,3,4,4,4,4]


# In[16]:


b=set(a)


# In[19]:


print(len(a)-len(b))   #set(a)=4
                        #len(a)=10
                        #len(b)=4


# In[20]:


print(len(a)-len(b))


# In[22]:


# 4.what is output of the following?

tuple_a=3,4
tuple_b=(3,4)
print(tuple_a==tuple_b)
print(tuple_a[1])


# In[23]:


# 5.what is output of the following?

names=["Carol","Albert","Ben","Donna"]
print("&".join(sorted(names)))


# In[ ]:




