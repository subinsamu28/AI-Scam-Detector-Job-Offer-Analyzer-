import re
import tldextract
import whois

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

def extract_links(text):
    return re.findall(r'(https?://[^\s]+)', text)

def get_domain_info(domain):
    try:
        w = whois.whois(domain)
        age = (2025 - int(str(w.creation_date[0].year))) if isinstance(w.creation_date, list) else 0
        return age
    except Exception:
        return None

def analyze_links_and_emails(text):
    report = []
    emails = extract_emails(text)
    links = extract_links(text)

    if not emails:
        report.append("⚠️ No email address found.")
    for email in emails:
        if any(free in email for free in ["gmail.com", "yahoo.com", "outlook.com"]):
            report.append(f"🚩 Email uses free domain: {email}")
        else:
            domain = email.split("@")[1]
            age = get_domain_info(domain)
            if age is not None and age < 2:
                report.append(f"🚩 Email domain {domain} is less than 2 years old.")
    
    for link in links:
        domain = tldextract.extract(link).registered_domain
        if domain:
            age = get_domain_info(domain)
            if age is not None and age < 2:
                report.append(f"⚠️ Link points to a very new domain: {domain}")

    if links:
        report.append(f"🔗 Found {len(links)} link(s). Check for URL mismatches or redirects.")

    if not links:
        report.append("ℹ️ No links found.")

    return report, emails
