import streamlit as st
import re
import time

# Assume supporting modules exist for complex operations (AI model, etc.)
from ai_model import classify_text  # zero-shot classification model
from rules import red_flag_rules, evaluate_text    # list or dict of regex patterns for heuristic flags
from similarity import compute_similarity  # function to compute similarity score and roles
from grammar import grammar_check   # function to get grammar score and issues
from ner import get_entities        # function to extract named entities (ORG, PERSON)
from verification import check_email_domain, check_link  # functions to verify domains and links

# ---- Page Configuration ----
st.set_page_config(
    page_title="AI Scam Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling for dark theme and custom elements
st.markdown("""
<style>
    /* Overall app background and text */
    .stApp {
        background-color: #111 !important;
        color: #EEE !important;
    }
    /* Hide Streamlit footer and hamburger menu */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    /* Headers colors (override if needed) */
    h1, h2, h3, h4, h5, h6 {
        color: #FFF !important;
        font-family: "Segoe UI", sans-serif;
    }
    /* Style for analysis result card containers */
    .analysis-card {
        background-color: #222; 
        padding: 1rem 1.5rem; 
        border-radius: 0.5rem; 
        border: 1px solid #444;
        margin-bottom: 1.5rem;
    }
    .analysis-card h4 {
        margin: 0 0 0.5rem 0;
    }
    /* Highlight for red-flagged text */
    .red-highlight {
        background-color: #ff4d4d; 
        color: #fff;
        padding: 0 4px;
        border-radius: 3px;
    }
    /* Customize st.metric cards for dark theme */
    div[data-testid="metric-container"] {
        background: #222 !important;
        border: 1px solid #444 !important;
        padding: 1rem !important;
        border-radius: 0.5rem !important;
    }
    div[data-testid="metric-container"] > label, div[data-testid="metric-container"] > div {
        color: #FFF !important;
    }
</style>
""", unsafe_allow_html=True)

# ---- Title and Instructions ----
st.title("🔎 AI Scam Detector – Job Offer Analyzer")
st.write("Paste the content of a job offer email or message below, and click **Analyze**. The app will run a multi-step AI detection pipeline to assess if the offer is likely **legitimate** or a **scam**, highlighting key findings for you.")

# ---- Text Input ----
user_input = st.text_area("Job Offer / Email Content:", height=200, placeholder="Enter the email text here...")

# Only proceed if there's input and user clicks the analyze button
if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter the text of the job offer or email to analyze.")
    else:
        # Run the multi-layer analysis pipeline with spinners for each stage
        # 1. Rule-based heuristic analysis
        with st.spinner("Scanning for red flags..."):
            flags_found = []
            highlighted_text = user_input
            for rule, pattern in red_flag_rules.items():
                # Assume red_flag_rules is a dict of {"rule_name": regex_pattern}
                if re.search(pattern, user_input, flags=re.IGNORECASE):
                    flags_found.append(rule)
                    # highlight the matching part in the text
                    highlighted_text = re.sub(pattern, 
                                               lambda m: f"<span class='red-highlight'>{m.group(0)}</span>", 
                                               highlighted_text, flags=re.IGNORECASE)
            time.sleep(0.2)  # slight pause for spinner visualization
        
        # 2. AI zero-shot classification
        with st.spinner("Running AI content classification..."):
            # This function returns a dict, e.g. {"label": "Legitimate Job Offer", "score": 0.805, "scores": {"Legitimate Job Offer":0.805, "Phishing/Scam Email":0.060, "Spam":0.135}}
            clf_result = classify_text(user_input)  
            ai_label = clf_result.get("label", "Unknown")
            ai_confidence = clf_result.get("score", 0.0)
            # Prepare other label scores for display
            other_labels = {lbl: sc for lbl, sc in clf_result.get("scores", {}).items() if lbl != ai_label}
            time.sleep(0.2)
        
        # 3. Link and email domain checks
        with st.spinner("Verifying email domains and links..."):
            email_warnings = []
            link_warnings = []
            # Check all email addresses in text
            emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', user_input)
            for email in set(emails):
                issue = check_email_domain(email)  # e.g. returns warning string if domain is free or suspicious, else None
                if issue:
                    email_warnings.append(f"**Email:** {email} – {issue}")
            # Check all URLs in text
            urls = re.findall(r'(https?://\S+)', user_input)
            for url in set(urls):
                issue = check_link(url)  # returns warning string if link is suspicious, else None
                if issue:
                    link_warnings.append(f"**Link:** {url} – {issue}")
            time.sleep(0.2)
        
        # 4. Named entity recognition for org/person
        with st.spinner("Extracting entities for consistency check..."):
            entities = get_entities(user_input)  # e.g. {"ORG": ["Acme Corporation"], "PERSON": ["John Doe"]}
            mismatch_warnings = []
            # If an ORG is mentioned and an email warning exists about a different domain, flag it
            if entities.get("ORG"):
                for org in entities["ORG"]:
                    # simple check: does org name appear in any email domain?
                    org_name = org.lower().replace(",", "")
                    match_found = any(org_name in email.split("@")[1].lower() for email in emails)
                    if not match_found and emails:
                        mismatch_warnings.append(f"Organization **{org}** is mentioned, but sender's email domain doesn’t match **{org}**.")
            # (Additional logic could compare person names to email username, etc.)
            time.sleep(0.1)
        
        # 5. Grammar and spelling analysis
        with st.spinner("Analyzing grammar and writing quality..."):
            grammar_score, issues = grammar_check(user_input)  # returns a score (0-100) and count of issues or list of issues
            if isinstance(issues, list):
                issue_count = len(issues)
            else:
                issue_count = issues  # assume it's a count if not list
            time.sleep(0.1)
        
        # 6. Structural similarity to real job offers
        with st.spinner("Comparing with real job offer patterns..."):
            similarity_pct, matched_roles = compute_similarity(user_input)  # returns similarity percentage and list of role titles
            time.sleep(0.1)
        
        score = 0
        reasons = []

        if flags_found: 
            score += min(15, 5 * len(flags_found))  # Cap flag penalty at 15
            for flag in flags_found:
                reasons.append(f"Red flag: {flag}")

        if email_warnings:
            score += min(10, 5 * len(email_warnings))  # Cap at 10
            for warn in email_warnings:
                reasons.append(f"Email warning: {warn}")

        if link_warnings:
            score += min(10, 5 * len(link_warnings))  # Cap at 10
            for warn in link_warnings:
                reasons.append(f"Link warning: {warn}")

        if mismatch_warnings:
            score += 5
            for warn in mismatch_warnings:
                reasons.append(f"Entity mismatch: {warn}")

        scam_confidence = clf_result["scores"].get("Phishing/Scam Email", 0)
        score += int(scam_confidence * 60)  # Cap AI model effect at 60

        if grammar_score < 60:
            score += 5  # Small penalty

        if similarity_pct < 20:
            score += 10  # Only if really low

        final_score = min(100, max(0, score))
        if final_score >= 60:
            verdict = "Likely Scam"
        elif final_score >= 40:
            verdict = "Suspicious"
        else:
            verdict = "Likely Legitimate"


        # ---- Display Results ----
        st.markdown("## 🛡️ Scam Analysis Summary", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"<div style='font-size:3em;font-weight:bold;color:#ff4444;'>{final_score:.0f} %</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:1.1em;color:#BBB;'>Scam Score</div>", unsafe_allow_html=True)
        with col2:
            verdict_icon = "🚩" if verdict == "Likely Scam" else "⚠️" if verdict == "Suspicious" else "✅"
            verdict_color = "#ff4444" if verdict == "Likely Scam" else "#ffa726" if verdict == "Suspicious" else "#36e458"
            st.markdown(f"<div style='font-size:2.5em;'>{verdict_icon} <span style='color:{verdict_color};font-weight:900'>{verdict}</span></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:1.1em;color:#BBB;'>Verdict</div>", unsafe_allow_html=True)
        
        # Rule-Based Analysis Section
        st.subheader("🔍 Rule-Based Heuristic Analysis")
        if flags_found:
            st.markdown(f"<b>Red Flags Detected:</b> <span style='color:#ff4d4d;font-size:1.2em;font-weight:700'>{len(flags_found)}</span>", unsafe_allow_html=True)
            # Display highlighted input text
            st.markdown(f"<div style='margin:1rem 0 1rem 0'>{highlighted_text}</div>", unsafe_allow_html=True)
            flagged_list = "".join([f"<li style='margin-bottom:0.25em'>{flag}</li>" for flag in flags_found])
            st.markdown(f"""<ul style="color:#ffb347;font-size:1.08em;font-weight:500;">{flagged_list}</ul>""", unsafe_allow_html=True)
        else:
            st.markdown("<b>Red Flags Detected:</b> <span style='color:#4ded30;font-size:1.1em'>0 (No obvious heuristic red flags found)</span>", unsafe_allow_html=True)

        # Zero-Shot Classification Section
        st.subheader("🤖 Zero-Shot NLP Classification")
        verdict_text = "Likely Scam" if ai_label.lower() != "legitimate job offer" and verdict == "Likely Scam" else "Likely Legitimate"
        card_color = "#ff4d4d" if verdict_text == "Likely Scam" else "#4ded30"
        verdict_icon = "🚩" if verdict_text == "Likely Scam" else "✅"

        st.markdown(f"""
        <div class="analysis-card" style="background: linear-gradient(90deg, #191724 80%, #19172400); border: 1.5px solid {card_color}; box-shadow:0 4px 24px 0 #0006; margin-bottom:2.3rem;">
            <div style="display: flex; align-items: center; gap: 1.2rem;">
                <span style="font-size:2.3em; flex-shrink:0; animation: verdict-pop 0.5s cubic-bezier(.6,1.8,.25,1.2);">{verdict_icon}</span>
                <div>
                    <div style="font-size:1.35em; font-weight:800; letter-spacing:0.5px; color:{card_color}">{verdict_text}</div>
                    <div style="color:#c7c7c7;font-size:1.05em;margin-top:.45em;">
                        <b>Raw Model:</b> <span style="color:#fff">{ai_label}</span> <span style="color:#888;">({ai_confidence*100:.1f}% confidence)</span>
                    </div>
                    <div style="color:#b0b0b0; font-size:.98em;">
                        <b>Other labels:</b> {" , ".join([f"{lbl} ({prob*100:.1f}%)" for lbl, prob in other_labels.items()]) or "None"}
                    </div>
                </div>
            </div>
        </div>
        <style>
        @keyframes verdict-pop {{
            0% {{ transform: scale(0.4) rotate(-12deg); opacity: 0;}}
            65% {{ transform: scale(1.12) rotate(4deg); opacity: 1;}}
            100% {{ transform: scale(1) rotate(0deg);}}
        }}
        </style>
        """, unsafe_allow_html=True)

        # Link & Domain Verification Section
        st.subheader("🔗 Link & Domain Verification")
        if email_warnings or link_warnings:
            for warn in email_warnings:
                st.write("⚠️ " + warn)
            for warn in link_warnings:
                st.write("⚠️ " + warn)
        else:
            st.write("✅ No suspicious email domains or links detected.")
        
        # Entity Mismatch Section
        st.subheader("🏢 Entity Consistency Check")
        if mismatch_warnings:
            for warn in mismatch_warnings:
                st.write("⚠️ " + warn)
        else:
            st.write("✅ No obvious organization/email mismatches found.")
        
        # Grammar Quality Section
        st.subheader("✍️ Grammar & Writing Quality")
        grade = "Good" if grammar_score > 80 else "Fair" if grammar_score > 50 else "Poor"
        st.write(f"**Writing Quality:** {grade} (Grammar score: {grammar_score:.0f}%, Issues detected: {issue_count})")
        if grade != "Good" and issue_count:
            st.write("*Note: Scam emails often contain spelling or grammar mistakes, which is a potential warning sign.*")
        
        # Structural Similarity Section
        st.subheader("📄 Structural Similarity to Real Job Offers")
        col_sim, col_role = st.columns([1, 2])
        with col_sim:
            st.metric(label="Similarity Score", value=f"{similarity_pct:.0f} %")
        with col_role:
            # Defensive: Only join if matched_roles is a list/tuple and not empty
            if matched_roles and isinstance(matched_roles, (list, tuple)) and len(matched_roles) > 0:
                st.write(f"**Possible Matched Job Role(s):** {', '.join(map(str, matched_roles))}")
            else:
                st.write("**Possible Matched Job Role(s):** Not clearly identified")

        st.caption("*(Similarity indicates how closely the message resembles a typical job offer. Low similarity or no clear role may suggest an unusual/scam message.)*")
