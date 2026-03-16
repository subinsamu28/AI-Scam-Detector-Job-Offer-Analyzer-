# AI Scam Detector – Job Offer Analyzer 
AI-powered scam detection system that analyzes job offer emails through six analysis layers — transformer classification, NER, semantic similarity, rule-based scanning, grammar analysis, and domain verification — delivering explainable risk scores via a Streamlit dashboard.


<h1 align="center">🔎 <strong>AI Scam Detector – Job Offer Analyzer</strong> 🛡️</h1>
<p align="center"><em>⚡ Multi-layered AI pipeline that analyzes job offers and catches scams in real-time.</em></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build: Passing">
  <img src="https://img.shields.io/badge/Contributors-1-orange?style=for-the-badge" alt="Contributors: 1">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10">
  <img src="https://img.shields.io/badge/Version-1.0-blueviolet?style=for-the-badge" alt="Version 1.0">
</p>

## 📸 Visual Overview

*Below is a quick look at the AI Scam Detector in action, analyzing a sample job offer email and highlighting key results:*  

<!-- Screenshot/GIF showcasing the UI -->
<p align="center">
  <img width="2559" height="1368" alt="image" src="https://github.com/user-attachments/assets/4e6e2ca4-a723-4d06-a8ee-0d8aba4aec08" />
  <img width="2460" height="902" alt="image" src="https://github.com/user-attachments/assets/f23b8a68-3c74-4c01-87c1-d2841573c716" />
  <img width="2472" height="1189" alt="image" src="https://github.com/user-attachments/assets/bb800e0f-a7cb-4384-868b-bfabd83aedad" />
</p>

## 📦 Installation and Setup

**Requirements:** Python 3.10+ and pip. Compatible with **Windows** 🪟, **Mac** 🍎, and **Linux** 🐧.

**Get Started:**

1. **Download or Clone:** Get the latest code:
   - 📥 **[Download ZIP](https://github.com/subinsamu28/job-offer-email-scam-detector/archive/refs/heads/main.zip)** or `git clone https://github.com/yourusername/AI-Scam-Detector.git`
2. **Python Setup:** Make sure Python 3.10+ is installed on your system.
3. **Virtual Environment (Optional):** Create and activate a virtual environment for the project:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate   # Windows
   ```
4. **Install Dependencies:** Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   > 🚨 **Note:** After installing, download the spaCy English model:
   > ```bash
   > python -m spacy download en_core_web_sm
   > ```
5. **Run the Application:** Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   After a few moments, Streamlit will open the app in your web browser.  
   - ✅ **Access the UI:** Go to [http://localhost:8501](http://localhost:8501) to view the dashboard.

## 🛠️ Usage Guide

Once the app is running, enter the text of a job offer email or message and click **Analyze**. The AI Scam Detector will evaluate the content through multiple steps and display a detailed report.

You can test the app with different scenarios. Below are two examples (click to expand):

<details>
<summary><strong>✔️ Legitimate Job Offer Example</strong> (click to expand)</summary>

**Input:** (excerpt from a real offer email)  
```text
Dear Jane Doe,

Thank you for applying to ABC Corp. We are pleased to offer you an interview for the Data Analyst position. This is a full-time role based in our New York office with a salary range of $70,000 - $80,000 per year.

Please let us know a suitable time for a virtual interview. You can also find more information about our company on our website (www.abccorp.com).

Sincerely,
John Smith  
HR Manager, ABC Corp  
john.smith@abccorp.com
```

**Analysis Outcome:**  
- ✅ *No obvious red flags* (content and sender look legitimate)  
- ✅ *AI Classification:* **Legitimate Job Offer** (approx. 90% confidence)  
- ✅ *Email domain* **abccorp.com** verified as company domain  
- ✅ *Grammar & writing* are professional  
- ✅ *Message structure* aligns with typical job offers (high similarity score)

</details>

<details>
<summary><strong>🚩 Scam Job Offer Example</strong> (click to expand)</summary>

**Input:** (excerpt from a suspected scam email)  
```text
Dear Candidate,

We are urgently looking to fill a data entry position and need your response within 24 hours. As a welcome gesture, we offer an upfront payment of $500 as a sign-on bonus, which you will receive immediately after you start.

Please send your bank account details and a copy of your ID card for verification. The interview will be conducted via Google Hangouts chat.

Sincerely,  
John Doe  
Recruitment Team  
johnrecruiter@gmail.com
```

**Analysis Outcome:**  
- 🚩 *Multiple red flags detected* (e.g. **Urgency**, **Upfront Payment**, **Sensitive info request**)  
- 🚩 *AI Classification:* **Likely Scam** (high confidence)  
- ⚠️ *Email domain* **gmail.com** is a free personal email (not an official company domain)  
- ⚠️ *Grammar & writing* appear somewhat suspicious (informal tone)  
- ⚠️ *Message structure* is unusual for a real offer (low similarity to typical offers)

</details>

## 🗃️ File Structure and Contents

<details>
<summary><strong>Project Structure</strong> (click to expand)</summary>

```bash
AI-Scam-Detector/
├── app.py             # Streamlit app UI for the scam detector 🖥️
├── ai_model.py        # AI model integration for text classification 🤖
├── rules.py           # Regex-based red flag rules (e.g. urgency, payment) 🚩
├── similarity.py      # Similarity scoring against known job offer templates 🔍
├── ner.py             # Named Entity Recognition (extracts ORG, PERSON) 🕵️
├── grammar.py         # Grammar and spelling checker integration 📝
├── verification.py    # Email domain & link verification logic 🔗
├── entity_analysis.py # (Alternate entity extraction logic using spaCy) 🕵️
├── link_analysis.py   # (Legacy link analysis module) 🔗
├── verdict.py         # Final verdict aggregation (scores & decision) 📊
├── examples/          # Sample email texts for testing 📂
│   ├── real1.txt      # Example of a legitimate job offer email 📄
│   └── scam1.txt      # Example of a scam job offer email 📄
├── requirements.txt   # Python dependencies for the project 📦
└── venv/              # (Optional) Pre-configured virtual environment ⚙️
```

</details>

## 🌐 Advanced Features & Tech Stack

This project combines several AI and rule-based techniques to detect scam offers:

- 🤖 **AI-Powered Classification:** Uses a pre-trained *Hugging Face Transformers* model for zero-shot text classification, distinguishing legitimate offers from scams.
- 🚩 **Rule-Based Scanning:** Applies custom regex rules to flag phrases indicating urgency, upfront payments, requests for sensitive info, and other common scam signals.
- 🕵️ **Entity Consistency Checks:** Extracts entities (organizations, people) with **spaCy** and cross-verifies them against email domains (catching mismatches between claimed company names and sender addresses).
- 🔗 **Link & Domain Verification:** Detects suspicious URLs or free email domains (e.g., Gmail, Yahoo) using heuristic checks to warn about unofficial contact points.
- 📝 **Grammar & Writing Analysis:** Leverages **LanguageTool** to evaluate grammar and spelling; many scam emails contain noticeable errors or unusual phrasing.
- 📊 **Structural Similarity:** Compares the email's structure to real job offers using **SentenceTransformers** embeddings, indicating how closely the message resembles a typical legitimate offer.
- 🖥️ **Streamlit Web App:** Provides an interactive dashboard to input email text and review analysis results, with clear highlighting and scoring for each detection layer.

## 🤝 Contribution Guidelines

Contributions are welcome! Whether it's bug fixes, new features, or improving documentation, we'd love your help.

**To contribute:**
- ⭐ **Fork** the repository and create a new branch for your feature or bugfix.
- 🔧 **Make your changes** with clear, well-documented code and comments.
- ✅ **Test** your improvements to ensure no existing functionality breaks.
- 🔃 **Submit a Pull Request** with a clear description of your changes and the problem it solves.

Please make sure to follow the project's coding style and conventions. By contributing, you agree that your contributions will be licensed under the same MIT License.

Found an issue or have a suggestion? Feel free to **open an issue** 🐞 on GitHub. Your feedback is valuable!

## 📝 License

This project is released under the **MIT License** © 2025. See the [LICENSE](LICENSE) file for details. 🖋️

## 📬 Contact and Support

For any questions or support, please reach out or join our community:

[![Email](https://img.shields.io/badge/Email-contact%40example.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:subinsamu28@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/subin-samu/)
[![GitHub](https://img.shields.io/badge/GitHub-Project-181717?style=flat&logo=github)](https://github.com/subinsamu28/job-offer-email-scam-detector.git)


## 🎉 Acknowledgments & Credits

A huge thank you to the open-source community and libraries that power this project:  
**Hugging Face** 🤗, **spaCy**, **Streamlit**, **LanguageTool**, and **SentenceTransformers**. Their excellent tools and models made this app possible.

Special thanks to everyone who has contributed, tested, or provided feedback for **AI Scam Detector**. Your support helps make the job hunting world a little safer! 🌟

