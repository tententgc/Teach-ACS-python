#!/usr/bin/env python
# coding: utf-8

# In[5]:


p=int(input("put your money :")) 
r=0.05 
print ("Year %21s " % "Amount on deposit")
for year in range (1,11):
    a = p*(1+r)**year
    print ("%4d %21.2f" %(year , a))


# In[ ]:




