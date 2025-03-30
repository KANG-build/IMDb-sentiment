from flask import Flask, request, jsonify
import pickle
import os
import numpy as np
from vectorizer import vect  # 로컬 vectorizer 사용

# Flask 앱 생성
app = Flask(__name__)

# 모델 로드
cur_dir = os.getcwd()
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))

# 분류 함수
def classify(document):
    label = {0: 'negative', 1: 'positive'}
    emoji_map = {'positive': '😊', 'negative': '😞'}
    
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    
    sentiment = label[y]
    emoji = emoji_map[sentiment]
    
    return sentiment, emoji, round(proba * 100, 2)

# API 엔드포인트
@app.route('/classify', methods=['POST'])
def classify_review():
    data = request.get_json()
    
    if not data or 'review' not in data:
        return jsonify({'error': '리뷰 텍스트가 필요합니다.'}), 400

    review = data['review']
    sentiment, emoji, confidence = classify(review)

    return jsonify({
        'sentiment': sentiment,
        'emoji': emoji
    })

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)

