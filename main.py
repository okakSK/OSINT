import sqlite3
from googlesearch import search

# Creating DB and connecting
conn = sqlite3.connect('osint.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT,
    url TEXT
)
''')
conn.commit()

def osint_search_and_save(keyword):
    print(f"Searching mentions for query: {keyword}")
    for url in search(keyword, num_results=10, lang="ru"):
        print(f"Found: {url}")
        cursor.execute('INSERT INTO results (keyword, url) VALUES (?, ?)', (keyword, url))
    conn.commit()
    print("Data saved to the database.")

if __name__ == "__main__":
    query = input("What are we searching for? (e-mail, phone number, username): ")
    osint_search_and_save(query)

    print("Done! Check the results table in osint.db")
