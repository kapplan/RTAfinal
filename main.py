from transformers import pipeline
from flask import Flask, request, jsonify, render_template
import random
import time

# -------------------------
# Sentiment analysis setup
# -------------------------
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):
    """Analyze sentiment of a single text and return label and score."""
    return sentiment_classifier(text)[0]

# -------------------------
# Flask app
# -------------------------
app = Flask(__name__)

# In-memory storage for post metrics
posts_data = {}

# -------------------------
# synthetic posts
# -------------------------
SYNTHETIC_POSTS = [
    "I love this product!",
    "This is terrible, never buying again.",
    "Pretty good, could be better.",
    "Amazing quality and fast delivery.",
    "Not satisfied with the service.",
    "Excellent! Highly recommend it.",
    "Mediocre experience overall."
]

POST_IDS = ["post_1", "post_2", "post_3", "post_4", "post_5"]

def generate_synthetic_interactions():
    """Randomly add likes, comments, shares and analyze sentiment for comments."""
    for post_id in POST_IDS:
        if post_id not in posts_data:
            posts_data[post_id] = {"likes": 0, "comments": 0, "shares": 0, "sentiments": []}
        # Random likes, comments, shares
        posts_data[post_id]["likes"] += random.randint(0, 3)
        posts_data[post_id]["shares"] += random.randint(0, 2)
        # Random comments
        if random.random() < 0.5:
            comment = random.choice(SYNTHETIC_POSTS)
            posts_data[post_id]["comments"] += 1
            sentiment = analyze_sentiment(comment)
            posts_data[post_id]["sentiments"].append(sentiment)

# -------------------------
# API endpoints
# -------------------------
@app.route('/post_interaction', methods=['POST'])
def add_interaction():
    data = request.get_json()
    post_id = data.get("post_id")
    interaction_type = data.get("type")
    comment_text = data.get("text", "")

    if not post_id or not interaction_type:
        return jsonify({"error": "post_id and type are required"}), 400

    if post_id not in posts_data:
        posts_data[post_id] = {"likes": 0, "comments": 0, "shares": 0, "sentiments": []}

    if interaction_type == "like":
        posts_data[post_id]["likes"] += 1
    elif interaction_type == "comment":
        posts_data[post_id]["comments"] += 1
        if comment_text:
            sentiment = analyze_sentiment(comment_text)
            posts_data[post_id]["sentiments"].append(sentiment)
    elif interaction_type == "share":
        posts_data[post_id]["shares"] += 1

    return jsonify({"message": "Interaction added", "metrics": posts_data[post_id]})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    # Update synthetic data every request
    generate_synthetic_interactions()
    return jsonify(posts_data)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# -------------------------
# RUN
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
