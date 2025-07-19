import spacy

# Load the spaCy English NER model
nlp = spacy.load("en_core_web_sm")

def get_entities(text):
    doc = nlp(text)
    # Return ORG (organization), PERSON, and other useful entity types
    entities = {
        "ORG": [],
        "PERSON": [],
        "EMAIL": [],
        "MONEY": [],
        "GPE": [],
        "URL": [],
    }
    # Get entity texts by label
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    # SpaCy doesn’t extract emails/urls by default, so use regex as backup
    import re
    emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    urls = re.findall(r'https?://\S+', text)
    if emails:
        entities["EMAIL"].extend(emails)
    if urls:
        entities["URL"].extend(urls)
    return entities
