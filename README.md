# job-offer-email-scam-detector
AI‑powered Rust &amp; WebAssembly web app that parses your PDF/DOCX resume and job description to generate 100 % ATS‑compliant Europass CVs and cover letters in real time.  


# 🛡️ Job Offer & Email Scam Detector – AI-Powered Analyzer

---

## 🚀 Project Overview  
In today’s digital world, job offer scams and phishing emails are rampant. This project provides an advanced AI-powered tool that analyzes job offer emails and messages to detect scams with precision. Leveraging zero-shot classification, heuristic rules, grammar checks, and domain verification, it delivers a comprehensive and reliable scam assessment to protect you.

---

## 🌟 Key Features  
- 🤖 **Zero-Shot AI Classification:** Uses Facebook’s `bart-large-mnli` transformer model for instant scam prediction without training data.  
- 🔍 **Heuristic Red-Flag Rules:** Regex-driven detection of common scam signals such as urgency, suspicious payment requests, and unprofessional emails.  
- 🏷️ **Named Entity Recognition (NER):** Extracts key entities (organizations, persons) to validate the message context.  
- ✍️ **Grammar & Style Analysis:** Flags unnatural language and poor grammar typical in scams.  
- 🔗 **Domain & Link Verification:** Checks email domains and embedded URLs for phishing or spoofing indicators.  
- 💻 **Streamlit Web Interface:** Sleek, dark-themed, user-friendly UI for quick analysis.  

---

## 🧰 Tech Stack  
- Python 3.10+  
- Hugging Face Transformers (`facebook/bart-large-mnli`)  
- Regex and NLP libraries (spaCy, etc.)  
- Streamlit for web app  
- Custom modules for rules, verification, and similarity scoring  

---

## ⚙️ Installation & Setup  

1. **Clone the repo:**  
```bash
git clone https://github.com/yourusername/job-offer-email-scam-detector.git
cd job-offer-email-scam-detector/AI-Scam-Detector
```

2. **Create and activate a virtual environment:**  
```bash
python3 -m venv venv
source venv/bin/activate    # Linux/macOS
.\venv\Scripts\activate   # Windows
```

3. **Install dependencies:**  
```bash
pip install -r requirements.txt
```

4. **(Optional) Configure environment variables** in `.env` if needed.

---

## 🏃 Usage  

Run the Streamlit app:  
```bash
streamlit run app.py
```

- Paste the content of a suspicious job offer or email into the input box.  
- Click **Analyze** to trigger the AI and heuristic pipeline.  
- Review detailed findings including scam likelihood, red-flag highlights, entity extraction, grammar issues, and final verdict.

---

## 🔍 How It Works  

The detection pipeline integrates multiple analysis layers:

1. **AI Classification:** Zero-shot model assigns scam likelihood among Legitimate, Scam, and Spam categories.  
2. **Heuristic Rules:** Regex patterns scan for urgent language, suspicious payment requests, unprofessional sender emails, and more.  
3. **Similarity Scoring:** Compares text with known scam templates for pattern matches.  
4. **Grammar Checking:** Identifies unusual phrasing and language mistakes typical of scams.  
5. **Named Entity Extraction:** Detects organizations and names to verify message authenticity.  
6. **Domain & Link Verification:** Validates sender email domains and embedded links for spoofing or phishing.

These layers combine to produce a confidence score and actionable feedback for users.

---

## 🧪 Examples  

Test the detector with provided samples:  
- `examples/scam1.txt` — typical scam message  
- `examples/real1.txt` — legitimate job offer  

---

## 📁 Project Structure  

```
├── app.py              # Streamlit app entrypoint  
├── ai_model.py         # AI zero-shot classification  
├── rules.py            # Regex-based heuristic rules  
├── similarity.py       # Text similarity engine  
├── grammar.py          # Grammar and style analysis  
├── ner.py              # Named entity recognition  
├── verification.py     # Email domain & link checks  
├── verdict.py          # Final decision logic  
├── examples/           # Sample texts for testing  
├── requirements.txt    # Python dependencies  
└── .env                # Optional environment configs  
```

---

## 🤝 Contribution  

Contributions, issues, and feature requests are welcome!  
1. Fork the repo  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a pull request  

---

## 📄 License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ and ⚡ AI for safer job searching.
