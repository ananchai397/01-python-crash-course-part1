#!/usr/bin/env python
# coding: utf-8

# In[3]:


#กำหนดให้ A = [1, 2, 3, 4, 5] และ B = [2, 3, 1, 3, 2] จงเขียน Map แบบ Multiple-list operations โดยให้ B ยกกำลังด้วย A พร้อมกับแสดงผล
A = [1, 2, 3, 4, 5] 
B = [2, 3, 1, 3, 2] 

answer = map (lambda x, y: y**x, A, B)
print(list(answer))


# In[4]:


#จงเขียนชื่อนักเรียน เลขที่ และคะแนนสอบไฟนอล พร้อมกับใช้คำสั่ง Zip() ในการจับคู่พร้อมกับแสดงผลลัพธ์ที่ถูกต้อง
name = ["dajim", "Daboyway", "joeyboy", "Jazz JSPKK", "Fhero"]
number = [1,2,3,4,5]
point = [75, 80, 69, 72, 43]

show = list(zip(name, number, point))
print(show)


# In[ ]:




