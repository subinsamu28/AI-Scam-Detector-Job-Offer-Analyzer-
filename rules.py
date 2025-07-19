# rules.py

# Simple example patterns, you can add more
red_flag_rules = {
    "Urgency": r"urgent|immediately|asap|24 hours|limited time",
    "Request for Sensitive Info": r"bank account|passport|driver'?s license|id card|social security",
    "Unusual Payment": r"bitcoin|gift card|crypto|western union|moneygram",
    "Unprofessional Email": r"@gmail\.com|@yahoo\.com|@hotmail\.com",
    "Upfront Payment Promise": r"initial payment|payment upfront|advance payment",
    # ...add more as you wish
}

# Function to scan text and return flags triggered
import re

def evaluate_text(text):
    score = 0
    red_flags = []
    for rule in red_flag_rules:
        if re.search(rule["pattern"], text, re.IGNORECASE):
            red_flags.append(rule["reason"])
            score += 15  # You can adjust weight per rule if you want
    score = min(score, 100)
    return score, red_flags
