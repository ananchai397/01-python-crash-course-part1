#!/usr/bin/env python
# coding: utf-8

# In[21]:


#สร้างลิสต์ระบุชื่อ นามสกุล อายุ ตัวเอง
lst = ['ananchai' , 'intho' , 25]
print(lst)


# In[22]:


#ลบอายุออกจากลิสต์
del lst[2]
print(lst)


# In[23]:


#ลบอายุของตัวเอง 10 ปี และแทรกไว้หน้าสุดของลิสต์
lst.insert(0,15)
print(lst)


# In[24]:


#เพิ่มส่วนสูง น้ำหนักลงในลิส์ โดยไปต่อท้าย
lst.append(175)
lst.append(75)
print(lst)


# In[25]:


#ปริ้นสมาชิกตัวที่ 3 ถึงตัวสุดท้าย
print(lst[2: ])


# In[ ]:




