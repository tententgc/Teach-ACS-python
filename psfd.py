#!/usr/bin/env python
# coding: utf-8

# In[3]:


word = input()
word_len = len(word)
def first(a):
    print('.', end='')
    for i in range(1,a+1):
        if i%3==0:
            print('.*..', end='')
        else:
            print('.#..', end='')
    print()
def second(a):
    print('.', end='')
    for i in range(1,a+1):
        if i%3==0:
            print('*.*.', end='')
        else:
            print('#.#.', end='')
    print()
def third (a,word):
    print('#', end='')
    for i in range(1,a+1):
        print('.' + '%c' % word[i-1] + '.', end='')
        if i%3==1:
            print('#', end='')
        elif i==a and a%3==2:
            print('#', end='')
        else:
            print('*', end='')
    print()
first(word_len)
second(word_len)
third(word_len,word)
second(word_len)
first(word_len)

