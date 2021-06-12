#!/usr/bin/env python
# coding: utf-8

# In[35]:


def hanoi (n,a,b,c): #3 A B C
    if n==0 :
        return
    hanoi(n-1,a,c,b) #A  C B
    print("ย้าย = ",n ," จาก = ",a ," ไป = ",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")


# In[6]:


a,b,c,d=10,23,40,50

if a%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if b%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if c%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if d%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")


# In[ ]:




