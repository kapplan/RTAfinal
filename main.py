
from transformers import pipeline

# Initialize Hugging Face sentiment analysis
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):
    """Analyze sentiment of a single text and return label and score."""
    return sentiment_classifier(text)[0]  # returns {'label':..., 'score':...}

from transformers import pipeline

# Initialize Hugging Face sentiment analysis
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):
    """Analyze sentiment of a single text and return label and score."""
    return sentiment_classifier(text)[0]  # returns {'label':..., 'score':...}


from flask import Flask, request, jsonify, render_template
from nlp_utils import analyze_sentiment

app = Flask(__name__)

# In-memory storage for post metrics
posts_data = {}

# -------------------------
# Add new interaction
# -------------------------
@app.route('/post_interaction', methods=['POST'])
def add_interaction():
    data = request.get_json()
    post_id = data.get("post_id")
    interaction_type = data.get("type")  # like, comment, share
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

# -------------------------
# Get all metrics
# -------------------------
@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(posts_data)

# -------------------------
# Dashboard page
# -------------------------
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# -------------------------
# Run app
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from nlp_utils import analyze_sentiment

app = Flask(__name__)

# In-memory storage for post metrics
posts_data = {}

# -------------------------
# Add new interaction
# -------------------------
@app.route('/post_interaction', methods=['POST'])
def add_interaction():
    data = request.get_json()
    post_id = data.get("post_id")
    interaction_type = data.get("type")  # like, comment, share
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

# -------------------------
# Get all metrics
# -------------------------
@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(posts_data)

# -------------------------
# Dashboard page
# -------------------------
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# -------------------------
# Run app
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)

