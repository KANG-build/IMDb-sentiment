#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import os
import numpy as np
from vectorizer import vect  # 로컬 vectorizer.py 사용

# 모델 로드
cur_dir = os.getcwd()
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))

# 분류 함수
def classify_review(review):
    label = {0: 'negative', 1: 'positive'}
    emoji_map = {'positive': '😊', 'negative': '😞'}
    
    X = vect.transform([review])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    
    sentiment = label[y]
    emoji = emoji_map[sentiment]
    confidence = round(proba * 100, 2)
    
    result = {
        'sentiment': sentiment,
        'emoji': emoji
    }
    
    return result

