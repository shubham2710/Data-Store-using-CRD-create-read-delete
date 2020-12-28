#!/usr/bin/env python
# coding: utf-8

# In[47]:


# importing the main file("code" is the name of the file I have used) as a library 
import main as x


# # CREATION 

# In[21]:


# to create a key with key_name,value given and with no time-to-live property
x.create('Delhi',1)


# In[22]:


x.create('Gurgoan',2)


# In[35]:


x.create('Noida',3)


# # CREATION with TIME

# In[24]:


# to create a key with key_name,value given and with time-to-live property value given(number of seconds)
x.create('Goa',4,3600)


# In[25]:


x.create('Mumbai',5,10)


# In[ ]:


# it returns the value of the respective key in Jasonobject format 'key_name:value'


# In[26]:


x.read('Delhi')


# In[27]:


x.read('Gurgoan')


# In[28]:


x.read('Goa')


# # KEY - ERROR 

# In[30]:


#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it
x.create("Delhi",1)


# In[31]:


x.create("Goa",50)


# In[ ]:





# # DELETION

# In[32]:


# it deletes the respective key and its value from the database(memory is also freed)
x.delete('Goa')


# In[39]:


x.read('Goa')


# In[ ]:





# # Modify

# In[40]:


x.read('Delhi')


# In[41]:


x.modify("Delhi",10)


# In[42]:


x.read('Delhi')
# it replaces the initial value of the respective key with new value 


# In[ ]:





# In[44]:


from threading import Thread


# In[ ]:


# we can access these using multiple threads like
t1=Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn


# In[46]:


#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB


# In[ ]:





# In[ ]:




