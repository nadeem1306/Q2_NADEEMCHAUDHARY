#!/usr/bin/env python
# coding: utf-8

# In[3]:


str1="EduCatiON";  
newStr = "";  
   
for i in range(0, len(str1)):  
     
    if str1[i].islower():  
         
        newStr += str1[i].upper();  
     
    elif str1[i].isupper():  
         
        newStr += str1[i].lower();  
      
    else:  
        newStr += str1[i];          
print("String after case conversion : " +  newStr);  


# In[ ]:




