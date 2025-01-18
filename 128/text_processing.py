#!/usr/bin/env python
# coding: utf-8

# # Text processing

# In[3]:


def remove_punc(input_text):
    punctuation_marks=['.',',','?','#','$']
    output_text=""
    for char in input_text:
        if char not in punctuation_marks:
            output_text+=char
    return output_text


# In[4]:


remove_punc('''hello!, "how are you?"''')


# In[27]:


def remove_stopwords(input_text):
    stop_words=['is','and','the','a','an','in','on']
    words=input_text.split()
    filtered_words=[]
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
            
      # join the filtered words back into a sentence      
    output_text=' '.join(filtered_words)
    return (output_text)      


# In[28]:


remove_stopwords("The movie was good and it is a hit")


# In[ ]:





# In[ ]:




