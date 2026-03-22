# 🚀 Automation Suite — All-in-One Python Automation Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

A powerful, modular, and professional **GUI-based automation platform** built with **PyQt6**, designed to centralize and execute multiple automation tools from a single interface.

---

## 🔥 Overview

**Automation Suite** is a unified desktop application that integrates multiple real-world automation scripts into a clean, modern GUI.

Instead of running scripts manually via terminal, users can:
- Launch tools with one click
- Monitor real-time execution logs
- Manage processes efficiently

---

## ✨ Features

### 🎯 Core Features
- ✅ Centralized automation dashboard
- ✅ One-click execution of scripts
- ✅ Live terminal output panel inside GUI
- ✅ Automatic process termination (no conflicts)
- ✅ Dark-themed professional UI (QSS styling)
- ✅ Modular & scalable architecture

---

### 📟 Process Management
- Runs scripts using `QProcess`
- Captures **stdout + stderr** in real-time
- Prevents overlapping executions
- Clean termination before new process starts

---

### 🎨 UI/UX Highlights
- Modern dark theme
- Smooth hover & click animations
- Glassmorphism-inspired styling
- Scrollable dynamic layout

---

## 🧰 Automation Modules

### 📧 Communication Automation
- Bulk Email Sender (Gmail API)
- Email Scheduler
- SMS Automation (Twilio)
- WhatsApp Automation
- Telegram Bots:
  - AutoGuide Bot
  - MentorAI Bot

---

### 🌐 Web & Scraping Automation
- Harmbench dataset scraper
- Automated login + scraping tools
- Currency rate scraper
- Multi-site scraping utilities

---

### 📊 Monitoring & Dashboards
- NetPulse Speedometer (Streamlit)
- System Resource Monitor
- Live Stock Notifier Dashboard

---

### 📁 File System Automation (25 Tools)
- JSON ↔ CSV Converter
- XML ↔ JSON Converter
- Merge CSV Files
- Split Text Files
- File Organizer
- Duplicate File Remover
- Folder Monitor & Backup
- Compression & Extraction Tools
- PDF Tools:
  - Merge
  - Split
  - Watermark
  - Convert (PDF ↔ Word)
- OCR (Image → Text)
- Bulk Rename Utilities

---

### 🤖 Bots & Automation
- Instagram Automation Bot
- GitHub Contribution Bot
- NetSec Automator

---

## 🏗️ Project Structure


AutomationSuite/
│
├── app.py # Main PyQt6 GUI
├── style.qss # UI Styling
│
├── backend/
│ └── runner.py # Process execution logic (QProcess)
│
├── ui/
│ └── components.py # Custom UI components (buttons, etc.)
│
├── universal_main.py # Central automation router
│
└── AutomationScripts/
├── bulk_email_sender/
├── stock_notifier/
├── file-system-automation/
├── web_scraping/
└── ...


---

## ⚙️ Tech Stack

- **Python 3.10+**
- **PyQt6** — GUI framework
- **Streamlit** — interactive dashboards
- **Selenium** — browser automation
- **Google APIs** — Gmail automation
- **Twilio API** — SMS automation
- **Plotly** — data visualization

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/automation-suite.git
cd automation-suite
2️⃣ Create Virtual Environment
python -m venv senv
senv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py
🧠 How It Works
GUI buttons trigger backend commands via QProcess
Each automation runs in an isolated process
Output streams are captured and displayed live
Previous processes are terminated before new execution
⚠️ Common Issues & Fixes
❌ Unicode Error (Windows)

Fix:

import sys
sys.stdout.reconfigure(encoding='utf-8')
❌ Missing credentials.json (Gmail API)
Place credentials.json in project root
Enable Gmail API in Google Cloud Console
❌ Streamlit Home Directory Error

Set environment variable:

set USERPROFILE=C:\Users\YourUsername
❌ Selenium Chrome Error

Install Chrome browser or specify path:

options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
```
## Stability Features
✅ Safe subprocess execution
✅ Error logging in GUI
✅ No CLI blocking issues
✅ Controlled environment per script
📌 Future Enhancements
📂 File picker dialogs (no hardcoded paths)
📊 Progress bars for tasks
🧠 AI-powered automation suggestions
🖥️ Task manager (CPU/RAM usage)
☁️ Cloud-based automation control
🤝 Contributing

## Contributions are welcome!

Steps:

Fork the repo
Create a new branch
Make changes
Submit a Pull Request


## 👨‍💻 Author

Sanchayan Ghosh

Automation Systems Developer
AI & Security Researcher
Builder of advanced automation frameworks
⭐ Support

## If you like this project:

⭐ Star the repository
🍴 Fork it
📢 Share it
💡 Inspiration

Built to eliminate repetitive manual work and create a centralized automation ecosystem for developers, researchers, and power users.
