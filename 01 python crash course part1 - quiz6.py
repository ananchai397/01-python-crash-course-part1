#!/usr/bin/env python
# coding: utf-8

# In[3]:


#กำหนดให้ lst = [1,2,3,4,5] จงเขียน List Comprehension เพื่อนำทุกตัวใน lst ไปคูณกับ 2 และลบด้วย 1 พร้อมกับแสดงผล
lst = [1,2,3,4,5] 
lst2 = [(item**2)-1 for item in lst]
print(lst2)


# In[9]:


#กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10,11,12,13] จงเขียน List Comprehension เพื่อหาตัวที่หาร 3 ไม่ลงตัว และนำผลลัพธ์นั้นยกกำลังสาม พร้อมกับแสดงผล
lst3 = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
lst4 = [x**3 for x in lst3 if x%3 != 0]
print(lst4)


# In[ ]:




