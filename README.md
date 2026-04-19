# 🛡️ PhishGuard — Cybersecurity Awareness Platform

> An interactive web platform for training cybersecurity threat detection skills.  
> Built with Python (Flask) · JavaScript · HTML5/CSS3

![PhishGuard](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?style=flat-square&logo=flask)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010%20Aligned-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## Overview

PhishGuard is a full-stack cybersecurity awareness platform designed to help users recognize and respond to real-world cyber threats. Built around OWASP Top 10 principles, it offers four interactive training modules backed by a Python REST API.

## Features

### 📧 Email Phishing Simulator
- Analyze real-vs-fake email scenarios crafted from real attack patterns
- Identify domain spoofing, urgency tactics, and social engineering
- Instant feedback with detailed red flag breakdowns
- Session scoring with analyst badge system

### 🧠 Adaptive Quiz Engine
- Three difficulty levels: Easy / Medium / Hard
- Topics: OWASP Top 10, attack techniques, incident response, secure coding
- Immediate explanations for every answer
- Performance scoring and badge awards

### 🗂️ Threat Intelligence Encyclopedia
- 8 detailed attack profiles: Phishing, Spear Phishing, Ransomware, MitM, SQLi, XSS, Credential Stuffing, Vishing
- Full attack kill chains, real-world incident examples, prevention techniques
- OWASP Top 10 cross-referencing
- Filterable by category and severity

### 📊 Threat Dashboard
- Global breach statistics and visualizations
- Attack vector distribution (animated bar + donut charts)
- Monthly breach trend line chart
- Industry sector risk index
- Live threat intelligence ticker
- Analyst terminal with threat summary

---

## Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Backend    | Python 3.10+, Flask |
| Frontend   | Vanilla JS, HTML5, CSS3 |
| Data       | JSON (easily swappable to DB) |
| Fonts      | Space Mono, Syne (Google Fonts) |
| Charts     | Custom SVG (no dependencies) |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Sedefehmdl/phishguard.git
cd phishguard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open [http://localhost:5000](http://localhost:5000)

---

## Project Structure

```
phishguard/
├── app.py                  # Flask application & API routes
├── requirements.txt
├── data/
│   ├── emails.json         # Email simulation scenarios
│   ├── threats.json        # Threat encyclopedia entries
│   ├── quiz.json           # Quiz questions (3 difficulty levels)
│   └── stats.json          # Dashboard statistics
├── templates/
│   ├── base.html           # Base layout with nav
│   ├── index.html          # Landing page
│   ├── simulator.html      # Email phishing simulator
│   ├── quiz.html           # Adaptive quiz engine
│   ├── threats.html        # Threat intelligence browser
│   └── dashboard.html      # Analytics dashboard
└── static/
    ├── css/main.css        # Design system & component styles
    └── js/main.js          # Shared utilities
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/emails` | Get email batch (`?mode=mixed&count=6`) |
| POST | `/api/check_email` | Submit phishing verdict |
| GET | `/api/quiz` | Get quiz questions (`?difficulty=medium`) |
| POST | `/api/quiz/answer` | Submit quiz answer |
| GET | `/api/threats` | Get threat list (`?category=...`) |
| GET | `/api/stats` | Get dashboard statistics |
| POST | `/api/score` | Calculate badge from score |

---

## Security Concepts Covered

- **OWASP A01** — Broken Access Control
- **OWASP A02** — Cryptographic Failures (MitM)
- **OWASP A03** — Injection (SQLi, XSS)
- **OWASP A07** — Authentication Failures (Credential Stuffing, Phishing)
- **OWASP A08** — Software Integrity Failures (Ransomware)
- Social Engineering: Phishing, Spear Phishing, Vishing, Smishing
- Business Email Compromise (BEC) / Whaling

---

## Author

**Sadaf Ahmadli**  
MSc Cybersecurity — Eötvös Loránd University (ELTE), Budapest  
TryHackMe Top 8% Globally  

[LinkedIn](https://linkedin.com/in/sadaf-ahmadli) · [GitHub](https://github.com/Sedefehmdl)

---

*Built for educational purposes. All threat data is curated from public cybersecurity reports.*
