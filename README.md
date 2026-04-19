# PhishGuard

**Interactive Cybersecurity Awareness Platform**

Train your instincts against phishing, social engineering, and web attacks — backed by real-world OWASP threat intelligence.

[**Live Demo**](https://phishguard-sg0a.onrender.com) &nbsp;·&nbsp; [Report Issue](https://github.com/Sedefehmdl/phishguard/issues)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![OWASP](https://img.shields.io/badge/OWASP-Top_10_Aligned-EF4444?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Live Demo

The application is deployed at **[phishguard-sg0a.onrender.com](https://phishguard-sg0a.onrender.com)**.

> Note: First visit may take ~30 seconds as the free-tier instance wakes up.

---

## About The Project

PhishGuard is a full-stack cybersecurity awareness platform built to help users recognize and defend against real-world cyber threats. The platform simulates authentic attack scenarios — from sophisticated phishing emails to OWASP Top 10 exploits — and provides interactive training backed by real breach statistics.

The project combines a Python Flask REST API with a custom-designed vanilla JavaScript frontend, featuring a dark terminal-inspired editorial aesthetic that reflects the cybersecurity operations center experience.

### Motivation

As an MSc Cybersecurity student, I wanted to build something that translates academic security theory into a hands-on tool. The goal was a project that goes beyond a standard CRUD app — one that combines full-stack development, UX design, and real educational value in the cybersecurity domain.

---

## Features

### Email Phishing Simulator
Analyze real-vs-fake email scenarios crafted from actual attack patterns. Users are presented with an inbox-style interface and must identify which emails are phishing attempts. Each decision is graded with detailed red flag analysis and trust indicators, teaching users to recognize attack techniques like domain spoofing, urgency manipulation, and social engineering.

### Adaptive Security Quiz
Test security knowledge across three difficulty tiers (Easy, Medium, Hard). Questions cover OWASP Top 10, attack techniques, incident response, and secure coding practices. Every answer includes an explanation, and final scores are translated into analyst badges — from "Learning Mode" to "Elite Analyst."

### Threat Intelligence Encyclopedia
A browsable database of 8 major attack vectors including Phishing, Spear Phishing, Ransomware, Man-in-the-Middle, SQL Injection, XSS, Credential Stuffing, and Vishing. Each entry includes the full attack kill chain, real-world incident examples (Colonial Pipeline, WannaCry, DNC hack), prevention techniques, and OWASP references.

### Threat Dashboard
A data visualization module displaying the global cybersecurity threat landscape. Built with custom SVG (no external chart libraries), it includes animated bar charts, donut charts, trend lines, an industry sector risk index, a live threat intelligence ticker, and an analyst terminal.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.10+, Flask 3.0, Gunicorn |
| Frontend | Vanilla JavaScript (ES6+), HTML5, CSS3 |
| Data Visualization | Custom SVG (no external chart libraries) |
| Typography | Space Mono, Syne (Google Fonts) |
| Data Storage | JSON (designed to be swappable to SQL/NoSQL) |
| Deployment | Render.com (EU Central region) |
| Version Control | Git, GitHub |

---

## Design Philosophy

The UI takes inspiration from Security Operations Center (SOC) dashboards merged with editorial magazine design:

- Dark terminal aesthetic with deep blacks and electric cyan accents
- Typography pairing of Space Mono (data) and Syne (headlines)
- Asymmetric layouts with intentional whitespace
- Subtle motion: scan-line effects, animated counters, glowing elements
- Every detail crafted with intentionality — no generic template aesthetic

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/Sedefehmdl/phishguard.git
cd phishguard

# Create a virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser to `http://localhost:5000`.

---

## Project Structure

```
phishguard/
├── app.py                      # Flask application & REST API
├── requirements.txt            # Python dependencies
├── README.md
├── data/
│   ├── emails.json             # Phishing simulation scenarios
│   ├── threats.json            # Threat encyclopedia entries
│   ├── quiz.json               # Quiz questions (3 difficulty tiers)
│   └── stats.json              # Dashboard statistics
├── templates/
│   ├── base.html               # Base layout with navigation
│   ├── index.html              # Landing page
│   ├── simulator.html          # Email phishing simulator
│   ├── quiz.html               # Adaptive quiz engine
│   ├── threats.html            # Threat intelligence browser
│   └── dashboard.html          # Analytics dashboard
└── static/
    ├── css/main.css            # Design system & components
    └── js/main.js              # Shared utilities
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/emails` | Retrieve email batch (`?mode=mixed&count=6`) |
| `POST` | `/api/check_email` | Submit phishing verdict for validation |
| `GET` | `/api/quiz` | Fetch quiz questions (`?difficulty=medium`) |
| `POST` | `/api/quiz/answer` | Submit quiz answer and receive explanation |
| `GET` | `/api/threats` | Get threat encyclopedia entries (`?category=...`) |
| `GET` | `/api/stats` | Dashboard statistics and metrics |
| `POST` | `/api/score` | Calculate badge achievement from score |

---

## Security Concepts Covered

### OWASP Top 10 Coverage

- **A01** — Broken Access Control
- **A02** — Cryptographic Failures (Man-in-the-Middle)
- **A03** — Injection (SQL Injection, XSS)
- **A07** — Identification and Authentication Failures (Credential Stuffing, Phishing)
- **A08** — Software and Data Integrity Failures (Ransomware)

### Attack Categories

- **Social Engineering** — Phishing, Spear Phishing, Vishing, Smishing, BEC/Whaling
- **Web Attacks** — SQL Injection, Cross-Site Scripting (XSS)
- **Network Attacks** — Man-in-the-Middle, ARP Poisoning, SSL Stripping
- **Malware** — Ransomware, Double Extortion Tactics
- **Authentication Attacks** — Credential Stuffing, Password Spraying

---

## Roadmap

Planned future enhancements:

- User authentication with persistent scores
- Leaderboard for multi-user training
- Additional threat profiles (supply chain, zero-day)
- Integration with real threat intelligence feeds (AlienVault OTX)
- Multilingual support (Turkish, Hungarian, German)
- Mobile-responsive improvements
- Export training certificates (PDF)

---

## Author

**Sadaf Ahmadli**  
MSc Cybersecurity Student at Eötvös Loránd University (ELTE), Budapest  
TryHackMe Top 8% Globally 

- LinkedIn: [sadaf-ahmadli](https://www.linkedin.com/in/sadaf-ahmadli-4863a4233/)
- GitHub: [Sedefehmdl](https://github.com/Sedefehmdl)
- Behance: [sedefehmdl](https://behance.net/sedefehmdl)

---

## License

This project is licensed under the MIT License. It is intended for educational purposes.

---

## Acknowledgments

- OWASP Foundation — for the Top 10 framework and security research
- TryHackMe — for hands-on security training that inspired this project
- ELTE Budapest — for cybersecurity coursework foundation
- Public threat reports from IBM Security, Verizon DBIR, and CISA
