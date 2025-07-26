# 🔍 OSINT-Search

A personal project that helps you perform OSINT (Open Source Intelligence) searches across the web by keyword (e-mail, phone number, username, etc.) using:
- ✅ CLI script (`main.py`)
- 🤖 Telegram bot (`bot.py`)
- 🌐 Web interface with Flask (`app.py` + `index.html`)

All results are stored in a local SQLite database (`osint.db`).

---

## 📦 About the project
This project has three parts:
- **main.py** – Command-line script to search and save results
- **bot.py** – Telegram bot for searching directly from Telegram
- **app.py + index.html** – Simple web app to search from a browser

The search is done via Google using the `googlesearch` library, and results are saved into `osint.db`.

---

## 🛠 Tech stack
- Python 3
- Flask
- telebot
- requests
- googlesearch-python
- SQLite3
- HTML + JavaScript (frontend)

---

## 🚀 How to run locally

### 1. Clone the repository
```bash
git clone https://github.com/Komronbek-Urinboev/OSINT-Search.git
cd OSINT-Search
```
2. Install dependencies
```bash
pip install flask pyTelegramBotAPI googlesearch-python
```

3. Run parts individually
✅ CLI script:
```bash
python main.py
🤖 Telegram bot:
```
Replace "TOKEN" in bot.py with your actual bot token
python bot.py
```bash
🌐 Web app:

python app.py
Then open http://127.0.0.1:5000 in your browser.
```
⚠️ Disclaimer

This is an educational project for learning and demonstration purposes only.
It is not intended for real-world investigations, and scraping Google may violate its terms of service.