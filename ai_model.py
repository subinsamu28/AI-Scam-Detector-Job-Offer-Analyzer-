from transformers import pipeline

# This will download and cache the BART MNLI model if not already present.
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_text(text):
    candidate_labels = [
        "Legitimate Job Offer",
        "Phishing/Scam Email",
        "Spam/Promotional Content"
    ]
    result = classifier(text, candidate_labels, multi_label=True)
    # Get the main label and confidence
    top_label = result["labels"][0]
    top_score = result["scores"][0]
    # Dict of all scores
    label_scores = dict(zip(result["labels"], result["scores"]))
    return {
        "label": top_label,
        "score": top_score,
        "scores": label_scores
    }
