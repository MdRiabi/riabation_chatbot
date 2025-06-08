import sqlite3

def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
                    user_id TEXT,
                    role TEXT,
                    content TEXT)''')
    conn.commit()
    conn.close()
