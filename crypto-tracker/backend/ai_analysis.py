from transformers import pipeline

def analyze_sentiment(texts: list):
    model = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")
    return [model(text) for text in texts]