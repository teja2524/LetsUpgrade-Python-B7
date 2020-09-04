#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lists
lst= ["teja",10,15.3,[1,2,3]]
lst 


# In[2]:


# accessing sublist or lists
lst[ 3][0]


# In[3]:


lst.index(10)


# In[5]:


# dictionaries are unordered key value pair
dit= {"name":"teja","age":"21","number":"12345"}
dit 


# In[6]:


# retrieving the values
dit.get('name')


# In[8]:


# sets are used for storing unique values
st= {"teja","samala",1,2,3,2,4,5,1}
st 


# In[9]:


st1= {"teja",1}
st.issubset(st)


# In[11]:


# tuple is an ordered immutable sequence of objects
tup= ("teja","@","malliktejasamala")
tup 


# In[12]:


tup.index("malliktejasamala")


# In[14]:


# strings
name= "teja"
name1= "samala"
name1 


# In[15]:


#string functions
name2="mallik"
name3= "manu"
name2+ name3
 

