#!/usr/bin/env python
# coding: utf-8

# In[6]:


#กำหนดให้ lst = [5, 2, 1, 3, 2] จงเขียนฟังก์ชั่น Reduce เพื่อหาผลลัพท์สุดท้ายของดำเนินการแบบเลขยกกำลัง 
from functools import reduce
lst = [5, 2, 1, 3, 2]
ans1 = reduce(lambda x,y: x**y, lst)
print(ans1)


# In[7]:


#กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียนฟังก์ชั่น Reduce เพื่อหาผลลัพท์สุดท้ายของดำเนินการแบบการคูณ
from functools import reduce
lst = [1,2,3,4,5,6,7,8,9,10] 
ans2 = reduce((lambda x, y: x*y), lst)
print(ans2)


# In[ ]:




