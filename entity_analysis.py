import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    orgs = set()
    persons = set()
    titles = set()

    for ent in doc.ents:
        if ent.label_ == "ORG":
            orgs.add(ent.text)
        elif ent.label_ == "PERSON":
            persons.add(ent.text)
        elif ent.label_ == "JOB_TITLE" or "Engineer" in ent.text or "Manager" in ent.text:
            titles.add(ent.text)

    return {
        "organizations": list(orgs),
        "people": list(persons),
        "titles": list(titles)
    }

def analyze_entities(text, extracted_emails):
    report = []
    entities = extract_entities(text)
    orgs = entities["organizations"]
    emails = extracted_emails or []
    seen_pairs = set()

    if orgs:
        for org in orgs:
            for email in emails:
                domain = email.split("@")[1]
                pair = (org.lower().strip(), domain.lower().strip())
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)

                if org.lower() not in domain.lower():
                    report.append(f"🚩 Organization '{org}' does not match domain '{domain}'")
    else:
        report.append("⚠️ No organization name found in message.")

    return report
