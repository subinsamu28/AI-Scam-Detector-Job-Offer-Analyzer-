import re

# Example: Check if email domain is from a known free provider
def check_email_domain(email):
    free_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "protonmail.com"]
    match = re.search(r"@([\w\.-]+)", email)
    if match:
        domain = match.group(1).lower()
        if domain in free_domains:
            return False, f"🚩 Email uses free domain: {domain}"
        else:
            return True, f"✅ Email domain looks professional: {domain}"
    return False, "❓ Could not extract domain from email."

# Example: Check if a link is suspicious (very basic)
def check_link(link):
    suspicious_keywords = ["bit.ly", "tinyurl", "free", "bonus", "giveaway", "prize"]
    for kw in suspicious_keywords:
        if kw in link.lower():
            return False, f"🚩 Suspicious keyword in link: {kw}"
    if link.lower().startswith("http://") or link.lower().startswith("https://"):
        return True, "✅ Link appears to be formatted correctly."
    return False, "❓ Link does not appear valid."
