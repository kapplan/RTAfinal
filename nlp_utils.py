# nlp_utils.py
from transformers import pipeline

# Initialize sentiment analysis pipeline
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    """Return sentiment analysis for a single text."""
    return sentiment_classifier(text)
