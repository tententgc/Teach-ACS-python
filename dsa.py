#!/usr/bin/env python
# coding: utf-8

# In[1]:


inputStr = str(input())
result = []
firstLine, secondLine, thirdLine = [], [], []
for i in range(1, len(inputStr) + 1):
    if(i % 3 == 0):
        firstLine.append('.*.')
        secondLine.append('*.*')
        thirdLine.append('*.' + inputStr[i - 1])
    else:
        firstLine.append('.#.')
        secondLine.append('#.#')
        if(i % 3 == 1 and i != 1):
            thirdLine.append('*.' + inputStr[i - 1])
        else:
            thirdLine.append('#.' + inputStr[i - 1])
    
result.append('.' + '.'.join(firstLine) + '.')
result.append('.' + '.'.join(secondLine) + '.')
if(len(inputStr) % 3 == 0):
    thirdLine.append('*')
else:
    thirdLine.append('#')
result.append('.'.join(thirdLine))
result.append('.' + '.'.join(secondLine) + '.')
result.append('.' + '.'.join(firstLine) + '.')
print('\n'.join(result))


# In[ ]:




