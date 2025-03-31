#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle


cur_dir = os.path.dirname(__file__)  # model/
stop_path = os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl')
with open(stop_path, 'rb') as f:
    stop = pickle.load(f)
    
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower())                    + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
                         preprocessor=None,
                         tokenizer=tokenizer)


# In[ ]:




