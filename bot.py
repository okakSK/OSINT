import os
import sqlite3
import telebot
from googlesearch import search    # pip install googlesearch-python

# ====== Settings ======
BOT_TOKEN = os.getenv("TOKEN", "TOKEN")
DB_PATH = 'osint.db'

bot = telebot.TeleBot(BOT_TOKEN)

# ====== DB Initialization ======
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT,
    url TEXT
)
''')
conn.commit()

# /start command
@bot.message_handler(commands=['start'])
def cmd_start(msg):
    bot.send_message(
        msg.chat.id,
        "Hello! Please enter a query for OSINT search (e-mail, phone number, username):"
    )
    bot.register_next_step_handler(msg, handle_search)

def handle_search(msg):
    keyword = msg.text.strip()
    chat_id = msg.chat.id

    bot.send_message(chat_id, f"Searching for mentions of: {keyword}")

    try:
        urls = search(keyword, num_results=10, lang="ru")
        for url in urls:
            bot.send_message(chat_id, f"Found: {url}")
            cursor.execute(
                'INSERT INTO results (keyword, url) VALUES (?, ?)',
                (keyword, url)
            )
        conn.commit()
    except Exception as e:
        bot.send_message(chat_id, f"Search error: {e}")

    bot.send_message(chat_id, "Done!")

if __name__ == "__main__":
    bot.infinity_polling()
