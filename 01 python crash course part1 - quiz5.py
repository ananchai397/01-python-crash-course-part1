#!/usr/bin/env python
# coding: utf-8

# In[6]:


#กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียน Map เพื่อหาเลขยกกำลังสามทั้งหมดของ lst ในรูปแบบ Lambda Function และ ฟังก์ชั่นธรรมดา
#mapในรูปแบบ Lambda Function
lst = [1,2,3,4,5,6,7,8,9,10] 
result = map(lambda x: x**3, lst)
print(list(result))


# In[15]:


#mapในรูปแบบฟังก์ชั่นธรรมดา
def result2(x): 
    return x**3
print(list(map(result2,lst)))


# In[16]:


#กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียน Filter เพื่อหาเลขใดในลิสต์เมื่อยกกำลังสองแล้วหารสองไม่ลงตัว ในรูปแบบ Lambda Function และ ฟังก์ชั่นธรรมดา
#Filterในรูปแบบ Lambda Function
result3 = filter(lambda a: ((a**2)%2 != 0), lst)
print(list(result3))


# In[17]:


#filterในรูปแบบฟังก์ชั่นธรรมดา
def result4(b):
    return (b**2)%2 !=0
print(list(filter(result4,lst)))


# In[ ]:




