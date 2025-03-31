from flask import Flask, request, jsonify
import pickle
import os
import sys 
import sklearn
import sklearn.linear_model._sgd_fast
sklearn.linear_model._sgd_fast.Log = object  # Log라는 클래스가 있다고 "속이는" 코드


sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))

import numpy as np
from vectorizer import vect  # 로컬 vectorizer 사용

# Flask 앱 생성
app = Flask(__name__)

# 모델 로드
cur_dir = os.path.dirname(__file__)  # flask-api/
clf_path = os.path.join(cur_dir, 'model', 'pkl_objects', 'classifier.pkl')

clf = pickle.load(open(clf_path, 'rb'))

# 분류 함수
def classify(document):
    label = {0: 'negative', 1: 'positive'}
    emoji_map = {'positive': '😊', 'negative': '😞'}
    
    X = vect.transform([document])
    y = clf.predict(X)[0]
    
    sentiment = label[y]
    emoji = emoji_map[sentiment]
    
    return sentiment, emoji

# API 엔드포인트
@app.route('/classify', methods=['POST'])
def classify_review():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': '리뷰 텍스트가 필요합니다.'}), 400

    review = data['text']
    sentiment, emoji = classify(review)

    return jsonify({
        'sentiment': sentiment,
        'emoji': emoji
    })

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)

