# Product Launch Feedback Dashboard

This is a **real-time product launch feedback dashboard** built with **Flask** and **Hugging Face Transformers**. It simulates reactions to a new product launch, including likes, shares, comments, and sentiment analysis.

---

## **Features**

- **Simulated real-time engagement**  
  Randomly generates likes, shares, and comments for multiple posts.

- **Sentiment analysis**  
  Uses Hugging Face `nlptown/bert-base-multilingual-uncased-sentiment` model to classify comment sentiment.

- **Interactive dashboard**  
  Visualizes:
  - Likes per post  
  - Shares per post  
  - Top positive and negative comments  

- **Synthetic data only**  
  No real social media API is required, so it works offline.

---

## **Project Structure**

RTAfinal/
├─ main.py # Flask app and backend logic
├─ nlp_utils.py # Sentiment analysis helper
└─ templates/
└─ dashboard.html # Dashboard frontend with charts

yaml
Copy code

---

## **Dependencies**

- Python 3.9+  
- Flask  
- Transformers (Hugging Face)  
- NumPy < 2  
- Chart.js (included via CDN in dashboard.html)

Install Python dependencies:

```bash
pip install flask transformers numpy==1.24.3
