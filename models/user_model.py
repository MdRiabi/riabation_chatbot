import sqlite3
from utils import security

def create_user(username, password):
    hashed = security.hash_password(password)
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    hashed = security.hash_password(password)
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    if result:
       return security.verify_password(password, result[0])
        
    return False
