# 🎬 IMDb Sentiment Analyzer

AI 기반 감정 분석기로, 사용자가 입력한 영화 리뷰가 긍정적인지 부정적인지 분석해주는 웹 애플리케이션입니다.  
Flask로 구성된 AI 서버, Spring Boot 백엔드, 순수 HTML 프론트엔드가 연동되어 있습니다.

---

## 📌 주요 기능

- 사용자 리뷰에 대한 **감정 분석 (긍정/부정)**
- 분석 결과에 따라 **이모지 출력 (😊 / 😞)**
- Flask + Scikit-learn 모델을 사용한 AI 서버
- Spring Boot 백엔드 서버에서 Flask API 호출 및 결과 전달
- 순수 HTML + JS 기반의 간단한 UI

---

## 🔁 작동 흐름

1. 사용자가 **HTML 페이지에서 리뷰 입력**
2. JavaScript가 `/analyze` (Spring 서버)로 **POST 요청 전송**
3. Spring 서버가 Flask 서버 (`localhost:5000/classify`)에 **리뷰 전송**
4. Flask 서버가 Scikit-learn 모델로 **감정 분석 수행**
5. 분석 결과 (`sentiment`, `emoji`)를 Spring 서버로 전송
6. 결과가 HTML에 **표시됨**

---

## 📦 기술 스택

| 파트        | 기술 |
|-------------|------|
| AI 서버     | Python 3, Flask, Scikit-learn |
| 백엔드 API  | Java 17, Spring Boot |
| 프론트엔드  | HTML, JavaScript |
| 통신 방식   | REST API, JSON |

