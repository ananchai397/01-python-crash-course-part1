#!/usr/bin/env python
# coding: utf-8

# In[3]:


#a=[[[1,3],[3,4]],[5,[5,6],[7,8]]] แล้ว a[1][1][1] คือค่าใด
a=[[[1,3],[3,4]],[5,[5,6],[7,8]]]
print a[1][1][1] 


# In[9]:


#เขียนชื่อนามสกุลอายุอยู่ในลิสต์เดียวกันของคน 4 คนแล้วใส่ไว้ในลิสต์ (์Nested List) และแสดงผล
mai = ["maiyarap","mai",24]
TJ = ["Urboy","TJ",26]
joey = ["Jo","Joey",39]
KH = ["khun","KH",37]
people = [mai,TJ,joey,KH]
print(people)


# In[10]:


#ลบคนสุดท้ายของลิสต์นั้นออกและแสดงผล
del people[3]
print(people)


# In[15]:


#เพิ่มคนที่5เข้ามาเป็นคนแรกของ Nested List และแสดงผล
PMC = ["Pujan","PMC",37]
people.insert(0,PMC)
print(people)


# In[16]:


#แก้ไขอายุคนที่สอง +10 และแสดงผล
TJ[2] = 36
print(people)


# In[ ]:




